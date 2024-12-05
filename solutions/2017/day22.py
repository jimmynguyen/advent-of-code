# https://adventofcode.com/2017/day/22
from typing import List
from solutions.challenge import Challenge

class Day22(Challenge):
    def read_file(self, filename: str) -> List[str]:
        return super().read_file(filename)

    @staticmethod
    def solve(rules: List[str], part2: bool = False) -> int:
        return 0


    @staticmethod
    def solve_part1(rules: List[str]) -> int:
        return Day22.solve(rules)

    @staticmethod
    def solve_part2(rules: List[str]) -> int:
        return Day22.solve(rules, True)


if __name__ == "__main__":
    Day22().solve_all()
