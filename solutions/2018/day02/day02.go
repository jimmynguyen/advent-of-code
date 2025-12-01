// https://adventofcode.com/2018/day/2
package main

import (
	"fmt"
	"os"
	"strings"
)

func handleError(
	message string,
	err error,
) {
	if err != nil {
		panic(fmt.Sprintf(message+": %v", err))
	}
}

func part1(lines []string) {
	count2, count3 := 0, 0
	for _, line := range lines {
		runeCount := map[rune]int{}
		for _, letter := range line {
			_, ok := runeCount[letter]
			if !ok {
				runeCount[letter] = 1
			} else {
				runeCount[letter] += 1
			}
		}

		has2, has3 := false, false
		for _, count := range runeCount {
			if !has2 && count == 2 {
				has2 = true
			}
			if !has3 && count == 3 {
				has3 = true
			}
			if has2 && has3 {
				break
			}
		}

		if has2 {
			count2++
		}
		if has3 {
			count3++
		}
	}
	result := count2 * count3
	fmt.Println("2018 day02 part 1 answer:", result)
}

func part2(lines []string) {
	possible := map[string]bool{}
	for _, line := range lines {
		linePossible := map[string]bool{}
		for i := 0; i < len(line); i++ {
			key := line[:i] + line[i+1:]
			linePossible[key] = true
		}
		for key, _ := range linePossible {
			_, ok := possible[key]
			if ok {
				fmt.Println("2018 day02 part 2 answer:", key)
				return
			}
			possible[key] = true
		}
	}
}

func main() {
	filename := "../inputs/2018/day02.txt"
	fileBytes, err := os.ReadFile(filename)
	handleError("Failed to read file", err)
	lines := strings.Split(string(fileBytes), "\n")
	part1(lines)
	part2(lines)
}
