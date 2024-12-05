# https://adventofcode.com/2017/day/2
from solutions.challenge import Challenge
from itertools import combinations


class Day02(Challenge):
    def read_file(self,filename):
        return [list(map(int,x.split())) for x in super().read_file(filename)]

    @staticmethod
    def solve_part1(data):
        return sum(max(x)-min(x) for x in data)

    @staticmethod
    def solve_part2(data):
        return sum(max(y)//min(y) for x in data for y in combinations(x,2) if max(y)%min(y) == 0)


if __name__ == "__main__":
    Day02().solve_all()
