# https://adventofcode.com/2021/day/2
from solutions.challenge import Challenge


class Direction:
    FORWARD = "forward"
    UP = "up"
    DOWN = "down"


class Day02(Challenge):
    def read_file(self, filename):
        return [(direction, int(units)) for direction, units in [tuple(x.split(" ")) for x in super().read_file(filename)]]

    @staticmethod
    def solve_part1(commands):
        hpos, depth = 0, 0
        for direction, units in commands:
            if direction == Direction.FORWARD:
                hpos += units
            elif direction == Direction.UP:
                depth -= units
            elif direction == Direction.DOWN:
                depth += units
        return hpos * depth

    @staticmethod
    def solve_part2(commands):
        hpos, depth, aim = 0, 0, 0
        for direction, units in commands:
            if direction == Direction.FORWARD:
                hpos += units
                depth += aim * units
            elif direction == Direction.UP:
                aim -= units
            elif direction == Direction.DOWN:
                aim += units
        return hpos * depth


if __name__ == "__main__":
    Day02().solve_all()
