# https://adventofcode.com/2015/day/2
from solutions.challenge import Challenge
from itertools import combinations
from math import prod


class Day02(Challenge):
    @staticmethod
    def solve(dimensions,compute_square_feet):
        square_feet = 0
        for dimension in dimensions:
            dimension = sorted(list(map(int,dimension.split("x"))))
            square_feet += compute_square_feet(dimension)
        return square_feet

    @staticmethod
    def solve_part1(input):
        return Day02.solve(input,lambda x: sum([prod(x[:2])] + [prod((2,) + c) for c in combinations(x,2)]))

    @staticmethod
    def solve_part2(input):
        return Day02.solve(input,lambda x: sum([2*sum(x[:2]),prod(x)]))


if __name__ == "__main__":
    Day02().solve_all()
