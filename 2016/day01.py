# https://adventofcode.com/2016/day/1
from challenge import Challenge


class Day01(Challenge):
    @staticmethod
    def update_state(pos,idx,neg,dist,visited,part2,part2_soln=None):
        if part2:
            for d in range(1,dist+1):
                new_pos = [x for x in pos]
                new_pos[idx] += -d if neg else d
                x,y = tuple(new_pos)
                if (x,y) in visited:
                    part2_soln = sum(abs(x) for x in new_pos)
                    break
                visited.add((x,y))
        pos[idx] += -dist if neg else dist
        return pos,visited,part2_soln

    @staticmethod
    def solve(directions,part2=False,verbose=False):
        directions = [(x[0],int(x[1:])) for x in directions.split(", ")]
        dir = Direction.NORTH
        pos = [0,0]
        if verbose: print(dir,pos)
        visited = {tuple(pos)}
        for turn,dist in directions:
            if verbose: print(turn,dist)
            if (dir == Direction.NORTH and turn == Turn.RIGHT) or (dir == Direction.SOUTH and turn == Turn.LEFT):
                dir = Direction.EAST
                idx,neg = 1,False
                pos,visited,part2_soln = Day01.update_state(pos,idx,neg,dist,visited,part2)
                if part2_soln is not None:
                    return part2_soln
            elif (dir == Direction.NORTH and turn == Turn.LEFT) or (dir == Direction.SOUTH and turn == Turn.RIGHT):
                dir = Direction.WEST
                idx,neg = 1,True
                pos,visited,part2_soln = Day01.update_state(pos,idx,neg,dist,visited,part2)
                if part2_soln is not None:
                    return part2_soln
            elif (dir == Direction.EAST and turn == Turn.RIGHT) or (dir == Direction.WEST and turn == Turn.LEFT):
                dir = Direction.SOUTH
                idx,neg = 0,True
                pos,visited,part2_soln = Day01.update_state(pos,idx,neg,dist,visited,part2)
                if part2_soln is not None:
                    return part2_soln
            elif (dir == Direction.EAST and turn == Turn.LEFT) or (dir == Direction.WEST and turn == Turn.RIGHT):
                dir = Direction.NORTH
                idx,neg = 0,False
                pos,visited,part2_soln = Day01.update_state(pos,idx,neg,dist,visited,part2)
                if part2_soln is not None:
                    return part2_soln
            else:
                raise ValueError(f"Invalid case: dir={dir}, turn={turn}")
            if verbose: print(dir,pos)
        return sum(abs(x) for x in pos)

    @staticmethod
    def solve_part1(input):
        return Day01.solve(input)

    @staticmethod
    def solve_part2(input):
        return Day01.solve(input,part2=True)


class Direction:
    NORTH = "N"
    SOUTH = "S"
    EAST = "E"
    WEST = "W"


class Turn:
    RIGHT = "R"
    LEFT = "L"


if __name__ == "__main__":
    Day01().solve_all()
