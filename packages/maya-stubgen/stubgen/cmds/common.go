package cmds

type MayaCmd struct {
	Name                string `json:"name"`
	PositionalArguments []Flag `json:"positional_arguments"`
	KeywordArguments    []Flag `json:"keyword_arguments"`
	ReturnType          string `json:"return_type"`
}

type Flag struct {
	Name  string   `json:"name"`
	Type  string   `json:"type"`
	modes []string `json:"modes"`
	Value string   `json:"value"`
}
