// https://adventofcode.com/2018/day/3
package main

import (
	"fmt"
	"os"
	"slices"
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
	claimed := map[int]map[int]int{}
	for _, line := range lines {
		parts := strings.Split(strings.Split(line, " @ ")[1], ": ")
		margins := strings.Split(parts[0], ",")
		leftMargin, err := strconv.Atoi(margins[0])
		handleError("Failed to parse left margin", err)
		topMargin, err := strconv.Atoi(margins[1])
		handleError("Failed to parse top margin", err)
		claimDimensions := strings.Split(parts[1], "x")
		numCols, err := strconv.Atoi(claimDimensions[0])
		handleError("Failed to parse num cols", err)
		numRows, err := strconv.Atoi(claimDimensions[1])
		handleError("Failed to parse num rows", err)
		for i := 0; i < numRows; i++ {
			for j := 0; j < numCols; j++ {
				_, ok := claimed[topMargin+i]
				if !ok {
					claimed[topMargin+i] = map[int]int{}
				}
				_, ok = claimed[topMargin+i][leftMargin+j]
				if !ok {
					claimed[topMargin+i][leftMargin+j] = 0
				}
				claimed[topMargin+i][leftMargin+j]++
			}
		}
	}
	count := 0
	for _, cols := range claimed {
		for _, numClaimed := range cols {
			if numClaimed > 1 {
				count++
			}
		}
	}
	fmt.Println("2018 day03 part 1 answer:", count)
}

func part2(lines []string) {
	allClaimIds := make([]int, 0)
	claimed := map[int]map[int]map[int]bool{}
	for _, line := range lines {
		parts := strings.Split(line, " @ ")
		claimId, err := strconv.Atoi(parts[0][1:])
		handleError("Failed to parse claim id", err)
		allClaimIds = append(allClaimIds, claimId)
		parts = strings.Split(parts[1], ": ")
		margins := strings.Split(parts[0], ",")
		leftMargin, err := strconv.Atoi(margins[0])
		handleError("Failed to parse left margin", err)
		topMargin, err := strconv.Atoi(margins[1])
		handleError("Failed to parse top margin", err)
		claimDimensions := strings.Split(parts[1], "x")
		numCols, err := strconv.Atoi(claimDimensions[0])
		handleError("Failed to parse num cols", err)
		numRows, err := strconv.Atoi(claimDimensions[1])
		handleError("Failed to parse num rows", err)
		for i := 0; i < numRows; i++ {
			for j := 0; j < numCols; j++ {
				_, ok := claimed[topMargin+i]
				if !ok {
					claimed[topMargin+i] = map[int]map[int]bool{}
				}
				_, ok = claimed[topMargin+i][leftMargin+j]
				if !ok {
					claimed[topMargin+i][leftMargin+j] = map[int]bool{}
				}
				_, ok = claimed[topMargin+i][leftMargin+j][claimId]
				if !ok {
					claimed[topMargin+i][leftMargin+j][claimId] = true
				}
			}
		}
	}
	for _, cols := range claimed {
		for _, claimIds := range cols {
			if len(claimIds) > 1 {
				for claimId, _ := range claimIds {
					index := slices.Index(allClaimIds, claimId)
					if index != -1 {
						allClaimIds = append(allClaimIds[:index], allClaimIds[index+1:]...)
					}
				}
			}
		}
	}
	fmt.Println("2018 day03 part 2 answer:", allClaimIds[0])
}

func main() {
	filename := "../inputs/2018/day03.txt"
	fileBytes, err := os.ReadFile(filename)
	handleError("Failed to read file", err)
	lines := strings.Split(string(fileBytes), "\n")
	part1(lines)
	part2(lines)
}
