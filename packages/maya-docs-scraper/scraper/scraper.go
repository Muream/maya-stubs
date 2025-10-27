package scraper

import (
	"encoding/json"
	"fmt"
	"log"
	"os"
	"slices"
	"sync"

	"github.com/gocolly/colly"
)

const URL = "https://help.autodesk.com/cloudhelp/2026/ENU/Maya-Tech-Docs/CommandsPython/index_all.html"

type MayaCmd struct {
	Name                string `json:"name"`
	PositionalArguments []Flag `json:"positional_arguments"`
	KeywordArguments    []Flag `json:"keyword_arguments"`
	ReturnType          string `json:"return_type"`
}

type Flag struct {
	Name string `json:"name"`
	Type string `json:"type"`
}

func ScrapeCmdsDocs() {

	// Thread-safe slice to collect results
	var results []MayaCmd
	var mu sync.Mutex

	c := colly.NewCollector(
		colly.AllowedDomains("help.autodesk.com"),
		colly.MaxDepth(1),
		colly.Async(true),
	)
	c2 := c.Clone()

	c.OnHTML("a[href]", func(h *colly.HTMLElement) {
		link := h.Request.AbsoluteURL(h.Attr("href"))
		ctx := colly.NewContext()
		cmd := MayaCmd{}
		cmd.ReturnType = "None"
		ctx.Put("cmd", &cmd) // attach a fresh struct for this page
		c2.Request("GET", link, nil, ctx, nil)
	})

	c.OnError(func(r *colly.Response, err error) {
		fmt.Println(err)
	})

	// Get the name of the command
	c2.OnHTML("h1", func(h *colly.HTMLElement) {
		scrapeName(h)
	})

	// Get positional arguments from the synopsis
	c2.OnHTML("p[id=synopsis] code", func(h *colly.HTMLElement) {
		scrapeSynopsis(h)
	})

	// Get the Flags (ie: Keyword Arguments)
	c2.OnHTML("h2:contains('Flags') ~ a + table tr[bgcolor]", func(h *colly.HTMLElement) {
		scrapeFlags(h)
	})

	// Used if the Return Value is a <table>
	c2.OnHTML("h2:contains('Return value') + table", func(h *colly.HTMLElement) {
		scrapeReturn(h)
	})

	// Used if the Return Value is a <p>
	c2.OnHTML("h2:contains('Return value') + p", func(h *colly.HTMLElement) {
		scrapeReturn(h)
	})

	// gather all the scraped commands
	c2.OnScraped(func(r *colly.Response) {
		cmd := r.Ctx.GetAny("cmd").(*MayaCmd)

		mu.Lock()
		results = append(results, *cmd)
		mu.Unlock()
	})

	c.Visit(URL)
	c.Wait()
	c2.Wait()

	slices.SortFunc(results, func(a MayaCmd, b MayaCmd) int {
		asdf := []string{a.Name, b.Name}
		slices.Sort(asdf)

		if asdf[0] == a.Name {
			return -1
		} else {
			return 1
		}
	})

	data, err := json.MarshalIndent(results, "", "  ")
	if err != nil {
		log.Fatal("Error encoding JSON:", err)
	}

	if err := os.WriteFile("maya_cmds.json", data, 0644); err != nil {
		log.Fatal("Error writing file:", err)
	}
}
