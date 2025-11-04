package html

import (
	"encoding/json"
	"fmt"
	"log"
	"os"
	"path/filepath"
	"regexp"
	"slices"
	"strconv"
	"strings"
	"sync"

	"maya-stubgen/stubgen/cmds/utils"

	"github.com/gocolly/colly"
)

const URL = "https://help.autodesk.com/cloudhelp/2026/ENU/Maya-Tech-Docs/CommandsPython/index_all.html"

var union_regex = regexp.MustCompile(`(?:\w+)\|(?:\w+)`)
var array_regex = regexp.MustCompile(`(?P<type>\w+)\[(?P<length>\d+|\.\.\.)?\]`)
var tuple_regex = regexp.MustCompile(`\[(?P<types>.+)\]`)
var synposis_regex = regexp.MustCompile(`\((?P<args>.+)\)`)

// if this is present in the argument description,
// the argument does not become bool in query mode
var query_mandatory_value_str = "In query mode, this flag needs a value"

func ScrapeCmdsDocs(cacheDir string) {

	// Thread-safe slice to collect results
	var results []utils.MayaCmd
	var mu sync.Mutex

	c := colly.NewCollector(
		colly.AllowedDomains("help.autodesk.com"),
		colly.MaxDepth(1),
		colly.Async(true),
	)
	c2 := c.Clone()

	c.OnHTML("a[href]", func(h *colly.HTMLElement) {
		link := h.Request.AbsoluteURL(h.Attr("href"))
		ctx := colly.NewContext()
		cmd := utils.MayaCmd{}
		cmd.ReturnType = "None"
		ctx.Put("cmd", &cmd) // attach a fresh struct for this page
		c2.Request("GET", link, nil, ctx, nil)
	})

	c.OnError(func(r *colly.Response, err error) {
		fmt.Println(err)
	})

	// Get the name of the command
	c2.OnHTML("h1", func(h *colly.HTMLElement) {
		scrapeName(h)
	})

	// Get positional arguments from the synopsis
	c2.OnHTML("p[id=synopsis] code", func(h *colly.HTMLElement) {
		scrapeSynopsis(h)
	})

	// Get the cmds.Flags (ie: Keyword Arguments)
	c2.OnHTML("h2:contains('cmds.Flags') ~ a + table tr[bgcolor]", func(h *colly.HTMLElement) {
		scrapeFlags(h)
	})

	// Used if the Return Value is a <table>
	c2.OnHTML("h2:contains('Return value') + table", func(h *colly.HTMLElement) {
		scrapeReturn(h)
	})

	// Used if the Return Value is a <p>
	c2.OnHTML("h2:contains('Return value') + p", func(h *colly.HTMLElement) {
		scrapeReturn(h)
	})

	// gather all the scraped commands
	c2.OnScraped(func(r *colly.Response) {
		cmd := r.Ctx.GetAny("cmd").(*utils.MayaCmd)

		mu.Lock()
		results = append(results, *cmd)
		mu.Unlock()
	})

	c.Visit(URL)
	c.Wait()
	c2.Wait()

	slices.SortFunc(results, func(a utils.MayaCmd, b utils.MayaCmd) int {
		asdf := []string{a.Name, b.Name}
		slices.Sort(asdf)

		if asdf[0] == a.Name {
			return -1
		} else {
			return 1
		}
	})

	data, err := json.MarshalIndent(results, "", "  ")
	if err != nil {
		log.Fatal("Error encoding JSON:", err)
	}

	cmdsCacheDir := filepath.Join(cacheDir, "docspec")
	if err := os.MkdirAll(cmdsCacheDir, os.ModePerm); err != nil {
		log.Fatal("Error creating docspec cache dir", err)
	}

	cmdsCachefile := filepath.Join(cmdsCacheDir, "cmds.json")
	if err := os.WriteFile(cmdsCachefile, data, os.ModePerm); err != nil {
		log.Fatal("Error writing file:", err)
	}
}

func scrapeName(h *colly.HTMLElement) {
	cmd := h.Request.Ctx.GetAny("cmd").(*utils.MayaCmd)

	cmd.Name = strings.TrimSpace(h.Text)
	cmd.Name = strings.Split(cmd.Name, " ")[0]
}

func scrapeSynopsis(h *colly.HTMLElement) {
	// cmd := h.Request.Ctx.GetAny("cmd").(*cmds.MayaCmd)
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
}

func scrapeFlags(h *colly.HTMLElement) {
	cmd := h.Request.Ctx.GetAny("cmd").(*utils.MayaCmd)

	next := h.DOM.Next()
	flag_description := strings.TrimSpace(next.Text())

	name := strings.TrimSpace(h.ChildText("td:nth-child(1) code"))
	name = strings.Split(name, "(")[0]

	if name == "" {
		return
	}

	typ := strings.TrimSpace(h.ChildText("td:nth-child(2) code i"))
	typ = mel_type_to_python(typ)

	modes := h.ChildAttrs("td:nth-child(3) img", "title")

	if slices.Contains(modes, "multiuse") {
		typ = fmt.Sprintf("Multiuse[%s]", typ)
	}

	is_query := slices.Contains(modes, "query")
	is_mandatory_query := strings.Contains(flag_description, query_mandatory_value_str)

	if is_query && !is_mandatory_query && typ != "bool" {
		typ = fmt.Sprintf("Queryable[%s]", typ)
	}

	cmd.KeywordArguments = append(cmd.KeywordArguments, utils.Flag{Name: name, Type: typ, Value: "..."})
}

func scrapeReturn(h *colly.HTMLElement) {
	cmd := h.Request.Ctx.GetAny("cmd").(*utils.MayaCmd)

	var mel_return_type string
	switch h.Name {
	case "table":
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
			python_type = fmt.Sprintf("Tuple[%s]", tuple_content)
		} else {
			python_type = fmt.Sprintf("List[%s]", array_type)
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

		python_type = fmt.Sprintf("Tuple[%s]", strings.Join(python_types, ", "))

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
		value = "Unknown"
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
