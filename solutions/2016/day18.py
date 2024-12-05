# https://adventofcode.com/2016/day/18
from solutions.challenge import Challenge


class Day18(Challenge):
    @staticmethod
    def is_trap(tiles):
        return tiles == ("^","^",".") or tiles == (".","^","^") or tiles == ("^",".",".") or tiles == (".",".","^")

    @staticmethod
    def solve_part1(map,num_rows=40):
        map = [map]
        while len(map) < num_rows:
            map.append("".join(["^" if Day18.is_trap(("." if i == 0 else map[-1][i-1],map[-1][i],map[-1][i+1] if i+1 < len(map[-1]) else ".")) else "." for i in range(len(map[-1]))]))
        return "".join(map).count(".")

    @staticmethod
    def solve_part2(map):
        return Day18.solve_part1(map,num_rows=400000)


if __name__ == "__main__":
    Day18().solve_all(".^.^..^......^^^^^...^^^...^...^....^^.^...^.^^^^....^...^^.^^^...^^^^.^^.^.^^..^.^^^..^^^^^^.^^^..^")
