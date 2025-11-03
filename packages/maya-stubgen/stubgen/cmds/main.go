package cmds

import "maya-stubgen/stubgen/writer"

func Run(outDir string, cacheDir string) {
	ScrapeCmdsDocs(cacheDir)
	writer.WriteStubs(cacheDir, outDir)
}
