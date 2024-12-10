package cmd

import (
	"strings"

	"github.com/jimmynguyen/advent-of-code/cli/internal/consts"
	"github.com/spf13/cobra"
	"github.com/spf13/viper"
)

func New() *cobra.Command {
	cmd := &cobra.Command{
		Use:           "aoc",
		Short:         "Advent of Code CLI",
		SilenceErrors: false,
		SilenceUsage:  false,
	}

	cmd.AddCommand(NewDownload())

	cmd.PersistentFlags().StringP(consts.FlagSessionCookie, "s", "", "session cookie")
	cmd.MarkPersistentFlagRequired(consts.FlagSessionCookie)

	viper.BindPFlags(cmd.PersistentFlags())
	viper.SetEnvPrefix("aoc")
	viper.SetEnvKeyReplacer(strings.NewReplacer("-", "_"))
	viper.AutomaticEnv()

	return cmd
}
