package utils

import (
	"slices"
	"strings"
)

type MayaCmdInfo struct {
	Cmd            *MayaCmd
	ReturnTypeList []string
	HasEditFlags   bool
	HasQueryFlags  bool
}

type MayaCmd struct {
	Name                string `json:"name"`
	PositionalArguments []Flag `json:"positional_arguments"`
	KeywordArguments    []Flag `json:"keyword_arguments"`
	ReturnType          string `json:"return_type"`
}

type Flag struct {
	Name  string `json:"name"`
	Type  string `json:"type"`
	Value string `json:"value"`
}

func (cmdInfo *MayaCmdInfo) ResolveQueryAndEdit() {
	var cmd *MayaCmd = cmdInfo.Cmd

	// Add edit and query keyword arguments accordingly
	if cmdInfo.HasQueryFlags {
		queryFlag := Flag{Name: "query", Type: "bool", Value: "..."}
		cmd.KeywordArguments = slices.Insert(cmd.KeywordArguments, 0, queryFlag)
	}
	if cmdInfo.HasEditFlags {
		editFlag := Flag{Name: "edit", Type: "bool", Value: "..."}
		cmd.KeywordArguments = slices.Insert(cmd.KeywordArguments, 0, editFlag)
	}
}

func (cmdInfo *MayaCmdInfo) ResolveReturnTypes() {
	var cmd *MayaCmd = cmdInfo.Cmd

	slices.Sort(cmdInfo.ReturnTypeList)
	cmdInfo.ReturnTypeList = slices.Compact(cmdInfo.ReturnTypeList)

	// Convert individual return types to python to avoid duplicates (e.g.: name, string => str, str)
	pyList := []string{}
	for _, typ := range cmdInfo.ReturnTypeList {
		pyList = append(pyList, MelTypeToPython(typ))
	}
	slices.Sort(pyList)
	pyList = slices.Compact(pyList)

	// Final clean conversion without duplicates
	cmd.ReturnType = MelTypeToPython(strings.Join(pyList, "|"))
}
