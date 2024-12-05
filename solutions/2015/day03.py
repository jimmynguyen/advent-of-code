# https://adventofcode.com/2015/day/3
from solutions.challenge import Challenge


class Day03(Challenge):
    @staticmethod
    def get_direction(d):
        if d == "^":
            direction = (0,1)
        elif d == "v":
            direction = (0,-1)
        elif d == "<":
            direction = (-1,0)
        elif d == ">":
            direction = (1,0)
        else:
            raise Exception("Invalid direction {}".format(d))
        return direction

    @staticmethod
    def solve(directions,position):
        visited = set(position)
        for i in range(0,len(directions),len(position)):
            for j in range(len(position)):
                direction = Day03.get_direction(directions[i+j])
                position[j] = tuple([sum(x) for x in zip(position[j],direction)])
                visited.add(position[j])
        return len(visited)

    @staticmethod
    def solve_part1(input):
        return Day03.solve(input,[(0,0)])

    @staticmethod
    def solve_part2(input):
        return Day03.solve(input,[(0,0),(0,0)])


if __name__ == "__main__":
    Day03().solve_all()
