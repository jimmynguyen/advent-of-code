# https://adventofcode.com/2022/day/6
from typing import Union
from challenge import Challenge

class Day06(Challenge):
    def read_file(self, filename: str) -> str:
        return super().read_file(filename)

    @staticmethod
    def solve(input: str, target_length: int) -> Union[int, None]:
        for start, end in zip(range(0, len(input) - target_length), range(target_length, len(input))):
            if len(set(input[start:end])) == target_length:
                return end
        return None

    @staticmethod
    def solve_part1(input: str) -> int:
        return Day06.solve(input, target_length=4)

    @staticmethod
    def solve_part2(input: str) -> int:
        return Day06.solve(input, target_length=14)


if __name__ == "__main__":
    Day06().solve_all()
