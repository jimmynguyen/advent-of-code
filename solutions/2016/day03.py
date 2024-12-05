# https://adventofcode.com/2016/day/3
from solutions.challenge import Challenge


class Day03(Challenge):
    @staticmethod
    def get_triangles(input):
        return [tuple(map(int,x.strip().split())) for x in input]

    @staticmethod
    def solve(triangles,verbose=False):
        num_possible = 0
        for triangle in triangles:
            # https://en.wikipedia.org/wiki/Triangle_inequality
            if 2*max(triangle) < sum(triangle):
                num_possible += 1
        return num_possible

    @staticmethod
    def solve_part1(input):
        return Day03.solve(Day03.get_triangles(input))

    @staticmethod
    def solve_part2(input):
        input = Day03.get_triangles(input)
        triangles = [(input[i][j],input[i+1][j],input[i+2][j]) for i in range(0,len(input),3) for j in range(3)]
        return Day03.solve(triangles)


if __name__ == "__main__":
    Day03().solve_all()
