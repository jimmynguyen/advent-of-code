# https://adventofcode.com/2024/day/6
from typing import List, Set, Tuple
from challenge import Challenge


ParsedChallengeInput = Tuple[List[str], Tuple[int, int]]


def get_next_direction(current_direction: str) -> str:
    return "^>v<"[("^>v<".index(current_direction) + 1) % 4]


def get_visited_nodes(grid: List[str], pos_guard: Tuple[int, int]) -> Tuple[Set[Tuple[int, int, str]], bool]:
    grid = list(grid)
    visited = set()
    is_cycle = True
    while pos_guard + tuple(grid[pos_guard[0]][pos_guard[1]]) not in visited:
        direction = grid[pos_guard[0]][pos_guard[1]]
        visited.add(pos_guard + tuple(direction))
        if direction == "^":
            next_pos = (pos_guard[0]-1, pos_guard[1])
        elif direction == "v":
            next_pos = (pos_guard[0]+1, pos_guard[1])
        elif direction == "<":
            next_pos = (pos_guard[0], pos_guard[1]-1)
        elif direction == ">":
            next_pos = (pos_guard[0], pos_guard[1]+1)
        else:
            raise Exception(f"Illegal state: invalid direction={direction}")

        if next_pos[0] < 0 or next_pos[0] >= len(grid) or next_pos[1] < 0 or next_pos[1] >= len(grid[0]):
            is_cycle = False
            break

        if grid[next_pos[0]][next_pos[1]] == ".":
            grid[next_pos[0]] = grid[next_pos[0]][:next_pos[1]] + direction + grid[next_pos[0]][next_pos[1]+1:]
            grid[pos_guard[0]] = grid[pos_guard[0]][:pos_guard[1]] + "." + grid[pos_guard[0]][pos_guard[1]+1:]
            pos_guard = next_pos
        elif grid[next_pos[0]][next_pos[1]] == "#":
            grid[pos_guard[0]] = grid[pos_guard[0]][:pos_guard[1]] + get_next_direction(direction) + grid[pos_guard[0]][pos_guard[1]+1:]
        else:
            raise Exception(f"Illegal state: invalid next_pos={next_pos}")
    return visited, is_cycle


class Day06(Challenge):
    def read_file(self, filename: str) -> ParsedChallengeInput:
        grid = super().read_file(filename)
        pos_guard = None
        for i, row in enumerate(grid):
            for j, col in enumerate(row):
                if col == "^":
                    pos_guard = (i, j)
            if pos_guard is not None:
                break
        if pos_guard is None:
            raise Exception("Failed to find guard")
        return grid, pos_guard

    @staticmethod
    def solve_part1(input: ParsedChallengeInput) -> int:
        grid, pos_guard = input
        visited, _ = get_visited_nodes(grid, pos_guard)
        return len(set((i, j) for i,j,_ in visited))

    @staticmethod
    def solve_part2(input: ParsedChallengeInput) -> int:
        grid, pos_guard = input
        visited, _ = get_visited_nodes(grid, pos_guard)
        visited = sorted(set((i,j) for i,j,_ in visited if (i,j) != pos_guard))

        cycles = []
        for i,j in visited:
            grid_copy = list(grid)
            grid_copy[i] = grid_copy[i][:j] + "#" + grid_copy[i][j+1:]
            _, is_cycle = get_visited_nodes(grid_copy, pos_guard)
            if is_cycle:
                cycles.append((i,j))

        return len(cycles)


if __name__ == "__main__":
    Day06().solve_all()
