package cmds

import (
	"encoding/json"
	"log"
	"maya-stubgen/stubgen/cmds/html"
	"maya-stubgen/stubgen/cmds/synopsis"
	"maya-stubgen/stubgen/writer"
	"os"
	"path/filepath"

	"dario.cat/mergo"
)

func Run(outDir string, cacheDir string) {
	synopsis.ScrapeCmdsSynopsis(cacheDir)
	html.ScrapeCmdsDocs(cacheDir)

	merge_results(cacheDir)

	writer.WriteStubs(cacheDir, outDir)
}

func merge_results(cacheDir string) {
	log.Println("Merging Synopsis & HTML Docspec")
	var err error

	synopsis_file := filepath.Join(cacheDir, "docspec", "synopsis", "cmds.json")
	html_file := filepath.Join(cacheDir, "docspec", "synopsis", "cmds.json")

	synopsis_content, err := os.ReadFile(synopsis_file)
	html_content, err := os.ReadFile(html_file)

	var a []any
	var b []any

	err = json.Unmarshal(synopsis_content, &a)
	if err != nil {
		log.Fatal(err)
	}

	err = json.Unmarshal(html_content, &b)
	if err != nil {
		log.Fatal(err)
	}

	err = mergo.Merge(&a, b, mergo.WithOverride)
	if err != nil {
		log.Fatal(err)
	}

	merged_content, err := json.Marshal(a)
	if err != nil {
		log.Fatal(err)
	}

	merged_file := filepath.Join(cacheDir, "docspec", "merged", "cmds.json")
	err = os.MkdirAll(filepath.Dir(merged_file), 0750)
	if err != nil {
		log.Fatal(err)
	}

	err = os.WriteFile(merged_file, merged_content, 0644)
	if err != nil {
		log.Fatal("Error writing merged json: ", err)
	}

}
