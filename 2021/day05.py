# https://adventofcode.com/2021/day/5
from challenge import Challenge


class Day05(Challenge):
    def read_file(self, filename):
        return [tuple(tuple(map(int, y.split(","))) for y in x.split(" -> ")) for x in super().read_file(filename)]

    @staticmethod
    def solve(paths):
        nrows, ncols = 1 + max(y[1] for x in paths for y in x), 1 + max(y[0] for x in paths for y in x)
        graph = [[0 for _ in range(ncols)] for _ in range(nrows)]
        for (x1, y1), (x2, y2) in paths:
            if x1 == x2:
                yrange = range(min(y1, y2), max(y1, y2) + 1)
                xrange = [x1] * len(yrange)
            elif y1 == y2:
                xrange = range(min(x1, x2), max(x1, x2) + 1)
                yrange = [y1] * len(xrange)
            else:
                xmin = min(x1, x2)
                if xmin == x1:
                    xrange = range(x1, x2 + 1)
                    yrange = range(y1, y2 + (1 if y1 < y2 else -1), 1 if y1 < y2 else -1)
                else:
                    xrange = range(x2, x1 + 1)
                    yrange = range(y2, y1 + (1 if y2 < y1 else -1), 1 if y2 < y1 else -1)
            for x, y in list(zip(xrange, yrange)):
                graph[y][x] += 1
        return sum(1 for r in graph for c in r if c >= 2)

    @staticmethod
    def solve_part1(paths):
        paths = [((x1, y1), (x2, y2)) for (x1, y1), (x2, y2) in paths if x1 == x2 or y1 == y2]
        return Day05.solve(paths)

    @staticmethod
    def solve_part2(paths):
        return Day05.solve(paths)


if __name__ == "__main__":
    Day05().solve_all()
