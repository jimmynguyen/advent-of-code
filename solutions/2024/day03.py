# https://adventofcode.com/2024/day/3
from solutions.challenge import Challenge
import re


class Day03(Challenge):
    def read_file(self, filename: str) -> str:
        return "".join(line.strip() for line in super().read_file(filename))

    @staticmethod
    def solve(instructions: str, regex: str) -> int:
        result = 0
        skip = False
        for instruction in re.findall(regex, instructions):
            if instruction == "don't()":
                skip = True
            elif instruction == "do()":
                skip = False
            elif not skip and instruction.startswith("mul("):
                a, b = tuple(map(int, instruction[len("mul("):-len(")")].split(",")))
                result += a * b
        return result

    @staticmethod
    def solve_part1(instructions: str) -> int:
        return Day03.solve(instructions, r"mul\(\d+,\d+\)")

    @staticmethod
    def solve_part2(instructions: str) -> int:
        return Day03.solve(instructions, r"mul\(\d+,\d+\)|don\'t\(\)|do\(\)")


if __name__ == "__main__":
    Day03().solve_all()
