# https://adventofcode.com/2020/day/3
from solutions.challenge import Challenge
from math import prod


class Day03(Challenge):
    @staticmethod
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

    @staticmethod
    def solve_part1(input):
        return Day03.solve(input,[(3,1)])

    @staticmethod
    def solve_part2(input):
        return Day03.solve(input,[(1,1),(3,1),(5,1),(7,1),(1,2)])


if __name__ == "__main__":
    Day03().solve_all()
