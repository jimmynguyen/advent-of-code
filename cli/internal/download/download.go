package download

import (
	"context"
	"fmt"
	"io"
	"net/http"
	"os"
	"strings"

	"github.com/go-faster/errors"
	"github.com/jimmynguyen/advent-of-code/cli/internal/consts"
	"github.com/spf13/viper"
)

func Run(
	ctx context.Context,
	year int,
	day int,
	filePath string,
) error {
	url := fmt.Sprintf("%s/%d/day/%d/input", consts.AdventOfCodeURL, year, day)
	request, err := http.NewRequestWithContext(ctx, http.MethodGet, url, nil)
	if err != nil {
		return errors.Wrapf(err, "failed to build request: url=%s", url)
	}

	request.AddCookie(&http.Cookie{
		Name:     "session",
		Value:    viper.GetString(consts.FlagSessionCookie),
		Domain:   ".adventofcode.com",
		Path:     "/",
		HttpOnly: true,
		Secure:   true,
	})

	client := &http.Client{}

	response, err := client.Do(request)
	if err != nil {
		return errors.Wrapf(err, "failed to download input: url=%s", url)
	}
	defer response.Body.Close()

	body, err := io.ReadAll(response.Body)
	if err != nil {
		return errors.Wrapf(err, "failed to read response body: url=%s", url)
	}

	if response.StatusCode != http.StatusOK {
		return errors.Errorf("failed to download input: status=%d, url=%s, response=%v", response.StatusCode, url, response)
	}

	err = os.WriteFile(filePath, []byte(strings.TrimSpace(string(body))), 0644)
	if err != nil {
		return errors.Wrapf(err, "failed to write response body to file: filePath=%s", filePath)
	}

	fmt.Printf("Successfully downloaded input for year=%d, day=%d to %s\n", year, day, filePath)

	return nil
}
