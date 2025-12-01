// https://adventofcode.com/2018/day/1
package main

import (
	"fmt"
	"os"
	"strconv"
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
	result := 0
	for _, line := range lines {
		num, err := strconv.Atoi(line[1:])
		handleError("Failed to convert string to number", err)
		if line[0] == '+' {
			result += num
		} else {
			result -= num
		}
	}
	fmt.Println("2018 day01 part 1 answer:", result)
}

func part2(lines []string) {
	visited := map[int]bool{0: true}
	result := 0
	for true {
		for _, line := range lines {
			num, err := strconv.Atoi(line[1:])
			handleError("Failed to convert string to number", err)
			if line[0] == '+' {
				result += num
			} else {
				result -= num
			}
			_, ok := visited[result]
			if ok {
				fmt.Println("2018 day01 part 2 answer:", result)
				return
			}
			visited[result] = true
		}
	}
}

func main() {
	filename := "../inputs/2018/day01.txt"
	fileBytes, err := os.ReadFile(filename)
	handleError("Failed to read file", err)
	lines := strings.Split(string(fileBytes), "\n")
	part1(lines)
	part2(lines)
}
