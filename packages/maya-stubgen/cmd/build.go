package cmd

import (
	"fmt"

	"github.com/spf13/cobra"
)

var outPath string
var cachePath string

// buildCmd represents the build command
var buildCmd = &cobra.Command{
	Use:   "build",
	Short: "A brief description of your command",
	Long: `A longer description that spans multiple lines and likely contains examples
and usage of using your command. For example:

Cobra is a CLI library for Go that empowers applications.
This application is a tool to generate the needed files
to quickly create a Cobra application.`,
	PersistentPreRunE: func(cmd *cobra.Command, args []string) error {
		if outPath == "" {
			return fmt.Errorf("--out is required")
		}
		return nil
	},
	Run: func(cmd *cobra.Command, args []string) {
		fmt.Println("build called")
	},
}

func init() {
	rootCmd.AddCommand(buildCmd)

	// Here you will define your flags and configuration settings.
	buildCmd.PersistentFlags().StringVarP(&outPath, "out", "o", "src", "output directory for the stubs.")
	buildCmd.PersistentFlags().StringVarP(&outPath, "cache", "c", ".cache", "output directory for the stubs.")

	// Cobra supports Persistent Flags which will work for this command
	// and all subcommands, e.g.:
	// buildCmd.PersistentFlags().String("foo", "", "A help for foo")

	// Cobra supports local flags which will only run when this command
	// is called directly, e.g.:
	// buildCmd.Flags().BoolP("toggle", "t", false, "Help message for toggle")
}
