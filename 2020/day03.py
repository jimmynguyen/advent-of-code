# https://adventofcode.com/2020/day/3
from math import prod
import util


def solve(lines,slopes):
    answer = []
    for slope in slopes:
        num_trees = 0
        pos = (0,0)
        h,w = len(lines),len(lines[0])
        while pos[1] + slope[1] < h:
            pos = [sum(x) for x in zip(pos,slope)]
            if lines[pos[1]][pos[0]%w] == "#":
                num_trees += 1
        answer.append(num_trees)
    return prod(answer)


if __name__ == "__main__":
    day = 3
    slopes = [[(3,1)],[(1,1),(3,1),(5,1),(7,1),(1,2)]]
    test_outputs = [7,336]
    util.solve(day,slopes,test_outputs,solve)