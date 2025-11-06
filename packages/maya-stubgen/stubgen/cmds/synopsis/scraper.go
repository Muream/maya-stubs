package synopsis

import (
	"fmt"
	"log"
	"os"
	"path/filepath"
	"regexp"
	"slices"
	"strings"

	"maya-stubgen/stubgen/cmds/utils"
)

// Regex used to parse the header of a command's synopsis
// https://regex101.com/r/9595nC/1
var synopsis_header_regex = regexp.MustCompile(
	`(?P<name>\w+)( (\[flags\])? ?(?P<positional_args>.*))?`,
)

// used to tokenize the arguments of the synopsis header
// https://regex101.com/r/65YWDk/1
var synopsis_args_regex = regexp.MustCompile(
	`(?P<type>[\w+|]+)\[?(?P<repeat>\.\.\.)?\]?(?P<repeat2> \(up to \d+ times\))?`,
)

var synopsis_flag_regex = regexp.MustCompile(
	`-(?P<short_name>\w+)\s+` +
		`-(?P<long_name>\w+)` +
		`(?P<types>[\w\|\s\[\].]+)?\s?` +
		`(?P<multi_use>\(multi-use\))?\s?` +
		`(\(Query Arg (?P<query_arg_mandatory>Mandatory|Optional)\))?`,
)

var keywords = []string{
	"False",
	"None",
	"True",
	"and",
	"as",
	"assert",
	"async",
	"await",
	"break",
	"class",
	"continue",
	"def",
	"del",
	"elif",
	"else",
	"except",
	"finally",
	"for",
	"from",
	"global",
	"if",
	"import",
	"in",
	"is",
	"lambda",
	"nonlocal",
	"not",
	"or",
	"pass",
	"raise",
	"return",
	"try",
	"while",
	"with",
	"yield",
}

func ScrapeCmdsSynopsis(cacheDir string) {
	var results []utils.MayaCmd

	files, err := filepath.Glob(filepath.Join(cacheDir, "synopsis", "*.txt"))
	if err != nil {
		log.Fatal(err)
	}

	for _, file := range files {
		cmd := scrapeCmdSynopsis(file)
		cmd.ReturnType = "Unknown"
		results = append(results, cmd)
	}

	synopsis_cache_dir := filepath.Join(cacheDir, "docspec", "synopsis")
	utils.WriteDocspecJson(synopsis_cache_dir, results)

}

func scrapeCmdSynopsis(file string) utils.MayaCmd {
	content, err := os.ReadFile(file)
	if err != nil {
		log.Fatal(err)
	}

	lines := strings.Split(string(content), "\n")

	cmd := utils.MayaCmd{}

	for i, line := range lines {
		line = strings.TrimSpace(line)
		switch {
		case i == 0:
			name, flags := parse_header(line)
			cmd.Name = name
			cmd.PositionalArguments = flags

		case synopsis_flag_regex.MatchString(line):
			flag := parse_flag(line)
			cmd.KeywordArguments = append(cmd.KeywordArguments, flag)
		default:
		}
	}

	return cmd
}

func parse_header(line string) (command_name string, out_flags []utils.Flag) {
	header_re_matches := synopsis_header_regex.FindStringSubmatch(line)

	name_index := synopsis_header_regex.SubexpIndex("name")
	command_name = header_re_matches[name_index]

	positional_args_index := synopsis_header_regex.SubexpIndex("positional_args")
	positional_args := header_re_matches[positional_args_index]

	if positional_args == "" {
		return command_name, out_flags
	}

	args := synopsis_args_regex.FindAllString(positional_args, -1)

	type_index := synopsis_args_regex.SubexpIndex("type")
	repeat_index := synopsis_args_regex.SubexpIndex("repeat")
	repeat2_index := synopsis_args_regex.SubexpIndex("repeat2")

	for i, arg := range args {
		arg_match := synopsis_args_regex.FindStringSubmatch(arg)
		type_ := arg_match[type_index]
		repeat := arg_match[repeat_index]
		repeat2 := arg_match[repeat2_index]

		flag := utils.Flag{}

		flag.Type = utils.MelTypeToPython(type_)
		if repeat != "" || repeat2 != "" {
			// positional arg remainder (ie: *args)
			flag.Name = "*args"
		} else {
			// "named" positional argument
			// NOTE: maya expects positional only arguments so the name doesn't mean much
			flag.Name = fmt.Sprintf("arg%d", i)
		}

		out_flags = append(out_flags, flag)
	}

	return command_name, out_flags
}

func parse_flag(line string) (flag utils.Flag) {
	flags_match := synopsis_flag_regex.FindStringSubmatch(line)

	short_name_index := synopsis_flag_regex.SubexpIndex("short_name")
	short_name := strings.TrimSpace(flags_match[short_name_index])

	long_name_index := synopsis_flag_regex.SubexpIndex("long_name")
	long_name := strings.TrimSpace(flags_match[long_name_index])

	types_index := synopsis_flag_regex.SubexpIndex("types")
	types := strings.TrimSpace(flags_match[types_index])

	arg_type := "Unknown"
	switch {

	case types == "":
		arg_type = "bool"

	case strings.Contains(types, " "):
		arg_type = utils.MelTypeToPython("[" + types + "]")

	default:
		arg_type = utils.MelTypeToPython(types)

	}

	if slices.Contains(keywords, long_name) {
		flag.Name = short_name
	} else {
		flag.Name = long_name
	}
	flag.Type = arg_type

	return flag
}
