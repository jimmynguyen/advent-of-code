# https://adventofcode.com/2021/day/7
from challenge import Challenge


class Day07(Challenge):
    def read_file(self, filename):
        return list(map(int, super().read_file(filename).split(",")))

    @staticmethod
    def compute_cost(target_position, position, history):
        key = (min(target_position, position), max(target_position, position))
        if key not in history:
            history[key] = sum(1 + x for x in range(0, abs(target_position - position)))
        return history[key]

    @staticmethod
    def solve(positions, compute_cost, history = {}):
        position_counts = {}
        for position in positions:
            position_counts[position] = position_counts.get(position, 0) + 1
        return min(sum(compute_cost(target_position, position, history) * count for position, count in position_counts.items()) for target_position in range(0, max(positions) + 1))

    @staticmethod
    def solve_part1(input):
        return Day07.solve(input, lambda target_position, position, history: abs(target_position - position))

    @staticmethod
    def solve_part2(input):
        return Day07.solve(input, Day07.compute_cost)


if __name__ == "__main__":
    Day07().solve_all()
