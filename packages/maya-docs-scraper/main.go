package main

import (
	"maya-docs-scraper/scraper"
	"maya-docs-scraper/stubs_writer"
)

func main() {
	scraper.ScrapeCmdsDocs()
	stubs_writer.WriteStubs()
}
