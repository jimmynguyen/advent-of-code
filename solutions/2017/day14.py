# https://adventofcode.com/2017/day/14
from solutions.challenge import Challenge
from day10 import Day10
from typing import Sequence


class Day14(Challenge):
    @staticmethod
    def build_grid(key: str, n: int=128) -> Sequence[Sequence[int]]:
        num_ones = 0
        grid = []
        for i in range(n):
            hash_hex = Day10.knot_hash(f"{key}-{i}")
            hash_bin = bin(int(hash_hex, 16))[2:].zfill(n)
            row = list(map(int,hash_bin))
            num_ones += sum(row)
            grid.append(row)
        return num_ones, grid

    @staticmethod
    def solve_part1(key: str) -> int:
        return Day14.build_grid(key)[0]

    @staticmethod
    def solve_part2(key: str, n: int=128) -> int:
        num_groups = 0
        grid = Day14.build_grid(key, n)[1]
        coords = [(i,j) for i in range(n) for j in range(n) if grid[i][j] == 1]
        visited = []
        for coord in coords:
            if coord in visited:
                continue
            stack = [coord]
            while len(stack) > 0:
                x = stack.pop()
                if x in visited:
                    continue
                visited.append(x)
                stack += [(x[0] + i, x[1] + j) for i,j in [(0,1),(1,0),(0,-1),(-1,0)] if (x[0] + i >= 0) and (x[1] + j >= 0) and (x[0] + i < n) and (x[1] + j < n) and (grid[x[0]][x[1]], grid[x[0] + i][x[1] + j]) == (1, 1)]
            num_groups += 1
        return num_groups


if __name__ == "__main__":
    Day14().solve_all("hwlqcszp")
