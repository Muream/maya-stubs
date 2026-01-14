package utils

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

	"dario.cat/mergo"
)

var _red_ = "\033[31m"
var _yellow_ = "\033[33m"
var _reset_ = "\033[0m"

var union_regex = regexp.MustCompile(`(?:\w+)(\|)(?:\w+)`)
var array_regex = regexp.MustCompile(`(?P<type>\w+)\[(?P<length>\d+|\.\.\.)?\]`)
var tuple_regex = regexp.MustCompile(`\[\s*(?P<types>\w+)?\s*(?P<types>.*?)\s*\]$`)
var tuple_token_regex = regexp.MustCompile(`[\w|]+(?:\[[\d.]*\])?|[\[\]]`)

func MelTypeToPython(type_name string) string {
	python_type := mel_type_to_python_complex(type_name)
	if python_type == "Unknown" {
		// msg := fmt.Sprintf("Could not map MEL type to Python: %s", type_name)
		// log.Printf("%s%s%s", _yellow_, msg, _reset_)
	}
	return python_type
}

func mel_type_to_python_complex(type_name string) string {
	var python_type string

	switch {
	case union_regex.MatchString(type_name) && !strings.Contains(type_name, "on|off"):
		var mel_types []string
		match_groups := union_regex.FindAllStringSubmatch(type_name, -1)
		for _, matches := range match_groups {
			mel_types = append(mel_types, strings.Split(matches[0], "|")...)
		}
		python_types := []string{}

		for _, mel_type := range mel_types {
			python_types = append(python_types, MelTypeToPython(mel_type))
		}

		if len(python_types) > 1 {
			python_type = fmt.Sprintf("Union[%s]", strings.Join(python_types, ", "))
		} else {
			python_type = python_types[0]
		}

	case array_regex.MatchString(type_name):
		matches := array_regex.FindStringSubmatch(type_name)
		type_index := array_regex.SubexpIndex("type")
		array_type := MelTypeToPython(matches[type_index])

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
		type_name_cleaned = strings.ReplaceAll(type_name_cleaned, ", ", " ")

		var melTypes []string
		var index int = 0
		match_groups := tuple_regex.FindAllStringSubmatch(type_name_cleaned, -1)
		for _, matches := range match_groups {
			for _, match := range matches[1:] {
				if strings.Contains(match, "...") {
					melTypes[index-1] = fmt.Sprintf("%s...", melTypes[index-1])
					index++
					continue
				}
				melTypes = append(melTypes, match)
				index++
			}
		}
		mel_types_str := strings.Join(melTypes, " ")

		mel_types := parse_tuple_types(mel_types_str)

		python_types := []string{}

		for _, mel_type := range mel_types {
			python_types = append(python_types, MelTypeToPython(mel_type))
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
		"double": "float",
		"length": "float",
		"angle":  "float",
		"linear": "float",
		// int
		"int64":       "int",
		"unsignedint": "int",
		"uint":        "int",
		"time":        "int",
		"indexrange":  "int",
		// bool
		"boolean": "bool",
		"on|off":  "bool",
		// ranges
		"timerange":  "NullableRange[float]",
		"floatrange": "Range[float]",
		// misc
		"any":  "Any",
		"":     "None",
		"none": "None",
		// Python fallbacks
		"str":                  "str",
		"Callable[..., Any]":   "Callable[..., Any]",
		"float":                "float",
		"int":                  "int",
		"bool":                 "bool",
		"NullableRange[float]": "NullableRange[float]",
		"Range[float]":         "Range[float]",
		"Any":                  "Any",
		"None":                 "None",
	}
	value, ok := type_map[strings.ToLower(name)]
	if !ok {
		if !strings.Contains(name, "...") {
			value = "Unknown"
		} else {
			value = name
		}
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

		// A new group is being opened
		case '[':
			depth++
			current.WriteRune(r)

		// The current group is being closed
		case ']':
			depth--
			current.WriteRune(r)

		// Sometimes values are comma separated, sometimes space separated
		case ',', ' ':
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

func WriteDocspecJson(cacheDir string, commands []MayaCmd) {

	slices.SortFunc(commands, func(a MayaCmd, b MayaCmd) int {
		sort_array := []string{a.Name, b.Name}
		slices.Sort(sort_array)

		if sort_array[0] == a.Name {
			return -1
		} else {
			return 1
		}
	})

	data, err := json.MarshalIndent(commands, "", "  ")
	if err != nil {
		log.Fatal("Error encoding JSON:", err)
	}

	if err := os.MkdirAll(cacheDir, os.ModePerm); err != nil {
		log.Fatal("Error creating docspec cache dir", err)
	}

	cmdsCachefile := filepath.Join(cacheDir, "cmds.json")
	if err := os.WriteFile(cmdsCachefile, data, os.ModePerm); err != nil {
		log.Fatal("Error writing file:", err)
	}
}

func MergeMayaCmdSlices(synopsisCmds, htmlCmds []MayaCmd) []MayaCmd {
	mergedCmds := map[string]MayaCmd{}

	for _, synopsisCmd := range synopsisCmds {
		mergedCmds[synopsisCmd.Name] = synopsisCmd
	}

	for _, htmlCmd := range htmlCmds {
		if synopsisCmd, exists := mergedCmds[htmlCmd.Name]; exists {
			if err := mergo.Merge(&synopsisCmd, htmlCmd, mergo.WithOverride); err != nil {
				msg := fmt.Sprintf("Error merging cmd %s: %v", htmlCmd.Name, err)
				log.Printf("%s%s%s", _red_, msg, _reset_)
				continue
			}
			mergedCmds[htmlCmd.Name] = synopsisCmd
		} else {
			// Add cmd from src, if not already present
			mergedCmds[htmlCmd.Name] = htmlCmd
		}
	}

	result := make([]MayaCmd, 0, len(mergedCmds))
	for _, cmd := range mergedCmds {
		result = append(result, cmd)
	}

	return result
}
