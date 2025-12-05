# https://adventofcode.com/2025/day/5
from solutions.challenge import Challenge


ParsedChallengeInput = tuple[list[tuple[int,int]],list[int]]


class Day05(Challenge):
    def read_file(self,filename) -> ParsedChallengeInput:
        lines_fresh_ingredient_ranges, lines_available_ingredients = super().read_file(filename, delimiter="\n\n")
        fresh_ingredient_ranges = sorted({tuple(map(int,line.split("-")))for line in lines_fresh_ingredient_ranges.split("\n")})
        available_ingredients = sorted(int(line) for line in lines_available_ingredients.split("\n"))
        return fresh_ingredient_ranges, available_ingredients


    @staticmethod
    def solve_part1(
        parsed_input: ParsedChallengeInput,
    ):
        fresh_ingredient_ranges, available_ingredients = parsed_input
        return sum(
            1
            for available_ingredient in available_ingredients
            if any(available_ingredient >= lo and available_ingredient <= hi for lo, hi in fresh_ingredient_ranges)
        )


    @staticmethod
    def solve_part2(
        parsed_input: ParsedChallengeInput,
    ):
        fresh_ingredient_ranges, _ = parsed_input
        fresh_ingredient_count = 0
        idx = 0
        num_fresh_ingredient_ranges = len(fresh_ingredient_ranges)
        while idx < num_fresh_ingredient_ranges:
            lo_curr, hi_curr = fresh_ingredient_ranges[idx]
            while idx + 1 < num_fresh_ingredient_ranges:
                lo_next, hi_next = fresh_ingredient_ranges[idx + 1]
                if hi_curr >= lo_next: # current range and next range overlaps
                    hi_curr = hi_next if hi_curr <= hi_next else hi_curr # update hi_curr if hi_curr < hi_next
                    idx += 1
                else:
                    break
            fresh_ingredient_count += hi_curr - lo_curr + 1
            idx += 1
        return fresh_ingredient_count


if __name__ == "__main__":
    Day05().solve_all()
