package synopsis

import (
	"fmt"
	"log"
	"os"
	"path/filepath"
	"regexp"
	"strings"

	"maya-stubgen/stubgen/cmds/utils"
)

var synopsis_header_regex = regexp.MustCompile(`(?P<name>\w+)( (\[flags\])? ?(?P<positional_args>.*))?`)

var synopsis_flag_regex = regexp.MustCompile(
	`-(?P<short_name>\w+)\s+` +
		`-(?P<long_name>\w+)` +
		`(?P<types>[\w\|\s\[\].]+)?\s?` +
		`(?P<multi_use>\(multi-use\))?\s?` +
		`(\(Query Arg (?P<query_arg_mandatory>Mandatory|Optional)\))?`,
)

func ScrapeCmdsSynopsis(cacheDir string) {
	var results []utils.MayaCmd

	files, err := filepath.Glob(filepath.Join(cacheDir, "synopsis", "*.txt"))
	if err != nil {
		log.Fatal(err)
	}

	for _, file := range files {
		cmd := scrapeCmdSynopsis(file)
		results = append(results, cmd)
		fmt.Println(cmd)
	}

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
			matches := synopsis_header_regex.FindStringSubmatch(line)

			name_index := synopsis_header_regex.SubexpIndex("name")
			cmd.Name = matches[name_index]

			positional_args_index := synopsis_header_regex.SubexpIndex("positional_args")
			//TODO: Positional Arguments should be properly supported and not be Named
			//Flags
			cmd.PositionalArguments = append(cmd.PositionalArguments, utils.Flag{"", matches[positional_args_index], ""})
		case synopsis_flag_regex.MatchString(line):
			// TODO: Parse Flags
		default:
		}
	}

	return cmd
}
