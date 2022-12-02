# https://adventofcode.com/2022/day/1
from challenge import Challenge


class Day01(Challenge):
    def read_file(self,filename):
        return [list(map(int, x.split("\n"))) for x in super().read_file(filename, delimiter="\n\n")]

    @staticmethod
    def solve(elf_inventories, compute):
        return compute(sum(elf_inventory) for elf_inventory in elf_inventories)

    @staticmethod
    def solve_part1(input):
        return Day01.solve(input, max)

    @staticmethod
    def solve_part2(input):
        return Day01.solve(input, lambda inventory_sums: sum(sorted(inventory_sums, reverse=True)[:3]))


if __name__ == "__main__":
    Day01().solve_all()
