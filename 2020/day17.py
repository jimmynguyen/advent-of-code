# https://adventofcode.com/2020/day/17
from challenge import Challenge
import numpy as np


class Day17(Challenge):
    @staticmethod
    def count_active_neighbors(i,j,k,l,h,w,d,t,grid):
        x_min,x_max = max(0,i-1),min(w,i+2)
        y_min,y_max = max(0,j-1),min(h,j+2)
        z_min,z_max = max(0,k-1),min(d,k+2)
        w_min,w_max = max(0,l-1),min(t,l+2)
        return np.count_nonzero(grid[x_min:x_max,y_min:y_max,z_min:z_max,w_min:w_max]) - (1 if grid[i,j,k,l] else 0)

    @staticmethod
    def pad_3d_grid(grid):
        grid = np.pad(grid,pad_width=10,mode="constant",constant_values=False)
        grid = grid[...,np.newaxis]
        return grid

    @staticmethod
    def pad_4d_grid(grid):
        top_layer = np.zeros_like(grid)
        bot_layer = np.zeros_like(grid)
        grid = np.stack((top_layer,grid,bot_layer),axis=3)
        grid = np.pad(grid,pad_width=10,mode="constant",constant_values=False)
        return grid

    @staticmethod
    def solve(grid,pad_grid):
        grid = np.array([[y == "#" for y in x] for x in grid])
        top_layer = np.array([[False for _ in range(grid.shape[1])] for _ in range(grid.shape[0])])
        bot_layer = np.array([[False for _ in range(grid.shape[1])] for _ in range(grid.shape[0])])
        grid = np.dstack((top_layer,grid,bot_layer))
        grid = pad_grid(grid)
        h,w,d,t = grid.shape
        for _ in range(6):
            _grid = grid.copy()
            for i in range(h):
                for j in range(w):
                    for k in range(d):
                        for l in range(t):
                            num_active_neighbors = Day17.count_active_neighbors(i,j,k,l,h,w,d,t,grid)
                            if grid[i,j,k,l] and num_active_neighbors not in [2,3]:
                                _grid[i,j,k,l] = False
                            elif not grid[i,j,k,l] and num_active_neighbors == 3:
                                _grid[i,j,k,l] = True
            grid = _grid
        return np.count_nonzero(grid)

    @staticmethod
    def solve_part1(input):
        return Day17.solve(input,Day17.pad_3d_grid)

    @staticmethod
    def solve_part2(input):
        return Day17.solve(input,Day17.pad_4d_grid)


if __name__ == "__main__":
    Day17().solve_all()
