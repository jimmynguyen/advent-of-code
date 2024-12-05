# https://adventofcode.com/2015/day/12
from solutions.challenge import Challenge
import json


class Day12(Challenge):
    @staticmethod
    def sum_numbers(data,ignore_red):
        sum = 0
        if isinstance(data,list):
            for x in data:
                sum += Day12.sum_numbers(x,ignore_red)
        elif isinstance(data,dict):
            if ignore_red and any([x == "red" for x in data.values()]):
                pass
            else:
                for x in data.values():
                    sum += Day12.sum_numbers(x,ignore_red)
        elif isinstance(data,str):
            pass
        else:
            sum += data
        return sum

    @staticmethod
    def solve(data,ignore_red):
        data = json.loads(data)
        return Day12.sum_numbers(data,ignore_red)

    @staticmethod
    def solve_part1(input):
        return Day12.solve(input,False)

    @staticmethod
    def solve_part2(input):
        return Day12.solve(input,True)


if __name__ == "__main__":
    Day12().solve_all()
