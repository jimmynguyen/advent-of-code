# https://adventofcode.com/2021/day/13
from solutions.challenge import Challenge


class Day13(Challenge):
    def read_file(self, filename):
        points, instructions = tuple(x.split("\n") for x in super().read_file(filename, delimiter = "\n\n"))
        points = [tuple(reversed([int(x) for x in point.split(",")])) for point in points]
        nrows = max(i for i, _ in points) + 2
        ncols = max(j for _, j in points) + 1
        paper = [["."] * ncols for _ in range(nrows)]
        for i, j in points:
            paper[i][j] = "#"
        return paper, [(axis, int(position)) for axis, position in [tuple(x.strip("fold along ").split("=")) for x in instructions]]

    @staticmethod
    def solve(input, num_instructions, print_paper=False):
        paper, instructions = input
        # print(len(paper), len(paper[0]))
        # print("original counts:", sum(1 if col == "#" else 0 for row in paper for col in row))
        for axis, position in instructions[:num_instructions]:
            # print(axis, position)
            if axis == "x":
                part1, part2 = [row[:position] for row in paper], [row[position+1:][::-1] for row in paper]
                # [print(x) for x in part1]
                # print()
                # [print(x) for x in part2]
            elif axis == "y":
                part1, part2 = paper[:position-1], paper[position:][::-1]
                # [print(x) for x in part1]
                # print()
                # [print(x) for x in part2]
            else:
                raise Exception(f"Unexpected axis: {axis}")
            # print("part1 counts:", sum(1 if col == "#" else 0 for row in part1 for col in row))
            # print(len(part1), len(part1[0]))
            # print("part2 counts:", sum(1 if col == "#" else 0 for row in part2 for col in row))
            # print(len(part2), len(part2[0]))
            for i in range(len(part1)):
                for j in range(len(part1[0])):
                    part1[i][j] = "#" if part1[i][j] == "#" or part2[i][j] == "#" else "."
            paper = part1
        # print("post-fold counts:", sum(1 if col == "#" else 0 for row in paper for col in row))
        if print_paper:
          paper2 = []
          for row in paper:
              paper2.append("".join(row))
          [print(x) for x in paper2]
        return sum(1 if col == "#" else 0 for row in paper for col in row)

    @staticmethod
    def solve_part1(input):
        return Day13.solve(input, 1)

    @staticmethod
    def solve_part2(input):
        return Day13.solve(input, len(input[1]), True)


if __name__ == "__main__":
    Day13().solve_all()
