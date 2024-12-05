// https://adventofcode.com/2018/day/6
package main

import (
	"fmt"
	"math"
	"os"
	"sort"
	"strconv"
	"strings"
	"sync"
)

const DEBUG = false

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

func parseCoordsAndGridSize(lines []string) ([][]int, int, int) {
	coords := make([][]int, 0, len(lines))
	for _, line := range lines {
		parts := strings.Split(line, ", ")
		x, err := strconv.Atoi(parts[0])
		handleError("Failed to parse x", err)
		y, err := strconv.Atoi(parts[1])
		handleError("Failed to parse y", err)
		coords = append(coords, []int{x, y})
	}

	xMax, yMax := coords[0][0], coords[0][1]
	sort.Slice(coords, func(x, y int) bool {
		xMax = max(xMax, coords[x][0], coords[y][0])
		yMax = max(yMax, coords[x][1], coords[y][1])
		if coords[x][0] == coords[y][0] {
			return coords[x][1] < coords[y][1]
		}
		return coords[x][0] < coords[y][0]
	})

	return coords, xMax + 1, yMax + 1
}

func initializeGrid(coords [][]int, xMax int) map[int]map[int]int {
	grid := map[int]map[int]int{}
	for x := 0; x < xMax; x++ {
		grid[x] = map[int]int{}
	}
	for id, coord := range coords {
		x, y := coord[0], coord[1]
		grid[x][y] = id
	}
	return grid
}

func printGrid(grid map[int]map[int]int, xMax int, yMax int) {
	if !DEBUG {
		return
	}
	for y := 0; y < yMax; y++ {
		rowString := ""
		for x := 0; x < xMax; x++ {
			if val, ok := grid[x][y]; !ok || val == -1 {
				rowString += ". "
			} else {
				rowString += string(rune('a'+grid[x][y])) + " "
			}
		}
		fmt.Println(rowString)
	}
	fmt.Println("=================")
}

func manhattanDistance(x1 int, y1 int, x2 int, y2 int) int {
	return int(math.Abs(float64(x1-x2)) + math.Abs(float64(y1-y2)))
}

func isFinite(grid map[int]map[int]int, xMax int, yMax int, x int, y int, id int) bool {
	// top
	finite := false
	for _x := x - 1; _x >= 0; _x-- {
		if grid[_x][y] == -1 || grid[_x][y] != id {
			finite = true
			break
		}
	}
	if !finite {
		return false
	}

	// bottom
	finite = false
	for _x := x + 1; _x < xMax; _x++ {
		if grid[_x][y] == -1 || grid[_x][y] != id {
			finite = true
			break
		}
	}
	if !finite {
		return false
	}

	// left
	finite = false
	for _y := y - 1; _y >= 0; _y-- {
		if grid[x][_y] == -1 || grid[x][_y] != id {
			finite = true
			break
		}
	}
	if !finite {
		return false
	}

	// right
	finite = false
	for _y := y + 1; _y < yMax; _y++ {
		if grid[x][_y] == -1 || grid[x][_y] != id {
			finite = true
			break
		}
	}
	return finite
}

func area(grid map[int]map[int]int, xMax int, yMax int, id int) int {
	area := 0
	for x := 0; x < xMax; x++ {
		for y := 0; y < yMax; y++ {
			if id == grid[x][y] {
				if !isFinite(grid, xMax, yMax, x, y, id) {
					return 0
				}
				area += 1
			}
		}
	}
	return area
}

func areaWithinThreshold(xMax int, yMax int, coords [][]int, totalDistanceThreshold int) int {
	area := 0
	for x1 := 0; x1 < xMax; x1++ {
		for y1 := 0; y1 < yMax; y1++ {
			totalDistance := 0
			for _, coord := range coords {
				x2, y2 := coord[0], coord[1]
				distance := manhattanDistance(x1, y1, x2, y2)
				totalDistance += distance
			}
			if totalDistance < totalDistanceThreshold {
				area += 1
			}
		}
	}
	return area
}

func populateGrid(grid map[int]map[int]int, xMax int, yMax int, coords [][]int) {
	for x1 := 0; x1 < xMax; x1++ {
		for y1 := 0; y1 < yMax; y1++ {
			minDistance := math.MaxInt
			for _, coord := range coords {
				x2, y2 := coord[0], coord[1]
				minDistance = min(minDistance, manhattanDistance(x1, y1, x2, y2))
			}

			for id, coord := range coords {
				x2, y2 := coord[0], coord[1]
				if manhattanDistance(x1, y1, x2, y2) == minDistance {
					if val, ok := grid[x1][y1]; !ok {
						grid[x1][y1] = id
					} else if val != id {
						grid[x1][y1] = -1
					}
				}
			}
		}
	}
}

func part1(lines []string) int {
	coords, xMax, yMax := parseCoordsAndGridSize(lines)
	grid := initializeGrid(coords, xMax)
	printGrid(grid, xMax, yMax)
	populateGrid(grid, xMax, yMax, coords)
	printGrid(grid, xMax, yMax)

	maxArea := math.MinInt
	for id := range coords {
		idArea := area(grid, xMax, yMax, id)
		maxArea = max(maxArea, idArea)
	}

	fmt.Println("Part 1 result:", maxArea)
	return maxArea
}

func part2(lines []string, totalDistanceThreshold int) int {
	coords, xMax, yMax := parseCoordsAndGridSize(lines)
	grid := initializeGrid(coords, xMax)
	printGrid(grid, xMax, yMax)
	populateGrid(grid, xMax, yMax, coords)
	printGrid(grid, xMax, yMax)

	totalArea := areaWithinThreshold(xMax, yMax, coords, totalDistanceThreshold)

	fmt.Println("Part 2 result:", totalArea)
	return totalArea
}

func main() {
	lines := readFile("day06.txt")

	waitGroup := &sync.WaitGroup{}
	waitGroup.Add(1)
	go func() {
		defer waitGroup.Done()
		part1(lines)
	}()
	if DEBUG {
		waitGroup.Wait()
	}
	waitGroup.Add(1)
	go func() {
		defer waitGroup.Done()
		part2(lines, 10000)
	}()
	waitGroup.Wait()
}
