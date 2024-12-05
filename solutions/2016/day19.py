# https://adventofcode.com/2016/day/19
from solutions.challenge import Challenge
from math import ceil


class Day19(Challenge):
    @staticmethod
    def solve_part1(num_elves):
        elves = list(range(1,num_elves+1))
        while len(elves) > 1:
            elves = elves[::2][0 if len(elves)%2 == 0 else 1:]
        return elves[0]

    @staticmethod
    def solve_part2_naive(num_elves):
        elves = list(range(1,num_elves+1))
        while len(elves) > 1:
            elves.remove(elves[ceil(len(elves)/2.)-(0 if len(elves)/2. == len(elves)//2 else 1)])
            elves = elves[1:] + [elves[0]]
        return elves[0]

    @staticmethod
    def solve_part2(n,i=1):
        # https://www.reddit.com/r/adventofcode/comments/5j4lp1/2016_day_19_solutions/dbdfazy/?utm_source=reddit&utm_medium=web2x&context=3
        while i*3 <= n:
            i *= 3
        return n if n == i else n-i+max(n-2*i,0)


if __name__ == "__main__":
    Day19().solve_all(3005290)
