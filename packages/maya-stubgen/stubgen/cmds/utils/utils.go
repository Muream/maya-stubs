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
)

var _red_ = "\033[31m"
var _yellow_ = "\033[33m"
var _reset_ = "\033[0m"

// Regex used to parse union types, only used if "on|off" is not present
// https://regex101.com/r/F7eUmS/1
var union_regex = regexp.MustCompile(`(?:[^\|]+)(\|)(?:[^\|]+)`)

// Regex used to parse array types
// https://regex101.com/r/JlTdUv/1
var array_regex = regexp.MustCompile(`(?P<type>\w+)\[(?P<length>\d+|\.\.\.)?\]`)

// Regex used to parse tuple types
// https://regex101.com/r/ZOzAaK/1
var tuple_regex = regexp.MustCompile(`\[\s*(?P<types>[\w|]+)?\s*(?P<types>.*?)\s*\]$`)

func MelTypeToPython(type_name string) string {
	python_type := mel_type_to_python_complex(type_name)
	if python_type == "Unknown" {
		msg := fmt.Sprintf("Could not map MEL type to Python: %s", type_name)
		log.Printf("%s%s%s", _yellow_, msg, _reset_)
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
		match_groups := tuple_regex.FindAllStringSubmatch(type_name_cleaned, -1)
		for _, matches := range match_groups {
			for _, match := range matches[1:] {
				melTypes = append(melTypes, match)
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
		"":        "bool",
		"none":    "bool",
		"on|off":  "bool",
		// ranges
		"timerange":  "NullableRange[float]",
		"floatrange": "Range[float]",
		// misc
		"any": "Any",
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

func MergeMayaCmdSlices(synopsisCmds, htmlCmds *[]MayaCmd) []MayaCmd {
	// Make a mergeCmds map and populate it with values from synopsisCmds
	mergedCmdsMap := map[string]MayaCmd{}
	for _, synopsisCmd := range *synopsisCmds {
		mergedCmdsMap[synopsisCmd.Name] = synopsisCmd
	}

	for _, htmlCmd := range *htmlCmds {
		synopsisCmd, exists := mergedCmdsMap[htmlCmd.Name]

		// Add cmd from src, if not already present
		if !exists {
			mergedCmdsMap[htmlCmd.Name] = htmlCmd
			continue
		}

		// Prioritize synopsis positional arguments as they are more reliable than html docs
		mergedCmd := MayaCmd{
			Name:                htmlCmd.Name,
			PositionalArguments: synopsisCmd.PositionalArguments,
			KeywordArguments:    htmlCmd.KeywordArguments,
			ReturnType:          htmlCmd.ReturnType,
		}

		// Check if html and synopsis have query flags
		// If both have it, compare types and combine if they are not the same
		// (`optionVar` command has a union of str | bool for `query` kwarg)
		queryFlag := Flag {
			Name: "query",
			Type: "bool",
		}
		var synopsisQueryFlag Flag
		hasSynopsisQueryFlag := false
		for _, kwarg := range synopsisCmd.KeywordArguments {
			if hasSynopsisQueryFlag {
				break
			}
			if kwarg.Name == "query" {
				hasSynopsisQueryFlag = true
				synopsisQueryFlag = kwarg
			}
		}

		var htmlQueryFlag Flag
		hasHtmlQueryFlag := false
		htmlQueryIndex := -1
		for i, kwarg := range htmlCmd.KeywordArguments {
			if hasHtmlQueryFlag {
				break
			}
			if kwarg.Name == "query" {
				hasHtmlQueryFlag = true
				htmlQueryFlag = kwarg
				htmlQueryIndex = i
			}
		}

		if hasSynopsisQueryFlag && hasHtmlQueryFlag {
			if htmlQueryFlag.Type != synopsisQueryFlag.Type {
				queryFlag.Type = fmt.Sprintf("Union[%s, %s]", htmlQueryFlag.Type, synopsisQueryFlag.Type)
			}
			mergedCmd.KeywordArguments[htmlQueryIndex] = queryFlag
		} else if hasSynopsisQueryFlag && !hasHtmlQueryFlag {
			mergedCmd.KeywordArguments = slices.Insert(mergedCmd.KeywordArguments, 0, synopsisQueryFlag)
		}

		// Check if either html or synopsis have edit flag
		// if any of it does, certify it's first item on the kwargs slice
		editFlag := Flag{
			Name: "edit",
			Type: "bool",
		}
		
		htmlEditFlagIndex := slices.Index(htmlCmd.KeywordArguments, editFlag)
		if htmlEditFlagIndex > 0 {
			// It exists and is not the first item in the slice
			// pop it so it can be inserted at start afterwards
			mergedCmd.KeywordArguments = append(htmlCmd.KeywordArguments[:htmlEditFlagIndex], htmlCmd.KeywordArguments[htmlEditFlagIndex+1:]...)
		}
		
		// Certify `edit` kwarg is first on the slice
		synopsisEditFlagIndex := slices.Index(synopsisCmd.KeywordArguments, editFlag)
		if synopsisEditFlagIndex > 0 || htmlEditFlagIndex > 0 {
			mergedCmd.KeywordArguments = slices.Insert(mergedCmd.KeywordArguments, 0, editFlag)
		}

		mergedCmdsMap[mergedCmd.Name] = mergedCmd
	}

	// Create slice from the map for returning
	mergedCmds := make([]MayaCmd, 0, len(mergedCmdsMap))
	for _, cmd := range mergedCmdsMap {
		mergedCmds = append(mergedCmds, cmd)
	}

	return mergedCmds
}
