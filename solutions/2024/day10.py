# https://adventofcode.com/2024/day/10
from typing import List
from challenge import Challenge


ParsedChallengeInput = List[str]


class Day10(Challenge):
    def read_file(self, filename: str) -> ParsedChallengeInput:
        return super().read_file(filename)

    @staticmethod
    def solve_part1(grid: ParsedChallengeInput) -> int:
        M, N = len(grid), len(grid[0])
        trail_heads = [(i, j) for i, row in enumerate(grid) for j, col in enumerate(row) if col == "0"]
        total_score = 0
        for i, j in trail_heads:
            score = 0
            queue = [(i, j)]
            while len(queue) > 0:
                (i, j) = queue.pop(0)
                if grid[i][j] == "9":
                    score += 1
                    continue
                next_target = str(int(grid[i][j]) + 1)
                for i_offset, j_offset in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    if i+i_offset >= 0 and i+i_offset < M and j+j_offset >= 0 and j+j_offset < N and grid[i+i_offset][j+j_offset] == next_target and (i+i_offset, j+j_offset) not in queue:
                        queue.append((i+i_offset, j+j_offset))
            total_score += score
        return total_score


    @staticmethod
    def solve_part2(grid: ParsedChallengeInput) -> int:
        M, N = len(grid), len(grid[0])
        trail_heads = [(i, j) for i, row in enumerate(grid) for j, col in enumerate(row) if col == "0"]
        total_score = 0
        for i, j in trail_heads:
            score = 0
            queue = [[(i, j)]]
            while len(queue) > 0:
                path = queue.pop(0)
                i, j = path[-1]
                if grid[i][j] == "9":
                    score += 1
                    continue
                next_target = str(int(grid[i][j]) + 1)
                for i_offset, j_offset in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    if i+i_offset >= 0 and i+i_offset < M and j+j_offset >= 0 and j+j_offset < N and grid[i+i_offset][j+j_offset] == next_target and (i+i_offset, j+j_offset) not in path:
                        queue.append(path + [(i+i_offset, j+j_offset)])
            total_score += score
        return total_score


if __name__ == "__main__":
    Day10().solve_all()
