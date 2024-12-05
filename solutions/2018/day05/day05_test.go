package main

import (
	"testing"
)

func TestPart1(t *testing.T) {
	lines := readFile("day05.test.txt")

	expected := 10
	actual := part1(lines)
	if expected != actual {
		t.Fatalf("Expected %v but was %v", expected, actual)
	}
}

func TestPart2(t *testing.T) {
	lines := readFile("day05.test.txt")

	expected := 4
	actual := part2(lines)
	if expected != actual {
		t.Fatalf("Expected %v but was %v", expected, actual)
	}
}
