package stubs_writer

import (
	"bufio"
	"encoding/json"
	"fmt"
	"log"
	"os"
	"strings"
	"text/template"
)

type MayaCmd struct {
	Name       string `json:"name"`
	Arguments  []Flag `json:"arguments"`
	ReturnType string `json:"return_type"`
}

type Flag struct {
	Name string `json:"name"`
	Type string `json:"type"`
}

func render_flag(flag Flag) string {
	return fmt.Sprintf("%s: %s", flag.Name, flag.Type)
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
		rendered_flags = append(rendered_flags, render_flag(flag))
	}
	return strings.Join(rendered_flags, ", ")
}

func WriteStubs() {

	tmplfile := "stubs_writer/function.tmpl"
	tmpl, err := template.New("function.tmpl").Funcs(template.FuncMap{
		"StringsJoin": strings.Join,
		"RenderArgs":  RenderArgs,
	}).ParseFiles(tmplfile)

	if err != nil {
		panic(err)
	}

	content, err := os.ReadFile("maya_cmds.json")
	if err != nil {
		log.Fatal("Error when opening file: ", err)
	}

	var payload []MayaCmd
	err = json.Unmarshal(content, &payload)
	if err != nil {
		log.Fatal("Error during Unmarshal: ", err)
	}

	f, err := os.Create("cmds.pyi")
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
