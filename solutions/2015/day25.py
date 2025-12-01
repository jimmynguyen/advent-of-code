# https://adventofcode.com/2015/day/25
from solutions.challenge import Challenge
import numpy as np


class Day25(Challenge):
    def read_file(self,filename):
        instruction = super().read_file(filename)
        row = int(instruction.split("row ")[1].split(",")[0])
        col = int(instruction.split("column ")[1].split(".")[0])
        return row,col

    @staticmethod
    def solve(pos,num_grps=3,verbose=False):
        row,col = pos
        known_codes = np.array([
            [20151125, 18749137, 17289845, 30943339, 10071777, 33511524],
            [31916031, 21629792, 16929656, 7726640, 15514188, 4041754],
            [16080970, 8057251, 1601130, 7981243, 11661866, 16474243],
            [24592653, 32451966, 21345942, 9380097, 10600672, 31527494],
            [77061, 17552253, 28094349, 6899651, 9250759, 31663883],
            [33071741, 6796745, 25397450, 24659492, 1534922, 27995004],
        ],dtype=np.int64)
        dim = 2*max(row,col)
        codes = np.zeros((dim,dim),dtype=np.int64)
        codes[:known_codes.shape[0],:known_codes.shape[1]] = known_codes
        for d in range(dim):
            for i,j in zip(reversed(range(d+1)),range(d+1)):
                if codes[i,j] == 0:
                    codes[i,j] = (prev_code*252533)%33554393
                if verbose: print(i,j,codes[i,j])
                if row-1 == i and col-1 == j:
                    return codes[i,j]
                prev_code = codes[i,j]
        return codes[row-1,col-1]

    @staticmethod
    def solve_part1(input):
        return Day25.solve(input,num_grps=3)

    @staticmethod
    def solve_part2(input):
        pass


if __name__ == "__main__":
    Day25().solve_all()
