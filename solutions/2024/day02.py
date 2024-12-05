# https://adventofcode.com/2024/day/2
from solutions.challenge import Challenge


class Day02(Challenge):
    def read_file(self, filename: str) -> list[list[int]]:
        return [list(map(int, line.split())) for line in super().read_file(filename)]

    @staticmethod
    def is_valid(levels: list[int]) -> bool:
        increasing = False
        decreasing = False
        invalid = False
        for diff in [a - b for a, b in zip(levels[:-1], levels[1:])]:
            if diff > 0:
                decreasing = True
                if not (diff >= 1 and diff <= 3):
                    invalid = True
                    break
            elif diff < 0:
                increasing = True
                if not (abs(diff) >= 1 and abs(diff) <= 3):
                    invalid = True
                    break
            else:
                invalid = True
                break
            if decreasing and increasing:
                invalid = True
                break
        return not invalid

    @staticmethod
    def solve(reports: list[list[int]], part2: bool =False):
        valid_count = 0
        for levels in reports:
            valid = Day02.is_valid(levels)
            if valid:
                valid_count += 1
            elif part2:
                original_levels = levels
                for idx in range(len(original_levels)):
                    levels = list(original_levels)
                    levels.pop(idx)
                    valid = Day02.is_valid(levels)
                    if valid:
                        valid_count += 1
                        break
        return valid_count

    @staticmethod
    def solve_part1(input: list[list[int]]) -> int:
        return Day02.solve(input)

    @staticmethod
    def solve_part2(input: list[list[int]]) -> int:
        return Day02.solve(input, part2=True)


if __name__ == "__main__":
    Day02().solve_all()
