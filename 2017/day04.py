# https://adventofcode.com/2017/day/4
from challenge import Challenge


class Day04(Challenge):
    def read_file(self,filename):
        return [x.split() for x in super().read_file(filename)]

    @staticmethod
    def solve_part1(passphrases):
        return len([x for x in passphrases if len(x) == len(set(x))])

    @staticmethod
    def solve_part2(passphrases):
        return Day04.solve_part1([["".join(sorted(y)) for y in x] for x in passphrases])


if __name__ == "__main__":
    Day04().solve_all()
