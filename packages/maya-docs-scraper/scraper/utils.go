package scraper

import (
	"fmt"
	"log"
	"regexp"
	"slices"
	"strconv"
	"strings"

	"github.com/gocolly/colly"
)

var global_command MayaCmd
var global_flag string

var union_regex = regexp.MustCompile(`(?:\w+)\|(?:\w+)`)
var array_regex = regexp.MustCompile(`(?P<type>\w+)\[(?P<length>\d+|\.\.\.)?\]`)
var tuple_regex = regexp.MustCompile(`\[(?P<types>.+)\]`)
var synposis_regex = regexp.MustCompile(`\((?P<args>.+)\)`)

func scrapeName(h *colly.HTMLElement) {
	cmd := h.Request.Ctx.GetAny("cmd").(*MayaCmd)

	cmd.Name = strings.TrimSpace(h.Text)
	cmd.Name = strings.Split(cmd.Name, " ")[0]

	// log.Printf("Command: %s\n", cmd.Name)
	global_command = *cmd
}

func scrapeSynopsis(h *colly.HTMLElement) {
	// cmd := h.Request.Ctx.GetAny("cmd").(*MayaCmd)
	txt := strings.ReplaceAll(h.Text, "\n", "")
	matches := synposis_regex.FindStringSubmatch(txt)

	if len(matches) == 0 {
		return
	}

	args_str := strings.Trim(matches[0], "() ")
	args := strings.Split(args_str, ",")
	if len(args) == 0 {
		return
	}

	first_arg := strings.TrimSpace(args[0])
	if strings.Contains(first_arg, "=") {
		return
	}

	va_args := strings.Split(first_arg, " ")
	py_va_args := make([]string, len(va_args))
	for i, t := range va_args {
		py_va_args[i] = mel_type_to_python(t)
	}
	fmt.Println(py_va_args)
	// fmt.Println()
	fmt.Println()
}

func scrapeFlags(h *colly.HTMLElement) {
	cmd := h.Request.Ctx.GetAny("cmd").(*MayaCmd)

	name := strings.TrimSpace(h.ChildText("td:nth-child(1) code"))
	name = strings.Split(name, "(")[0]

	if name == "" {
		return
	}

	global_flag = name

	typ := strings.TrimSpace(h.ChildText("td:nth-child(2) code i"))
	// typ = strings.Trim(typ, " [,]")
	typ = mel_type_to_python(typ)

	cmd.KeywordArguments = append(cmd.KeywordArguments, Flag{name, typ})
}

func scrapeReturn(h *colly.HTMLElement) {
	cmd := h.Request.Ctx.GetAny("cmd").(*MayaCmd)

	var mel_return_type string
	switch h.Name {
	case "table":
		// mel_return_type = h.ChildText("tr td[valign]")
		types := []string{}
		h.ForEach("tr td[valign]", func(i int, h *colly.HTMLElement) {
			types = append(types, h.Text)
		})
		slices.Sort(types)
		types = slices.Compact(types)
		mel_return_type = strings.Join(types, "|")
	case "p":
		mel_return_type = strings.TrimSpace(h.Text)
	}

	python_return_type := mel_type_to_python(mel_return_type)

	cmd.ReturnType = python_return_type
}

func mel_type_to_python(type_name string) string {
	python_type := mel_type_to_python_complex(type_name)
	if python_type == "Unknown" {
		log.Printf("Could not map MEL type to Python: %s", type_name)
	}
	return python_type
}

func mel_type_to_python_complex(type_name string) string {
	var python_type string

	switch {
	case union_regex.MatchString(type_name):
		if type_name == "on|off" {
			break
		}
		mel_types := strings.Split(type_name, "|")
		python_types := []string{}

		for _, mel_type := range mel_types {
			python_types = append(python_types, mel_type_to_python(mel_type))
		}

		python_type = strings.Join(python_types, " | ")
	case array_regex.MatchString(type_name):
		matches := array_regex.FindStringSubmatch(type_name)
		type_index := array_regex.SubexpIndex("type")
		array_type := mel_type_to_python(matches[type_index])

		length_index := array_regex.SubexpIndex("length")
		array_length := matches[length_index]
		if array_length != "" && array_length != "..." {
			length, err := strconv.ParseInt(array_length, 10, 32)
			if err != nil {
				log.Panicf("Array Length is not an int: %s", array_length)
			}
			s := make([]string, length)
			for i := range s {
				s[i] = array_type
			}
			tuple_content := strings.Join(s, ", ")
			python_type = fmt.Sprintf("tuple[%s]", tuple_content)
		} else {
			python_type = fmt.Sprintf("list[%s]", array_type)
		}

	case tuple_regex.MatchString(type_name):
		// Some tuples look like this [[, int, str, ]]
		// TODO: Should we delete the double brackets?
		type_name_cleaned := strings.ReplaceAll(type_name, "[, ", "[")
		type_name_cleaned = strings.ReplaceAll(type_name_cleaned, ", ]", "]")

		matches := tuple_regex.FindStringSubmatch(type_name_cleaned)
		types_index := tuple_regex.SubexpIndex("types")
		mel_types_str := matches[types_index]

		mel_types := parse_tuple_types(mel_types_str)

		python_types := []string{}

		for _, mel_type := range mel_types {
			python_types = append(python_types, mel_type_to_python(mel_type))
		}

		python_type = fmt.Sprintf("tuple[%s]", strings.Join(python_types, ", "))

	default:
		python_type = mel_type_to_python_simple(type_name)
	}

	return python_type
}

func mel_type_to_python_simple(name string) string {
	type_map := map[string]string{
		// str
		"string":        "str",
		"name":          "str",
		"selectionitem": "str",
		"script":        "Callable[..., Any]",
		// float
		"float":  "float",
		"double": "float",
		"length": "float",
		"angle":  "float",
		"linear": "float",
		// int
		"int":         "int",
		"int64":       "int",
		"unsignedint": "int",
		"uint":        "int",
		"time":        "int",
		"indexrange":  "int",
		// bool
		"":        "bool",
		"boolean": "bool",
		"None":    "bool",
		"none":    "bool",
		"on|off":  "bool",
		"any":     "Any",
		// ranges
		"timerange":  "NullableRange[float]",
		"floatrange": "Range[float]",
	}
	value, ok := type_map[strings.ToLower(name)]
	if !ok {
		// value = "Unknown"
		fmt.Printf("%s::%s -> %s\n", global_command.Name, global_flag, name)
		value = name
	}
	return value
}

// simple depth based parser that is able to recognize nested tuples
func parse_tuple_types(types string) []string {
	var result []string
	var current strings.Builder
	depth := 0

	for _, r := range types {
		switch r {
		case '[':
			depth++
			current.WriteRune(r)
		case ']':
			depth--
			current.WriteRune(r)
		case ',':
			if depth == 0 {
				// Split here
				part := strings.TrimSpace(current.String())
				if part != "" {
					result = append(result, part)
				}
				current.Reset()
			} else {
				current.WriteRune(r)
			}
		default:
			current.WriteRune(r)
		}
	}

	// Add the last part
	if part := strings.TrimSpace(current.String()); part != "" {
		result = append(result, part)
	}

	return result
}
