package cmd

import (
	"fmt"
	"github.com/spf13/cobra"
	"maya-stubgen/stubgen/cmds"
)

// cmdsCmd represents the cmds command
var cmdsCmd = &cobra.Command{
	Use:   "cmds",
	Short: "A brief description of your command",
	Long: `A longer description that spans multiple lines and likely contains examples
and usage of using your command. For example:

Cobra is a CLI library for Go that empowers applications.
This application is a tool to generate the needed files
to quickly create a Cobra application.`,
	Run: func(cmd *cobra.Command, args []string) {

		outPath, err := cmd.Flags().GetString("out")
		if err != nil {
			fmt.Errorf("Could not read out path: %s", err)
		}
		cachePath, err := cmd.Flags().GetString("cache")

		if err != nil {
			fmt.Errorf("Could not read out path: %s", err)
		}

		cmds.Run(outPath, cachePath)
	},
}

func init() {
	buildCmd.AddCommand(cmdsCmd)
}
