// https://adventofcode.com/2018/day/5
package main

import (
	"fmt"
	"os"
	"sort"
	"strings"
	"sync"
	"unicode"
)

func readFile(filename string) []string {
	fileBytes, err := os.ReadFile(filename)
	handleError("Failed to read file", err)
	lines := strings.Split(string(fileBytes), "\n")
	sort.Strings(lines)
	return lines
}

func handleError(
	message string,
	err error,
) {
	if err != nil {
		panic(fmt.Sprintf(message+": %v", err))
	}
}

func react(line string) int {
	var out string
	for true {
		out = ""
		for i := 0; i < len(line); i++ {
			if i+1 < len(line) && (unicode.IsUpper(rune(line[i])) && unicode.IsLower(rune(line[i+1])) && line[i] == byte(unicode.ToUpper(rune(line[i+1]))) || unicode.IsUpper(rune(line[i+1])) && unicode.IsLower(rune(line[i])) && line[i+1] == byte(unicode.ToUpper(rune(line[i])))) {
				i += 1
			} else {
				out += string(line[i])
			}
		}
		if out == line {
			break
		}
		line = out
	}
	return len(out)
}

func part1(lines []string) int {
	line := lines[0]
	result := react(line)
	fmt.Println("Part 1 result:", result)
	return result
}

func part2(lines []string) int {
	line := lines[0]

	units := map[rune]bool{}
	for _, unit := range line {
		unit = unicode.ToLower(unit)
		units[unit] = true
	}

	result := len(line)
	waitGroup := &sync.WaitGroup{}
	for unit := range units {
		waitGroup.Add(1)
		go func(unit rune) {
			defer waitGroup.Done()
			strippedLine := strings.ReplaceAll(strings.ReplaceAll(line, string(unit), ""), string(unicode.ToUpper(unit)), "")
			result = min(result, react(strippedLine))
		}(unit)
	}
	waitGroup.Wait()

	fmt.Println("Part 2 result:", result)
	return result
}

func main() {
	lines := readFile("day05.txt")

	waitGroup := &sync.WaitGroup{}
	waitGroup.Add(1)
	go func() {
		defer waitGroup.Done()
		part1(lines)
	}()
	waitGroup.Add(1)
	go func() {
		defer waitGroup.Done()
		part2(lines)
	}()
	waitGroup.Wait()
}
