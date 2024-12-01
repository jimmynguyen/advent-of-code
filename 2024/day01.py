# https://adventofcode.com/2024/day/1
from challenge import Challenge


class Day01(Challenge):
    def read_file(self,filename):
        left, right = [], []
        for line in super().read_file(filename):
            left_item, right_item = tuple(line.split("   "))
            left.append(int(left_item))
            right.append(int(right_item))
        return left, right

    @staticmethod
    def solve(input,part2=False):
        left, right = input
        result = 0
        if not part2:
            for a, b in zip(sorted(left), sorted(right)):
                result += abs(a - b)
        else:
            for a in left:
                result += a * sum([1 for b in right if b == a])
        return result

    @staticmethod
    def solve_part1(input):
        return Day01.solve(input)

    @staticmethod
    def solve_part2(input):
        return Day01.solve(input,part2=True)


if __name__ == "__main__":
    Day01().solve_all()
