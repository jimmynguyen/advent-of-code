// https://adventofcode.com/2018/day/4
package main

import (
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
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

func part1(lines []string) int {
	guardToMinutesAsleep := map[int]int{}
	guardToMinuteToCount := map[int]map[int]int{}
	var guard int
	var sleepStartMinute int
	var err error
	for _, line := range lines {
		if strings.Contains(line, "Guard #") {
			guard, err = strconv.Atoi(strings.Split(strings.Split(line, "Guard #")[1], " ")[0])
			handleError("Failed to parse guard", err)
			if _, ok := guardToMinuteToCount[guard]; !ok {
				guardToMinuteToCount[guard] = map[int]int{}
			}
		} else if strings.HasSuffix(line, "falls asleep") {
			sleepStartMinute, err = strconv.Atoi(strings.Split(strings.Split(line, ":")[1], "]")[0])
			handleError("Failed to sleep start", err)
		} else if strings.HasSuffix(line, "wakes up") {
			sleepEndMinute, err := strconv.Atoi(strings.Split(strings.Split(line, ":")[1], "]")[0])
			handleError("Failed to sleep end", err)
			guardToMinutesAsleep[guard] += sleepEndMinute - sleepStartMinute
			for minute := sleepStartMinute; minute < sleepEndMinute; minute++ {
				guardToMinuteToCount[guard][minute]++
			}
		}
	}
	maxGuard := -1
	maxMinutesAsleep := -1
	for guard, minutesAsleep := range guardToMinutesAsleep {
		if maxMinutesAsleep < minutesAsleep {
			maxMinutesAsleep = minutesAsleep
			maxGuard = guard
		}
	}
	maxMinute := -1
	maxCount := -1
	for minute, count := range guardToMinuteToCount[maxGuard] {
		if maxCount < count {
			maxCount = count
			maxMinute = minute
		}
	}
	result := maxGuard * maxMinute
	fmt.Println("2018 day04 part 1 answer:", result)
	return result
}

func part2(lines []string) int {
	guardToMinutesAsleep := map[int]int{}
	guardToMinuteToCount := map[int]map[int]int{}
	var guard int
	var sleepStartMinute int
	var err error
	for _, line := range lines {
		if strings.Contains(line, "Guard #") {
			guard, err = strconv.Atoi(strings.Split(strings.Split(line, "Guard #")[1], " ")[0])
			handleError("Failed to parse guard", err)
			if _, ok := guardToMinuteToCount[guard]; !ok {
				guardToMinuteToCount[guard] = map[int]int{}
			}
		} else if strings.HasSuffix(line, "falls asleep") {
			sleepStartMinute, err = strconv.Atoi(strings.Split(strings.Split(line, ":")[1], "]")[0])
			handleError("Failed to sleep start", err)
		} else if strings.HasSuffix(line, "wakes up") {
			sleepEndMinute, err := strconv.Atoi(strings.Split(strings.Split(line, ":")[1], "]")[0])
			handleError("Failed to sleep end", err)
			guardToMinutesAsleep[guard] += sleepEndMinute - sleepStartMinute
			for minute := sleepStartMinute; minute < sleepEndMinute; minute++ {
				guardToMinuteToCount[guard][minute]++
			}
		}
	}
	maxGuard := -1
	maxMinute := -1
	maxCount := -1
	for guard, minuteToCount := range guardToMinuteToCount {
		for minute, count := range minuteToCount {
			if maxCount < count {
				maxCount = count
				maxMinute = minute
				maxGuard = guard
			}
		}
	}
	result := maxGuard * maxMinute
	fmt.Println("2018 day04 part 2 answer:", result)
	return result
}

func main() {
	lines := readFile("../inputs/2018/day04.txt")

	part1(lines)
	part2(lines)
}
