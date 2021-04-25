# https://adventofcode.com/2017/day/5
from challenge import Challenge


class Day05(Challenge):
    def read_file(self,filename):
        return [int(x) for x in super().read_file(filename)]

    @staticmethod
    def solve_part1(instructions,allow_decrement=False):
        pc = 0
        steps = 0
        while pc >= 0 and pc < len(instructions):
            offset = instructions[pc]
            instructions[pc] += -1 if offset >= 3 and allow_decrement else 1
            pc += offset
            steps += 1
        return steps

    @staticmethod
    def solve_part2(instructions):
        return Day05.solve_part1(instructions,allow_decrement=True)


if __name__ == "__main__":
    Day05().solve_all()
