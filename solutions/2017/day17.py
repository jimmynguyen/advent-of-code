# https://adventofcode.com/2017/day/17
from solutions.challenge import Challenge
from typing import Optional


class Day17(Challenge):
    @staticmethod
    def solve_part1(num_steps: int, n: int=2017, idx_target: Optional[int]=None) -> int:
        state = [0]
        idx = 0
        output = None
        for x in range(1, n + 1):
            idx = ((num_steps + idx) % x) + 1
            if idx_target is None:
                state.insert(idx, x)
            elif idx == idx_target:
                output = x
        return state[(state.index(n) + 1) % len(state)] if idx_target is None else output

    @staticmethod
    def solve_part2(num_steps: int, n: int=int(5e7)) -> int:
        return Day17.solve_part1(num_steps, n=n, idx_target=1)


if __name__ == "__main__":
    Day17().solve_all(312)
