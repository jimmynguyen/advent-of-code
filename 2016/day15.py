# https://adventofcode.com/2016/day/15
from challenge import Challenge
import re


class Day15(Challenge):
    def read_file(self,filename):
        return {x[0]:x[2:0:-1] for x in sorted([tuple(map(int,re.split(" has | positions; at time=0, it is at position ",x[len("Disc #"):-1]))) for x in super().read_file(filename)],key=lambda x:x[0])}

    @staticmethod
    def solve_part1(state):
        t = 0
        while not all((curr+i+1)%total == 0 for i,(curr,total) in enumerate(state.values())):
            state = {k:((v[0]+1)%v[1],v[1])for k,v in state.items()}
            t += 1
        return t

    @staticmethod
    def solve_part2(state):
        state[max(state.keys())+1] = (0,11)
        return Day15.solve_part1(state)


if __name__ == "__main__":
    Day15().solve_all()
