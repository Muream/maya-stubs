package cmds

import (
	"maya-stubgen/stubgen/cmds/html"
	"maya-stubgen/stubgen/cmds/synopsis"
	"maya-stubgen/stubgen/writer"
)

func Run(outDir string, cacheDir string) {
	synopsis.ScrapeCmdsSynopsis(cacheDir)
	html.ScrapeCmdsDocs(cacheDir)
	writer.WriteStubs(cacheDir, outDir)
}
