package writer

import (
	"bufio"
	"encoding/json"
	"fmt"
	"log"
	"os"
	"path/filepath"
	"sort"
	"strings"
	"text/template"

	"maya-stubgen/stubgen/cmds/utils"
)

func render_flag(flag utils.Flag) string {
	var value string
	if flag.Value == "" {
		value = ""
	} else {
		value = fmt.Sprintf(" = %s", flag.Value)
	}
	return fmt.Sprintf("%s: %s%s", flag.Name, flag.Type, value)
}

func RenderArgs(positional_flags []utils.Flag, keyword_flags []utils.Flag) string {
	starArgAdded := false

	rendered_flags := []string{}
	for i, flag := range positional_flags {

		argName := flag.Name
		argType := flag.Type

		if !starArgAdded {
			starArgAdded = strings.HasPrefix(argName, "*")
		}

		// If flag has no Name, use default name based on positinal flag index (arg0, arg1, etc...)
		if argName == "" {
			argName = fmt.Sprintf("arg%d", i)
		} else if strings.HasPrefix(argName, "*") {
			// *args found, indicate for forward slash placement
			starArgAdded = true
		}

		// If a *arg exists and there were previous positional args, add a forward slash to indicate previous mandatory args
		if starArgAdded && i != 0 && len(positional_flags) <= 1 {
			rendered_flags = append(rendered_flags, "/")
		}

		rendered_flags = append(rendered_flags, fmt.Sprintf("%s: %s", argName, argType))
	}

	// Add "*" empty positional if there is at least one keyword flag
	if !starArgAdded && len(positional_flags) == 0 && len(keyword_flags) > 0 {
		rendered_flags = append(rendered_flags, "*")
		starArgAdded = true
	}

	// Add forward slash if no "*" args were added before it
	if len(positional_flags) > 0 && len(keyword_flags) > 0 && !starArgAdded {
		rendered_flags = append(rendered_flags, "/")
	}

	for _, flag := range keyword_flags {
		flag.Value = "..."
		rendered_flags = append(rendered_flags, render_flag(flag))
	}

	res := strings.Join(rendered_flags, ", ")
	return res
}

func WriteStubs(cacheDir string, outDir string) {
	tmplfile := filepath.Join("packages", "maya-stubgen", "stubgen", "writer", "function.tmpl")
	tmpl, err := template.New("function.tmpl").Funcs(template.FuncMap{
		"StringsJoin": strings.Join,
		"RenderArgs":  RenderArgs,
	}).ParseFiles(tmplfile)

	if err != nil {
		panic(err)
	}

	content, err := os.ReadFile(filepath.Join(cacheDir, "docspec", "merged", "cmds.json"))
	if err != nil {
		log.Fatal("Error when opening file: ", err)
	}

	var payload []utils.MayaCmd
	err = json.Unmarshal(content, &payload)
	if err != nil {
		log.Fatal("Error during Unmarshal: ", err)
	}
	sort.Slice(payload, func(i, j int) bool {
		return payload[i].Name < payload[j].Name
	})

	cmds_out_dir := filepath.Join(outDir, "maya-stubs", "cmds")
	err = os.MkdirAll(cmds_out_dir, 0755)
	if (err) != nil {
		log.Fatal("Error creating directory: ", err)
	}

	f, err := os.Create(filepath.Join(cmds_out_dir, "__init__.pyi"))
	if (err) != nil {
		log.Fatal("Error creating file: ", err)
	}
	defer f.Close()

	w := bufio.NewWriter(f)

	w.WriteString("from __future__ import annotations\n\n")
	w.WriteString("from typing import Any, Callable, List, Optional, Tuple, TypeAlias, TypeVar, Union\n\n\n")

	w.WriteString("Unknown = Any\n\n")

	w.WriteString("_T = TypeVar(name=\"_T\")\n\n")

	w.WriteString("Queryable: TypeAlias = Union[bool, _T]\n")
	w.WriteString("Multiuse: TypeAlias = Union[_T, List[_T]]\n")
	w.WriteString("Range: TypeAlias = Union[Tuple[_T], Tuple[_T, _T]]\n")
	w.WriteString("NullableRange: TypeAlias = Range[Optional[_T]]\n\n")

	for _, cmd := range payload {
		if err := tmpl.Execute(w, cmd); err != nil {
			log.Fatal("Error executing template: ", err)
		}
	}

	w.Flush()
}
