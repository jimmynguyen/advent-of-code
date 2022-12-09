# https://adventofcode.com/2022/day/9
from typing import List, Tuple
from challenge import Challenge
from math import sqrt

class Day09(Challenge):
    DIAGONAL_DISTANCE = sqrt(2)

    INCREMENTS_BY_DIRECTION_DICT = {
        "R": (0, 1),
        "L": (0, -1),
        "U": (-1, 0),
        "D": (1, 0)
    }

    def read_file(self, filename: str) -> List[Tuple[str, int]]:
        steps = []
        for line in super().read_file(filename):
            direction, distance = line.split()
            steps.append((direction, int(distance)))
        return steps

    @staticmethod
    def compute_distance(position1: List[int], position2: List[int]) -> float:
        return sqrt((position1[0] - position2[0]) ** 2 + (position1[1] - position2[1]) ** 2)

    @staticmethod
    def move(rope, row_increment, col_increment):
        head_knot_position = rope[0]
        head_knot_position[0] += row_increment
        head_knot_position[1] += col_increment
        for idx in range(1, len(rope)):
            prev_knot_position = rope[idx-1]
            curr_knot_position = rope[idx]
            # if distance between the current and previous knots is greater than
            # the distance of a diagonal, move the current knot closer to the
            # previous knot. otherwise, stop moving
            if Day09.compute_distance(prev_knot_position, curr_knot_position) > Day09.DIAGONAL_DISTANCE:
                # update current knot row
                if prev_knot_position[0] < curr_knot_position[0]:
                    curr_knot_position[0] -= 1
                elif prev_knot_position[0] > curr_knot_position[0]:
                    curr_knot_position[0] += 1
                # update current knot column
                if prev_knot_position[1] < curr_knot_position[1]:
                    curr_knot_position[1] -= 1
                elif prev_knot_position[1] > curr_knot_position[1]:
                    curr_knot_position[1] += 1
            else:
                return

    @staticmethod
    def solve(steps: List[Tuple[str, int]], num_knots: int) -> int:
        rope = [[0, 0] for _ in range(num_knots)]
        tail_history = set([tuple(rope[-1])])
        for direction, distance in steps:
            row_increment, col_increment = Day09.INCREMENTS_BY_DIRECTION_DICT[direction]
            for _ in range(distance):
                Day09.move(rope, row_increment, col_increment)
                tail_history.add(tuple(rope[-1]))
        return len(tail_history)

    @staticmethod
    def solve_part1(steps: List[Tuple[str, int]]) -> int:
        return Day09.solve(steps, 2)

    @staticmethod
    def solve_part2(steps: List[Tuple[str, int]]) -> int:
        return Day09.solve(steps, 10)


if __name__ == "__main__":
    Day09().solve_all()
