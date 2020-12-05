# https://adventofcode.com/2020/day/1
from itertools import combinations
from math import prod
import util


def read_file(filename):
    return list(map(int,util.read_file(filename)))


def solve(nums,n):
    combos = combinations(nums,n)
    for c in combos:
        if sum(c) == 2020:
            return prod(c)
    return 0


if __name__ == "__main__":
    day = 1
    inputs = [2,3]
    test_outputs = [514579,241861950]
    util.solve(day,inputs,test_outputs,solve,read_file)