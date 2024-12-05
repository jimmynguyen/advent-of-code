# https://adventofcode.com/2021/day/1
from solutions.challenge import Challenge


class Day01(Challenge):
    def read_file(self, filename):
        return list(map(int, super().read_file(filename)))

    @staticmethod
    def solve(nums, increment):
        comparison_nums = [sum(nums[i:i+increment]) for i in range(len(nums) + 1 - increment)]
        return len([i for i in range(len(comparison_nums)-1) if comparison_nums[i+1] > comparison_nums[i]])

    @staticmethod
    def solve_part1(input):
        return Day01.solve(input, 1)

    @staticmethod
    def solve_part2(input):
        return Day01.solve(input, 3)


if __name__ == "__main__":
    Day01().solve_all()
