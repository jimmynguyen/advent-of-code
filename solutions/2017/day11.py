# https://adventofcode.com/2017/day/11
from solutions.challenge import Challenge
from math import inf


class Day11(Challenge):
    @staticmethod
    def get_dist_from_origin(coords):
        coords = [x for x in coords]
        dist = 0
        while (coords[0] > 0 and coords[1] < 0) or (coords[0] < 0 and coords[1] > 0):
            coords[0] += -1 if coords[0] > 0 else 1
            coords[1] += 1 if coords[1] < 0 else -1
            dist += 1
        return dist + sum(abs(x) for x in coords)

    @staticmethod
    def solve_part1(directions, return_max=False):
        coords = [0,0]
        max_dist = -inf
        for dir in directions.split(","):
            if dir == "n":
                coords[0] += 0
                coords[1] -= 1
            elif dir == "s":
                coords[0] += 0
                coords[1] += 1
            elif dir == "nw":
                coords[0] -= 1
                coords[1] += 0
            elif dir == "se":
                coords[0] += 1
                coords[1] += 0
            elif dir == "sw":
                coords[0] -= 1
                coords[1] += 1
            elif dir == "ne":
                coords[0] += 1
                coords[1] -= 1
            if return_max:
                max_dist = max(max_dist, Day11.get_dist_from_origin(coords))
        return max_dist if return_max else Day11.get_dist_from_origin(coords)

    @staticmethod
    def solve_part2(directions, return_max=True):
        return Day11.solve_part1(directions, return_max=return_max)


if __name__ == "__main__":
    Day11().solve_all()
