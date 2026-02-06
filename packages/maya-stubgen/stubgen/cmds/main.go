package cmds

import (
	"encoding/json"
	"log"
	"os"
	"path/filepath"

	"maya-stubgen/stubgen/cmds/html"
	"maya-stubgen/stubgen/cmds/synopsis"
	"maya-stubgen/stubgen/cmds/utils"
	"maya-stubgen/stubgen/writer"
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
	html_file := filepath.Join(cacheDir, "docspec", "html", "cmds.json")

	synopsis_content, err := os.ReadFile(synopsis_file)
	html_content, err := os.ReadFile(html_file)

	var synopsisCmds []utils.MayaCmd
	var htmlCmds []utils.MayaCmd

	err = json.Unmarshal(synopsis_content, &synopsisCmds)
	if err != nil {
		log.Fatal(err)
	}

	err = json.Unmarshal(html_content, &htmlCmds)
	if err != nil {
		log.Fatal(err)
	}

	mergedCmds := utils.MergeMayaCmdSlices(&synopsisCmds, &htmlCmds)

	merged_content, err := json.MarshalIndent(mergedCmds, "", "  ")
	if err != nil {
		log.Fatal(err)
	}

	merged_file := filepath.Join(cacheDir, "docspec", "merged", "cmds.json")
	err = os.MkdirAll(filepath.Dir(merged_file), 0755)
	if err != nil {
		log.Fatal(err)
	}

	err = os.WriteFile(merged_file, merged_content, 0644)
	if err != nil {
		log.Fatal("Error writing merged json: ", err)
	}

}
