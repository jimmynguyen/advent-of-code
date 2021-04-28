# https://adventofcode.com/2017/day/19
from challenge import Challenge
from typing import Sequence


class Day19(Challenge):
    def read_file(self, filename: str, strip: bool=False):
        return super().read_file(filename, strip=strip)

    @staticmethod
    def solve_part1(diagram: Sequence[str], return_steps: bool=False) -> int:
        row = 1
        col = diagram[0].index("|")
        dir = "S"
        path = ""
        steps = 1
        while 0 <= row < len(diagram) and 0 <= col <= len(diagram[row]) and diagram[row][col] != " ":
            if diagram[row][col] in "|-" or diagram[row][col].isalpha():
                if diagram[row][col].isalpha():
                    path += diagram[row][col]
                if dir == "S":
                    row += 1
                elif dir == "N":
                    row -= 1
                elif dir == "E":
                    col += 1
                elif dir == "W":
                    col -= 1
                else:
                    raise ValueError("invalid scenario 1")
            elif diagram[row][col] == "+":
                if dir in "NS":
                    if col + 1 >= len(diagram[row]) or diagram[row][col + 1] == " ":
                        dir = "W"
                        col -= 1
                    elif col - 1 < 0 or diagram[row][col - 1] == " ":
                        dir = "E"
                        col += 1
                    else:
                        raise ValueError("invalid scenario 2")
                elif dir in "WE":
                    if row + 1 >= len(diagram) or len(diagram[row + 1]) < col or diagram[row + 1][col] == " ":
                        dir = "N"
                        row -= 1
                    elif row - 1 < 0 or len(diagram[row - 1]) < col or diagram[row - 1][col] == " ":
                        dir = "S"
                        row += 1
                    else:
                        raise ValueError("invalid scenario 3")
                else:
                    raise ValueError("invalid scenario 4")
            else:
                raise ValueError("invalid scenario 5")
            steps += 1
        return steps if return_steps else path

    @staticmethod
    def solve_part2(diagram: Sequence[str], return_steps: bool=True) -> int:
        return Day19.solve_part1(diagram, return_steps)


if __name__ == "__main__":
    Day19().solve_all()
