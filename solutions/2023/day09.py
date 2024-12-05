# https://adventofcode.com/2023/day/9
import math
from typing import Dict, List, Tuple
from challenge import Challenge


ParsedChallengeInput = List[List[int]]


class Day09(Challenge):
    def read_file(self, filename: str) -> ParsedChallengeInput:
        return [list(map(int, line.split())) for line in super().read_file(filename)]

    @staticmethod
    def solve_part1(input: ParsedChallengeInput) -> int:
        result = 0
        for numbers in input:
            levels = [numbers]
            while not all(number == 0 for number in levels[-1]):
                levels.append([b - a for a, b in zip(levels[-1][:-1], levels[-1][1:])])
            next_value = 0
            for level in levels[::-1]:
                next_value += level[-1]
            result += next_value
        return result

    @staticmethod
    def solve_part2(input: ParsedChallengeInput) -> int:
        result = 0
        for numbers in input:
            levels = [numbers]
            while not all(number == 0 for number in levels[-1]):
                levels.append([b - a for a, b in zip(levels[-1][:-1], levels[-1][1:])])
            next_value = 0
            for level in levels[::-1]:
                next_value = level[0] - next_value
            result += next_value
        return result


if __name__ == "__main__":
    Day09().solve_all()
