package main

import (
	"context"
	"os"

	"github.com/fatih/color"
	"github.com/jimmynguyen/advent-of-code/cli/cmd"
)

func main() {
	ctx := context.Background()

	if err := cmd.New().ExecuteContext(ctx); err != nil {
		color.Red("Error: %+v", err)
		os.Exit(1)
	}
}
