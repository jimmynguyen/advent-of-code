# https://adventofcode.com/2015/day/10
from solutions.challenge import Challenge


class Day10(Challenge):
    @staticmethod
    def solve(seq,num_passes):
        for _ in range(num_passes):
            res = ""
            i = 0
            subseq = None
            while i < len(seq):
                subseq = seq[i]
                while i < len(seq)-1 and seq[i] == seq[i+1]:
                    i += 1
                    subseq += seq[i]
                res += str(len(subseq)) + subseq[0]
                i += 1
            seq = res
        return len(seq)

    @staticmethod
    def solve_part1(input):
        return Day10.solve(input,40)

    @staticmethod
    def solve_part2(input):
        return Day10.solve(input,50)


if __name__ == "__main__":
    Day10().solve_all()
