package utils

import (
	"slices"
	"strings"
)

type MayaCmd struct {
	Name                string   `json:"name"`
	PositionalArguments []Flag   `json:"positional_arguments"`
	KeywordArguments    []Flag   `json:"keyword_arguments"`
	ReturnType          string   `json:"return_type"`
	HasEditFlags        bool     `json:"has_edit_flags"`
	HasQueryFlags       bool     `json:"has_query_flags"`
	ReturnTypeList      []string `json:"return_type_list"`
}

type Flag struct {
	Name  string `json:"name"`
	Type  string `json:"type"`
	Value string `json:"value"`
}

func (cmd *MayaCmd) ResolveReturnTypes() {
	slices.Sort(cmd.ReturnTypeList)
	cmd.ReturnTypeList = slices.Compact(cmd.ReturnTypeList)

	// Convert individual return types to python to avoid duplicates (e.g.: name, string => str, str)
	pyList := []string{}
	for _, typ := range cmd.ReturnTypeList {
		pyList = append(pyList, MelTypeToPython(typ))
	}
	slices.Sort(pyList)
	pyList = slices.Compact(pyList)

	// Final clean conversion without duplicates
	cmd.ReturnType = MelTypeToPython(strings.Join(pyList, "|"))
}
