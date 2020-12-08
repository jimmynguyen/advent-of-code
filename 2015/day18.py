# https://adventofcode.com/2015/day/18
import util


def is_corner(h,w,i,j):
    return (i,j) in [(0,0),(0,w-1),(h-1,0),(h-1,w-1)]


def is_on(grid,h,w,i,j,corners_always_on):
    return (corners_always_on and is_corner(h,w,i,j)) or grid[i][j] == "#"


def get_on_neighbors(grid,h,w,i,j,corners_always_on):
    y_min,y_max = max(0,i-1),min(i+2,h)
    x_min,x_max = max(0,j-1),min(j+2,w)
    num_on = 0
    for y in range(y_min,y_max):
        for x in range(x_min,x_max):
            if not (y == i and x == j) and is_on(grid,h,w,y,x,corners_always_on):
                num_on += 1
    return num_on


def solve(grid,args):
    num_steps,corners_always_on = args
    h,w = len(grid),len(grid[0])
    grid = [list(x) for x in grid]
    if corners_always_on:
        grid[0][0] = "#"
        grid[0][w-1] = "#"
        grid[h-1][0] = "#"
        grid[h-1][w-1] = "#"
    for _ in range(num_steps):
        new_grid = [x.copy() for x in grid]
        for i in range(h):
            for j in range(w):
                num_neighbors_on = get_on_neighbors(grid,h,w,i,j,corners_always_on)
                if is_on(grid,h,w,i,j,corners_always_on) and (not corners_always_on or not is_corner(h,w,i,j)) and num_neighbors_on not in [2,3]:
                    new_grid[i][j] = "."
                elif grid[i][j] == "." and num_neighbors_on == 3:
                    new_grid[i][j] = "#"
        grid = new_grid
    return sum([1 for x in grid for y in x if y == "#"])


if __name__ == "__main__":
    day = 18
    inputs = [(100,False),(100,True)]
    test_inputs2 = [(4,False),(5,True)]
    test_outputs = [4,17]
    util.solve(day,inputs,test_outputs,solve,test_inputs2=test_inputs2)