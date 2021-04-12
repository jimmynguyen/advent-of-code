# https://adventofcode.com/2020/day/11
from challenge import Challenge


class Day11(Challenge):
    @staticmethod
    def count_num_occupied_neighbors_1(i,j,h,w,grid):
        y_min,y_max = max(0,i-1),min(h-1,i+1)
        x_min,x_max = max(0,j-1),min(w-1,j+1)
        num_occupied_neighbors = 0
        for y in range(y_min,y_max+1):
            for x in range(x_min,x_max+1):
                if (not (y == i and x == j)) and grid[y][x] == Status.OCCUPIED:
                    num_occupied_neighbors += 1
        return num_occupied_neighbors

    @staticmethod
    def count_num_occupied_neighbors_2(i,j,h,w,grid):
        directions = [[0,-1],[1,-1],[1,0],[1,1],[0,1],[-1,1],[-1,0],[-1,-1]]
        num_occupied_neighbors = 0
        for direction in directions:
            y,x = i,j
            is_occupied = False
            while True:
                y,x = y+direction[0],x+direction[1]
                if y < 0 or y >= h or x < 0 or x >= w:
                    break
                elif grid[y][x] == Status.OCCUPIED:
                    is_occupied = True
                    break
                elif grid[y][x] == Status.EMPTY:
                    break
            if is_occupied:
                num_occupied_neighbors += 1
        return num_occupied_neighbors

    @staticmethod
    def count_num_occupied(grid):
        num_occupied = 0
        for row in grid:
            for seat in row:
                if seat == Status.OCCUPIED:
                    num_occupied += 1
        return num_occupied

    @staticmethod
    def solve(grid,args):
        count_num_occupied_neighbors,num_occupied_neighbors_limit = args
        h,w = len(grid),len(grid[0])
        while True:
            new_grid = [x for x in grid]
            num_changes = 0
            for i in range(h):
                for j in range(w):
                    num_occupied_neighbors = count_num_occupied_neighbors(i,j,h,w,grid)
                    if grid[i][j] == Status.EMPTY and num_occupied_neighbors == 0:
                        new_grid[i] = new_grid[i][:j] + Status.OCCUPIED + new_grid[i][j+1:]
                        num_changes += 1
                    elif grid[i][j] == Status.OCCUPIED and num_occupied_neighbors >= num_occupied_neighbors_limit:
                        new_grid[i] = new_grid[i][:j] + Status.EMPTY + new_grid[i][j+1:]
                        num_changes += 1
            grid = new_grid
            if num_changes == 0:
                break
        return Day11.count_num_occupied(grid)

    @staticmethod
    def solve_part1(input):
        return Day11.solve(input,(Day11.count_num_occupied_neighbors_1,4))

    @staticmethod
    def solve_part2(input):
        return Day11.solve(input,(Day11.count_num_occupied_neighbors_2,5))


class Status:
    EMPTY = "L"
    FLOOR = "."
    OCCUPIED = "#"


if __name__ == "__main__":
    Day11().solve_all()
