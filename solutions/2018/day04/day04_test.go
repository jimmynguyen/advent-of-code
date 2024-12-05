package main

import (
	"testing"
)

func TestPart1(t *testing.T) {
	lines := readFile("day04.test.txt")

	expected := 240
	actual := part1(lines)
	if expected != actual {
		t.Fatalf("Expected %v but was %v", expected, actual)
	}
}

func TestPart2(t *testing.T) {
	lines := readFile("day04.test.txt")

	expected := 4455
	actual := part2(lines)
	if expected != actual {
		t.Fatalf("Expected %v but was %v", expected, actual)
	}
}
