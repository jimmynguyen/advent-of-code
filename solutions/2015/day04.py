# https://adventofcode.com/2015/day/4
from solutions.challenge import Challenge
import hashlib


class Day04(Challenge):
    @staticmethod
    def solve(key,prefix):
        template = key + "{}"
        num = 1
        while not hashlib.md5(bytes(template.format(num),"utf-8")).hexdigest().startswith(prefix):
            num += 1
        return num

    @staticmethod
    def solve_part1(input):
        return Day04.solve(input,"0"*5)

    @staticmethod
    def solve_part2(input):
        return Day04.solve(input,"0"*6)


if __name__ == "__main__":
    Day04().solve_all()
