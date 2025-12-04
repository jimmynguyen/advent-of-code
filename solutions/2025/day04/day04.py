# https://adventofcode.com/2025/day/4
from solutions.challenge import Challenge
import numpy as np
from scipy.signal import convolve2d


ParsedChallengeInput = np.ndarray


class Day04(Challenge):
    def read_file(self,filename) -> ParsedChallengeInput:
        lines = super().read_file(filename, delimiter="\n")
        nrows = len(lines)
        ncols = len(lines[0])
        grid = np.zeros(shape=(nrows,ncols), dtype=int)
        for y, line in enumerate(lines):
            for x, character in enumerate(line):
                grid[y,x] = 1 if character == "@" else 0
        return grid


    @staticmethod
    def solve_part1(
        parsed_input: ParsedChallengeInput,
        part2: bool = False,
    ):
        grid = parsed_input
        total_accessible_count = 0
        while True:
            neighbor_sum = convolve2d(grid, np.ones((3,3), dtype=int), "same") - grid
            accessible_count = np.sum(neighbor_sum[grid == 1] < 4)
            if not part2:
                return accessible_count
            if accessible_count == 0:
                break
            total_accessible_count += accessible_count
            grid[np.logical_and(grid == 1, neighbor_sum < 4)] = 0
        return total_accessible_count


    @staticmethod
    def solve_part2(
        parsed_input: ParsedChallengeInput,
    ):
        return Day04.solve_part1(parsed_input, part2=True)


if __name__ == "__main__":
    Day04().solve_all()
