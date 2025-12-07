# https://adventofcode.com/2025/day/6
from solutions.challenge import Challenge
from math import prod
from collections import defaultdict


ParsedChallengeInput = list[tuple]


class Day06(Challenge):
    def read_file(self,filename) -> ParsedChallengeInput:
        lines = super().read_file(filename, delimiter="\n", strip=False)
        operation_indices = [idx for idx, character in enumerate(lines[-1]) if character != " "]
        return [
            tuple((line[idx_start:idx_end] + (" " if line[idx_end-1] != " " else ""))[:-1] for line in lines)
            for idx_start, idx_end
            in zip(operation_indices, operation_indices[1:] + [len(lines[-1])])
        ]


    @staticmethod
    def solve_part1(
        parsed_input: ParsedChallengeInput,
    ):
        problems = parsed_input
        grand_total = 0
        for problem in problems:
            nums = list(map(int, problem[:-1]))
            if problem[-1].strip() == "+":
                total = sum(nums)
            elif problem[-1].strip() == "*":
                total = prod(nums)
            else:
                raise RuntimeError(f"Invalid operation={problem[-1]}")
            grand_total += total
        return grand_total


    @staticmethod
    def solve_part2(
        parsed_input: ParsedChallengeInput,
    ):
        problems = parsed_input
        grand_total = 0
        for problem in problems:
            grid = defaultdict(lambda: "")
            ncols = len(problem[:-1])
            nrows = 0
            for idx, row in enumerate(problem[:-1]):
                nrows = max(nrows, len(row))
                for jdx, num in enumerate(row[::-1]):
                    grid[(idx, jdx)] = num
            nums = []
            for idx in range(nrows):
                num = ""
                for jdx in range(ncols):
                    num += grid[(jdx, idx)]
                nums.append(int(num))
            if problem[-1].strip() == "+":
                total = sum(nums)
            elif problem[-1].strip() == "*":
                total = prod(nums)
            else:
                raise RuntimeError(f"Invalid operation={problem[-1]}")
            grand_total += total
        return grand_total


if __name__ == "__main__":
    Day06().solve_all()
