# https://adventofcode.com/2025/day/2
from solutions.challenge import Challenge
import re


class Day02(Challenge):
    def read_file(self,filename) -> list[tuple[int,int]]:
        return [tuple(map(int, line.split("-"))) for line in super().read_file(filename, delimiter=",")]

    @staticmethod
    def solve_part1(
        id_ranges: list[tuple[int,int]],
        match_pattern: re.Pattern = r"(.+)\1"
    ):
        invalid_id_sum = 0
        for id_start, id_end in id_ranges:
            for id in range(id_start, id_end + 1):
                has_repeating_pattern = bool(re.fullmatch(match_pattern, str(id)))
                if has_repeating_pattern:
                    invalid_id_sum += id
        return invalid_id_sum

    @staticmethod
    def solve_part2(
        id_ranges: list[tuple[int,int]],
    ):
        return Day02.solve_part1(id_ranges, match_pattern=r"(.+)\1+")


if __name__ == "__main__":
    Day02().solve_all()
