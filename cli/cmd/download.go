package cmd

import (
	"time"

	"github.com/go-faster/errors"
	"github.com/jimmynguyen/advent-of-code/cli/internal/consts"
	"github.com/jimmynguyen/advent-of-code/cli/internal/download"
	"github.com/spf13/cobra"
	"github.com/spf13/viper"
)

func NewDownload() *cobra.Command {
	currentYear := time.Now().Year()

	cmd := &cobra.Command{
		Use:     "download",
		Aliases: []string{"dl"},
		Short:   "Download inputs from https://adventofcode.com/{year}/day/{day}/inputs",
		RunE: func(cmd *cobra.Command, args []string) error {
			year := viper.GetInt(consts.FlagYear)
			if year < 2015 || year > currentYear {
				return errors.Errorf("invalid --year=%d. Valid range: [2015, %d]", year, currentYear)
			}

			day := viper.GetInt(consts.FlagDay)
			if day < 1 || day > 25 {
				return errors.Errorf("invalid --day=%d. Valid range: [1, 25]", day)
			}

			filePath := viper.GetString(consts.FlagFilePath)
			if filePath == "" {
				return errors.Errorf("invalid --file-path=%s", filePath)
			}

			return download.Run(cmd.Context(), year, day, filePath)
		},
	}

	defaultDay := 0
	if time.Now().Month() == 12 {
		defaultDay = time.Now().Day()
	}

	cmd.Flags().IntP(consts.FlagYear, "y", currentYear, "year")
	cmd.Flags().IntP(consts.FlagDay, "d", defaultDay, "day")
	cmd.Flags().StringP(consts.FlagFilePath, "p", "", "input file path")
	cmd.MarkFlagRequired(consts.FlagFilePath)

	viper.BindPFlags(cmd.Flags())

	return cmd
}
