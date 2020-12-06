# https://adventofcode.com/2015/day/2
from itertools import combinations
from math import prod
import util


def solve(dimensions,compute_square_feet):
    square_feet = 0
    for dimension in dimensions:
        dimension = sorted(list(map(int,dimension.split("x"))))
        square_feet += compute_square_feet(dimension)
    return square_feet


if __name__ == "__main__":
    day = 2
    inputs = [
        lambda x: sum([prod(x[:2])] + [prod((2,) + c) for c in combinations(x,2)]),
        lambda x: sum([2*sum(x[:2]),prod(x)])
    ]
    test_outputs = [101,48]
    util.solve(day,inputs,test_outputs,solve)