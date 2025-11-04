package writer

import (
	"bufio"
	"encoding/json"
	"fmt"
	"log"
	"os"
	"path/filepath"
	"strings"
	"text/template"
)

type MayaCmd struct {
	Name             string `json:"name"`
	Arguments        []Flag `json:"arguments"`
	KeywordArguments []Flag `json:"keyword_arguments"`
	ReturnType       string `json:"return_type"`
}

type Flag struct {
	Name  string `json:"name"`
	Type  string `json:"type"`
	Value string `json:"value"`
}

func render_flag(flag Flag) string {
	var value string
	if flag.Value == "" {
		value = ""
	} else {
		value = fmt.Sprintf(" = %s", flag.Value)
	}
	return fmt.Sprintf("%s: %s%s", flag.Name, flag.Type, value)
}

func RenderArgs(positional_flags []Flag, keyword_flags []Flag) string {
	rendered_flags := []string{}
	if len(positional_flags) > 0 {
		for i, flag := range positional_flags {
			rendered_flags = append(rendered_flags, fmt.Sprintf("arg%d: %s", i, flag.Type))
		}
		rendered_flags = append(rendered_flags, "/")
	}

	for _, flag := range keyword_flags {
		flag.Value = "..."
		rendered_flags = append(rendered_flags, render_flag(flag))
	}

	res := strings.Join(rendered_flags, ", ")
	// if res != "" {
	// 	res += ","
	// }
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

	content, err := os.ReadFile(filepath.Join(cacheDir, "docspec", "cmds.json"))
	if err != nil {
		log.Fatal("Error when opening file: ", err)
	}

	var payload []MayaCmd
	err = json.Unmarshal(content, &payload)
	if err != nil {
		log.Fatal("Error during Unmarshal: ", err)
	}

	f, err := os.Create(filepath.Join(outDir, "maya-stubs", "cmds", "__init__.pyi"))
	if (err) != nil {
		log.Fatal("Error creating file: ", err)
	}
	defer f.Close()

	w := bufio.NewWriter(f)

	w.WriteString("# pyright: reportExplicitAny=false\n")
	w.WriteString("from typing import Any, Callable, TypeVar\n\n\n")

	w.WriteString("Unknown = Any\n\n")

	w.WriteString("_T = TypeVar(\"_T\")\n\n")

	w.WriteString("Queryable = bool | _T\n")
	w.WriteString("Multiuse = _T | list[_T]\n")
	w.WriteString("Range = tuple[_T] | tuple[_T, _T]\n")
	w.WriteString("NullableRange = Range[_T | None]\n\n")

	for _, cmd := range payload {
		if err := tmpl.Execute(w, cmd); err != nil {
			log.Fatal("Error executing template: ", err)
		}
	}

	w.Flush()
}
