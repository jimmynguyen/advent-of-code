# https://adventofcode.com/2022/day/8
from solutions.challenge import Challenge
import numpy as np

class Day08(Challenge):
    def read_file(self, filename: str) -> np.ndarray:
        lines = super().read_file(filename)
        num_rows = len(lines)
        num_cols = len(lines[0])
        grid = np.zeros((num_rows, num_cols))
        for idx_row in range(num_rows):
            for idx_col in range(num_cols):
                grid[idx_row, idx_col] = int(lines[idx_row][idx_col])
        return grid

    @staticmethod
    def solve_part1(grid: np.ndarray) -> int:
        visible = np.zeros_like(grid, dtype=bool)
        visible[[0, -1], :] = True
        visible[:, [0, -1]] = True
        for idx_row in range(1, grid.shape[0] - 1):
            for idx_col in range(1, grid.shape[1] - 1):
                visible[idx_row, idx_col] = np.all(grid[:idx_row, idx_col] < grid[idx_row, idx_col]) \
                    or np.all(grid[idx_row+1:, idx_col] < grid[idx_row, idx_col]) \
                    or np.all(grid[idx_row, :idx_col] < grid[idx_row, idx_col]) \
                    or np.all(grid[idx_row, idx_col+1:] < grid[idx_row, idx_col])
        return np.sum(visible)

    @staticmethod
    def compute_dist(array: np.ndarray, value: float):
        return np.size(array) if np.all(array < value) else np.argmax(array >= value) + 1

    @staticmethod
    def solve_part2(grid: np.ndarray) -> int:
        dist = np.zeros_like(grid)
        for idx_row in range(1, grid.shape[0] - 1):
            for idx_col in range(1, grid.shape[1] - 1):
                top_dist = Day08.compute_dist(grid[idx_row-1::-1, idx_col], grid[idx_row, idx_col])
                bot_dist = Day08.compute_dist(grid[idx_row+1:, idx_col], grid[idx_row, idx_col])
                left_dist = Day08.compute_dist(grid[idx_row, idx_col-1::-1], grid[idx_row, idx_col])
                rite_dist = Day08.compute_dist(grid[idx_row, idx_col+1:], grid[idx_row, idx_col])
                dist[idx_row, idx_col] = top_dist * bot_dist * left_dist * rite_dist
        return int(np.max(dist))

if __name__ == "__main__":
    Day08().solve_all()
