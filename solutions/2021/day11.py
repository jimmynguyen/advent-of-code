# https://adventofcode.com/2021/day/11
import sys
from solutions.challenge import Challenge
from itertools import product


class Day11(Challenge):
    def read_file(self, filename):
        return [list(map(int, x)) for x in super().read_file(filename)]

    @staticmethod
    def increment_energy_levels(energy_levels):
        for i in range(len(energy_levels)):
            for j in range(len(energy_levels[0])):
                energy_levels[i][j] += 1

    @staticmethod
    def get_neighbors(row, col, nrows, ncols):
        neighbor_increments = [x for x in product((-1, 0, 1), (-1, 0, 1)) if x[0] != 0 or x[1] != 0]
        return [(row + i, col + j) for i, j in neighbor_increments if row + i >= 0 and row + i < nrows and col + j >= 0 and col + j < ncols]

    @staticmethod
    def flash_energy_levels(energy_levels):
        nrows = len(energy_levels)
        ncols = len(energy_levels[0])
        flashed = set()
        flash_queue = [(i, j) for i in range(nrows) for j in range(ncols) if energy_levels[i][j] > 9]
        while len(flash_queue) > 0:
            octopus = flash_queue.pop(0)
            row, col = octopus
            if octopus not in flashed and energy_levels[row][col] > 9:
                flashed.add(octopus)
                for neighbor_octopus in Day11.get_neighbors(row, col, nrows, ncols):
                    energy_levels[neighbor_octopus[0]][neighbor_octopus[1]] += 1
                    flash_queue.append(neighbor_octopus)
        for row, col in flashed:
            energy_levels[row][col] = 0
        num_flashes = len(flashed)
        return num_flashes, num_flashes == nrows * ncols

    @staticmethod
    def solve(energy_levels, steps):
        total_num_flashes = 0
        for i in range(steps):
            Day11.increment_energy_levels(energy_levels)
            num_flashes, all_flashed = Day11.flash_energy_levels(energy_levels)
            if all_flashed:
                return i + 1
            total_num_flashes += num_flashes
        return total_num_flashes

    @staticmethod
    def solve_part1(input):
        return Day11.solve(input, 100)

    @staticmethod
    def solve_part2(input):
        return Day11.solve(input, sys.maxsize)


if __name__ == "__main__":
    Day11().solve_all()
