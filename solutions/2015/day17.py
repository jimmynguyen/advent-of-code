# https://adventofcode.com/2015/day/17
from solutions.challenge import Challenge
from itertools import combinations


class Day17(Challenge):
    @staticmethod
    def solve(containers,args):
        liters,find_min_num_containers = args
        containers = [int(x) for x in containers]
        combos = [x for n in range(1,len(containers)) for x in combinations(containers,n) if sum(x) == liters]
        if find_min_num_containers:
            min_num_containers = min(len(x) for x in combos)
            combos = [x for x in combos if len(x) == min_num_containers]
        return len(combos)

    @staticmethod
    def solve_part1(input):
        return Day17.solve(input,(150,False))

    @staticmethod
    def solve_part2(input):
        return Day17.solve(input,(150,True))


if __name__ == "__main__":
    Day17().solve_all()
