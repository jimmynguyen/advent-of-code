# https://adventofcode.com/2022/day/XX
from typing import Any, List
from challenge import Challenge

class DayXX(Challenge):
    def read_file(self, filename: str) -> List[Any]:
        return super().read_file(filename)

    @staticmethod
    def solve(input: List[Any]) -> int:
        return None

    @staticmethod
    def solve_part1(input: List[Any]) -> int:
        return DayXX.solve(input)

    @staticmethod
    def solve_part2(input: List[Any]) -> int:
        return DayXX.solve(input)


if __name__ == "__main__":
    DayXX().solve_all()
