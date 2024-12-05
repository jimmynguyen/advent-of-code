# https://adventofcode.com/2021/day/9
from solutions.challenge import Challenge
from math import prod


class Day09(Challenge):
    def read_file(self, filename):
        return [list(map(int, x)) for x in super().read_file(filename)]

    @staticmethod
    def get_neighbors(heightmap, row, col):
        nrows, ncols = len(heightmap), len(heightmap[0])
        return [(row + i, col + j) for i, j in [(0, -1), (0, 1), (-1, 0), (1, 0)] if row + i >= 0 and row + i < nrows and col + j >= 0 and col + j < ncols]

    @staticmethod
    def get_neighbor_heights(heightmap, row, col):
        return [heightmap[i][j] for i, j in Day09.get_neighbors(heightmap, row, col)]

    @staticmethod
    def get_low_points(heightmap):
        return [(row, col) \
            for row in range(len(heightmap)) \
            for col in range(len(heightmap[0])) \
            if all(heightmap[row][col] < neighbor_height \
                for neighbor_height in Day09.get_neighbor_heights(heightmap, row, col))]

    @staticmethod
    def compute_risk_level(heightmap):
        return sum(1 + heightmap[row][col] for row, col in Day09.get_low_points(heightmap))

    @staticmethod
    def find_three_largest_basins(heightmap):
        low_points = Day09.get_low_points(heightmap)
        visited = set()
        stack = [(x, x) for x in low_points]
        basin_sizes = {x: 0 for x in low_points}
        while len(stack) > 0:
            node, src = stack.pop()
            if node not in visited:
                visited.add(node)
                basin_sizes[src] += 1
                stack += [(x, src) for x in Day09.get_neighbors(heightmap, node[0], node[1]) if heightmap[x[0]][x[1]] > heightmap[node[0]][node[1]] and heightmap[x[0]][x[1]] < 9]
        return prod(sorted(basin_sizes.values(), reverse = True)[:3])

    @staticmethod
    def solve_part1(input):
        return Day09.compute_risk_level(input)

    @staticmethod
    def solve_part2(input):
        return Day09.find_three_largest_basins(input)


if __name__ == "__main__":
    Day09().solve_all()
