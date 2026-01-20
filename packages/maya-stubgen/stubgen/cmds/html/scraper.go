package html

import (
	"fmt"
	"log"
	"path/filepath"
	"slices"
	"strings"
	"sync"

	"maya-stubgen/stubgen/cmds/utils"

	"github.com/gocolly/colly"
)

const URL = "https://help.autodesk.com/cloudhelp/2026/ENU/Maya-Tech-Docs/CommandsPython/index_all.html"

// if this is present in the argument description,
// the argument does not become bool in query mode
var query_mandatory_value_str = "In query mode, this flag needs a value"

func ScrapeCmdsDocs(cacheDir string) {

	// Thread-safe slice to collect results
	var results []utils.MayaCmd
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
		cmd := utils.MayaCmd{
			ReturnType: "None",
		}
		cmdInfo := utils.MayaCmdInfo{
			Cmd:           &cmd,
			HasQueryFlags: false,
			HasEditFlags:  false,
		}
		ctx.Put("cmd", &cmd)         // attach a fresh struct for this page
		ctx.Put("cmdInfo", &cmdInfo) // attach a fresh info struct for this page
		c2.Request("GET", link, nil, ctx, nil)
	})

	c.OnError(func(r *colly.Response, err error) {
		fmt.Println(err)
	})

	// Get the name of the command
	c2.OnHTML("h1", func(h *colly.HTMLElement) {
		scrapeName(h)
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
		cmdInfo := r.Ctx.GetAny("cmdInfo").(*utils.MayaCmdInfo)

		mu.Lock()
		cmdInfo.ResolveQueryAndEdit()
		cmdInfo.ResolveReturnTypes()
		results = append(results, *cmdInfo.Cmd)
		mu.Unlock()
	})

	c.Visit(URL)
	c.Wait()
	c2.Wait()

	out_docspec_dir := filepath.Join(cacheDir, "docspec", "html")
	utils.WriteDocspecJson(out_docspec_dir, results)
}

func scrapeName(h *colly.HTMLElement) {
	cmd := h.Request.Ctx.GetAny("cmd").(*utils.MayaCmd)

	cmd.Name = strings.TrimSpace(h.Text)
	cmd.Name = strings.Split(cmd.Name, " ")[0]

	log.Println("[HTML Scraper] Scraping", cmd.Name)
}

func scrapeFlags(h *colly.HTMLElement) {
	cmdInfo := h.Request.Ctx.GetAny("cmdInfo").(*utils.MayaCmdInfo)
	cmd := cmdInfo.Cmd

	next := h.DOM.Next()
	flag_description := strings.TrimSpace(next.Text())

	name := strings.TrimSpace(h.ChildText("td:nth-child(1) code"))
	name = strings.Split(name, "(")[0]

	if name == "" {
		return
	}

	melTyp := strings.TrimSpace(h.ChildText("td:nth-child(2) code i"))
	typ := utils.MelTypeToPython(melTyp)

	modes := h.ChildAttrs("td:nth-child(3) img", "title")
	hasQueryMode := slices.Contains(modes, "query")
	hasEditMode := slices.Contains(modes, "edit")
	hasMultiUseMode := slices.Contains(modes, "multiuse")

	if hasMultiUseMode {
		typ = fmt.Sprintf("Multiuse[%s]", typ)
	}

	is_mandatory_query := strings.Contains(flag_description, query_mandatory_value_str)
	if hasQueryMode && !is_mandatory_query {
		cmdInfo.ReturnTypeList = append(cmdInfo.ReturnTypeList, melTyp)
		if typ != "bool" {
			typ = fmt.Sprintf("Queryable[%s]", typ)
		}
	}

	cmd.KeywordArguments = append(cmd.KeywordArguments, utils.Flag{Name: name, Type: typ, Value: "..."})

	if !cmdInfo.HasQueryFlags && hasQueryMode {
		cmdInfo.HasQueryFlags = true
	}
	if !cmdInfo.HasEditFlags && hasEditMode {
		cmdInfo.HasEditFlags = true
	}
}

func scrapeReturn(h *colly.HTMLElement) {
	cmdInfo := h.Request.Ctx.GetAny("cmdInfo").(*utils.MayaCmdInfo)

	var mel_return_type string
	switch h.Name {
	case "table":
		h.ForEach("tr td[valign]", func(i int, h *colly.HTMLElement) {
			cmdInfo.ReturnTypeList = append(cmdInfo.ReturnTypeList, h.Text)
		})
	case "p":
		mel_return_type = strings.TrimSpace(h.Text)
		cmdInfo.ReturnTypeList = append(cmdInfo.ReturnTypeList, mel_return_type)
	}
}
