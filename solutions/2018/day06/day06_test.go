package main

import (
	"testing"
)

func TestPart1(t *testing.T) {
	lines := readFile("day06.test.txt")

	expected := 17
	actual := part1(lines)
	if expected != actual {
		t.Fatalf("Expected %v but was %v", expected, actual)
	}
}

func TestPart2(t *testing.T) {
	lines := readFile("day06.test.txt")

	expected := 16
	actual := part2(lines, 32)
	if expected != actual {
		t.Fatalf("Expected %v but was %v", expected, actual)
	}
}
