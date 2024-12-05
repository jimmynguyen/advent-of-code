# https://adventofcode.com/2015/day/1
from solutions.challenge import Challenge


class Day01(Challenge):
    @staticmethod
    def solve_part1(input):
        return input.count("(") - input.count(")")

    @staticmethod
    def solve_part2(input):
        floor = 0
        for i,x in enumerate(input):
            if x == "(":
                floor += 1
            else:
                floor -= 1
            if floor == -1:
                return i + 1
        return None


if __name__ == "__main__":
    Day01().solve_all()
