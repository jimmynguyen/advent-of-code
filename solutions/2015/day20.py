# https://adventofcode.com/2015/day/20
from solutions.challenge import Challenge
import numba


class Day20(Challenge):
    @staticmethod
    @numba.njit
    def count_presents_with_inf_elves(elf,house):
        return (10 * elf) if house % elf == 0 else 0

    @staticmethod
    @numba.njit
    def count_presents_with_max_elves(elf,house,max_elves=50):
        return (11 * elf) if house % elf == 0 and elf * max_elves >= house else 0

    @staticmethod
    @numba.njit
    def solve(goal,count_presents):
        num_presents = 0
        house = 0
        while num_presents < goal:
            house += 1
            num_presents = 0
            for elf in range(1,house+1):
                num_presents += count_presents(elf,house)
        return house

    @staticmethod
    def solve_part1(input):
        return Day20.solve(int(input),Day20.count_presents_with_inf_elves)

    @staticmethod
    def solve_part2(input):
        return Day20.solve(int(input),Day20.count_presents_with_max_elves)


if __name__ == "__main__":
    Day20().solve_all()
