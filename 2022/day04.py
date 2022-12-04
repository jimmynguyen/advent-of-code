# https://adventofcode.com/2022/day/4
from typing import Callable, List, Set, Tuple
from challenge import Challenge


class Day04(Challenge):
    def read_file(self, filename: str) -> List[Tuple[Set[int], Set[int]]]:
        assignment_pairs = []
        for line in super().read_file(filename):
            assignment_pair = tuple()
            for assignment in line.split(","):
                start, end = tuple(map(int, assignment.split("-")))
                assignment_pair += (set(range(start, end + 1)),)
            assignment_pairs.append(assignment_pair)
        return assignment_pairs

    @staticmethod
    def solve(assignment_pairs: List[Tuple[Set[int], Set[int]]], should_count: Callable[[Tuple[Set[int], Set[int]]], bool]) -> int:
        count = 0
        for assignment_pair in assignment_pairs:
            if should_count(assignment_pair):
                count += 1
        return count

    @staticmethod
    def solve_part1(assignment_pairs: List[Tuple[Set[int], Set[int]]]) -> int:
        return Day04.solve(assignment_pairs, lambda assignment_pair: assignment_pair[0].issubset(assignment_pair[1]) or assignment_pair[1].issubset(assignment_pair[0]))

    @staticmethod
    def solve_part2(assignment_pairs: List[Tuple[Set[int], Set[int]]]) -> int:
        return Day04.solve(assignment_pairs, lambda assignment_pair: len(assignment_pair[0].intersection(assignment_pair[1])) > 0)


if __name__ == "__main__":
    Day04().solve_all()
