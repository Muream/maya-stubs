package html

import (
	"fmt"
	"log"
	"path/filepath"
	"regexp"
	"slices"
	"strings"
	"sync"

	"maya-stubgen/stubgen/cmds/utils"

	"github.com/gocolly/colly"
)

var synposis_regex = regexp.MustCompile(`\((?P<args>.+)\)`)

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
		cmd := utils.MayaCmd{}
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

	// Get the cmds.Flags (ie: Keyword Arguments)
	c2.OnHTML("h2:contains('cmds.Flags') ~ a + table tr[bgcolor]", func(h *colly.HTMLElement) {
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
		cmd := r.Ctx.GetAny("cmd").(*utils.MayaCmd)

		mu.Lock()
		results = append(results, *cmd)
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

func scrapeSynopsis(h *colly.HTMLElement) {
	// cmd := h.Request.Ctx.GetAny("cmd").(*cmds.MayaCmd)
	txt := strings.ReplaceAll(h.Text, "\n", "")
	matches := synposis_regex.FindStringSubmatch(txt)

	if len(matches) == 0 {
		return
	}

	args_str := strings.Trim(matches[0], "() ")
	args := strings.Split(args_str, ",")
	if len(args) == 0 {
		return
	}

	first_arg := strings.TrimSpace(args[0])
	if strings.Contains(first_arg, "=") {
		return
	}

	va_args := strings.Split(first_arg, " ")
	py_va_args := make([]string, len(va_args))
	for i, t := range va_args {
		py_va_args[i] = utils.MelTypeToPython(t)
	}
}

func scrapeFlags(h *colly.HTMLElement) {
	cmd := h.Request.Ctx.GetAny("cmd").(*utils.MayaCmd)

	next := h.DOM.Next()
	flag_description := strings.TrimSpace(next.Text())

	name := strings.TrimSpace(h.ChildText("td:nth-child(1) code"))
	name = strings.Split(name, "(")[0]

	if name == "" {
		return
	}

	typ := strings.TrimSpace(h.ChildText("td:nth-child(2) code i"))
	typ = utils.MelTypeToPython(typ)

	modes := h.ChildAttrs("td:nth-child(3) img", "title")

	if slices.Contains(modes, "multiuse") {
		typ = fmt.Sprintf("Multiuse[%s]", typ)
	}

	is_query := slices.Contains(modes, "query")
	is_mandatory_query := strings.Contains(flag_description, query_mandatory_value_str)

	if is_query && !is_mandatory_query && typ != "bool" {
		typ = fmt.Sprintf("Queryable[%s]", typ)
	}

	cmd.KeywordArguments = append(cmd.KeywordArguments, utils.Flag{Name: name, Type: typ, Value: "..."})
}

func scrapeReturn(h *colly.HTMLElement) {
	cmd := h.Request.Ctx.GetAny("cmd").(*utils.MayaCmd)

	var mel_return_type string
	switch h.Name {
	case "table":
		types := []string{}
		h.ForEach("tr td[valign]", func(i int, h *colly.HTMLElement) {
			types = append(types, h.Text)
		})
		slices.Sort(types)
		types = slices.Compact(types)
		mel_return_type = strings.Join(types, "|")
	case "p":
		mel_return_type = strings.TrimSpace(h.Text)
	}

	python_return_type := utils.MelTypeToPython(mel_return_type)

	cmd.ReturnType = python_return_type
}
