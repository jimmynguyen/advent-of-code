# https://adventofcode.com/2016/day/2
from challenge import Challenge


class Day02(Challenge):
    @staticmethod
    def solve(directions,pos,keypad,verbose=False):
        code = ""
        if verbose: print(pos)
        for direction in directions:
            if verbose: print(direction)
            for dir in direction:
                if verbose: print(dir)
                if dir == Direction.UP and pos[0]-1 >= 0 and keypad[pos[0]-1][pos[1]] is not None:
                    pos[0] -= 1
                elif dir == Direction.DOWN and pos[0]+1 < len(keypad) and keypad[pos[0]+1][pos[1]] is not None:
                    pos[0] += 1
                elif dir == Direction.LEFT and pos[1]-1 >= 0 and keypad[pos[0]][pos[1]-1] is not None:
                    pos[1] -= 1
                elif dir == Direction.RIGHT and pos[1]+1 < len(keypad) and keypad[pos[0]][pos[1]+1] is not None:
                    pos[1] += 1
                if verbose: print(pos)
            code += str(keypad[pos[0]][pos[1]])
        return code

    @staticmethod
    def solve_part1(input):
        return Day02.solve(input,pos=[1,1],keypad=[[1,2,3],[4,5,6],[7,8,9]])

    @staticmethod
    def solve_part2(input):
        return Day02.solve(input,pos=[2,0],keypad=[[None,None,1,None,None],[None,2,3,4,None],[5,6,7,8,9],[None,"A","B","C",None],[None,None,"D",None,None]])


class Direction:
    UP = "U"
    DOWN = "D"
    LEFT = "L"
    RIGHT = "R"


if __name__ == "__main__":
    Day02().solve_all()
