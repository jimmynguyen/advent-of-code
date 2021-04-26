# https://adventofcode.com/2017/day/12
from challenge import Challenge
from typing import Dict, Sequence, Set


class Day12(Challenge):
    def read_file(self, filename: str) -> Dict[int, Sequence[int]]:
        return {int(x.split(" <-> ")[0]): list(map(int,x.split(" <-> ")[1].split(", "))) for x in super().read_file(filename)}

    @staticmethod
    def explore(adj_mat: Dict[int, Sequence[int]], src: int) -> Set[int]:
        stack = [src]
        visited = set()
        while len(stack) > 0:
            x = stack.pop()
            if x in visited:
                continue
            visited.add(x)
            stack.extend([y for y in adj_mat[x]])
        return visited

    @staticmethod
    def solve_part1(adj_mat: Dict[int, Sequence[int]], src: int=0) -> int:
        return len(Day12.explore(adj_mat, src))

    @staticmethod
    def solve_part2(adj_mat: Dict[int, Sequence[int]]) -> int:
        srcs = [x for x in adj_mat.keys()]
        num_groups = 0
        while len(srcs) > 0:
            src = srcs.pop()
            visited = Day12.explore(adj_mat, src)
            srcs = list(filter(lambda x:x not in visited, srcs))
            num_groups += 1
        return num_groups


if __name__ == "__main__":
    Day12().solve_all()
