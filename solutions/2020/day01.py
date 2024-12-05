# https://adventofcode.com/2020/day/1
from solutions.challenge import Challenge
from itertools import combinations
from math import prod


class Day01(Challenge):
    def read_file(self,filename):
        return list(map(int,super().read_file(filename)))

    @staticmethod
    def solve(nums,n):
        combos = combinations(nums,n)
        for c in combos:
            if sum(c) == 2020:
                return prod(c)
        return 0

    @staticmethod
    def solve_part1(input):
        return Day01.solve(input,2)

    @staticmethod
    def solve_part2(input):
        return Day01.solve(input,3)


if __name__ == "__main__":
    Day01().solve_all()
