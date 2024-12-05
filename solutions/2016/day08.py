# https://adventofcode.com/2016/day/8
from solutions.challenge import Challenge
import numpy as np


class Day08(Challenge):
    @staticmethod
    def get_screen(instructions,width=50,height=6):
        screen = np.zeros((height,width),dtype=bool)
        for ins in instructions:
            if Operations.RECT in ins:
                w,h = tuple(map(int,ins.strip(Operations.RECT).split("x")))
                screen[:h,:w] = True
            elif Operations.ROTATE_ROW in ins:
                row,shift = tuple(map(int,ins.strip(Operations.ROTATE_ROW).split(" by ")))
                shift = shift % width
                if shift > 0:
                    screen[row,:] = np.hstack((screen[row,-shift:],screen[row,:-shift]))
            elif Operations.ROTATE_COL in ins:
                col,shift = tuple(map(int,ins.strip(Operations.ROTATE_COL).split(" by ")))
                shift = shift % width
                if shift > 0:
                    screen[:,col] = np.hstack((screen[-shift:,col],screen[:-shift,col]))
            else:
                raise ValueError(f"Invalid instruction: {ins}")
        return screen

    @staticmethod
    def solve_part1(instructions,width=50,height=6):
        screen = Day08.get_screen(instructions,width,height)
        return screen.sum()

    @staticmethod
    def solve_part2(instructions,letter_width=5):
        screen = Day08.get_screen(instructions).astype(str)
        screen[screen == "True"] = "#"
        screen[screen == "False"] = "."
        np.set_printoptions(linewidth=225)
        print(screen)


class Operations:
    RECT = "rect "
    ROTATE_ROW = "rotate row y="
    ROTATE_COL = "rotate column x="


if __name__ == "__main__":
    Day08().solve_all()
