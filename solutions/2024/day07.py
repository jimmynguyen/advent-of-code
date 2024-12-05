# https://adventofcode.com/2024/day/7
from typing import List, Tuple
from challenge import Challenge
from itertools import product


ParsedChallengeInput = List[Tuple[int, List[int]]]


def solve(equations: ParsedChallengeInput, possible_operands: str) -> int:
    calibration_result = 0
    for result, numbers in equations:
        for operands in product(possible_operands, repeat=len(numbers)-1):
            current_result = numbers[0]
            for idx, operand in enumerate(operands):
                if operand == "+":
                    current_result += numbers[idx+1]
                elif operand == "*":
                    current_result *= numbers[idx+1]
                elif operand == "|":
                    current_result = int(f"{current_result}{numbers[idx+1]}")
                else:
                    raise Exception(f"Invalid operand={operand}")
            if result == current_result:
                calibration_result += result
                break
    return calibration_result


class Day07(Challenge):
    def read_file(self, filename: str) -> ParsedChallengeInput:
        equations = []
        for line in super().read_file(filename):
            result, numbers = line.split(": ")
            result, numbers = int(result), [int(number) for number in numbers.strip().split()]
            equations.append((result, numbers))
        return equations

    @staticmethod
    def solve_part1(equations: ParsedChallengeInput) -> int:
        return solve(equations, possible_operands="+*")


    @staticmethod
    def solve_part2(equations: ParsedChallengeInput) -> int:
        return solve(equations, possible_operands="+*|")


if __name__ == "__main__":
    Day07().solve_all()
