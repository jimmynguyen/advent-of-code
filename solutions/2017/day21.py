# https://adventofcode.com/2017/day/21
from typing import List
from solutions.challenge import Challenge

class Pattern(object):
    def __init__(self, pattern) -> None:
        self.pattern = pattern
        self.pattern_grid = pattern.split("/")
        self.size = len(self.pattern_grid)


class Rule(object):
    def __init__(self, rule: str):
        self.input_pattern, self.output_pattern = rule.split(" => ")
        self.input_size = len(self.input_pattern)
        self.output_size = len(self.output_pattern)
        self._build_input_patterns(self.input_pattern.split("/"))

    def _build_input_patterns(self, pattern):
        patterns = [
            pattern,
            self._flip_horizontally(pattern),
            self._flip_vertically(pattern),
        ]
        for pattern in list(patterns):
            for _ in range(3):
                pattern = self._rotate_clockwise_90(pattern)
                patterns.append(["".join(row) for row in pattern])
        self.input_patterns = set("/".join(pattern) for pattern in patterns)

    def _rotate_clockwise_90(self, pattern):
        return list(zip(*pattern[::-1]))

    def _flip_vertically(self, pattern):
        return pattern[::-1]

    def _flip_horizontally(self, pattern):
        return [row[::-1] for row in pattern]

    def is_match(self, pattern):
        return pattern in self.input_patterns

    def __str__(self) -> str:
        return f"{self.input_pattern} => {self.output_pattern}"


class Day21(Challenge):
    def read_file(self, filename: str) -> List[Rule]:
        return list(map(Rule, super().read_file(filename)))

    @staticmethod
    def enhance(pattern: str, rules: List[Rule]):
        pattern = pattern.split("/")
        size = len(pattern)
        block_size = 2 if size % 2 == 0 else 3
        block_array = []
        for idx_row in range(0, size, block_size):
            block_row = []
            for idx_col in range(0, size, block_size):
                block_row.append([x[idx_col:idx_col + block_size] for x in pattern[idx_row:idx_row + block_size]])
            block_array.append(block_row)
        enhanced_block_array = []
        for block_row in block_array:
            enhanced_block_row = []
            for block in block_row:
                block_pattern = "/".join("".join(block_pattern_row) for block_pattern_row in block)
                for rule in rules:
                    if rule.is_match(block_pattern):
                        enhanced_block_row.append(rule.output_pattern.split("/"))
                        break
            enhanced_block_array.append(enhanced_block_row)
        enhanced_pattern = []
        for enhanced_block_row in enhanced_block_array:
            enhanced_pattern_row = []
            for enhanced_block in enhanced_block_row:
                if len(enhanced_pattern_row) == 0:
                    enhanced_pattern_row = enhanced_block
                else:
                    for idx_row, x in enumerate(enhanced_block):
                        enhanced_pattern_row[idx_row] += x
            enhanced_pattern.extend(enhanced_pattern_row)
        return "/".join(enhanced_pattern)


    @staticmethod
    def solve(rules: List[Rule], num_iterations: int) -> int:
        pattern = ".#./..#/###"
        for _ in range(num_iterations):
            pattern = Day21.enhance(pattern, rules)
        return pattern.count("#")


    @staticmethod
    def solve_part1(rules: List[Rule]) -> int:
        return Day21.solve(rules, num_iterations=5)

    @staticmethod
    def solve_part2(rules: List[Rule]) -> int:
        return Day21.solve(rules, num_iterations=18)


if __name__ == "__main__":
    Day21().solve_all()
