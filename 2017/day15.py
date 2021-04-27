# https://adventofcode.com/2017/day/15
from challenge import Challenge
from typing import Optional, Tuple


class Day15(Challenge):
    def read_file(self, filename) -> Tuple[int, int]:
        return tuple(int(x.split("starts with ")[1]) for x in super().read_file(filename))

    @staticmethod
    def solve_part1(generators_state: Tuple[int, int], n: int=int(4e7), multipliers: Tuple[int, int]=(16807, 48271), criteria: Optional[Tuple[int, int]]=None) -> int:
        num_pairs = 0
        generators_vals = ([], [])
        idx_pair = 0
        while idx_pair < n:
            generators_state = tuple(map(lambda i: (generators_state[i] * multipliers[i]) % 2147483647, range(len(generators_state))))
            for i in range(len(generators_vals)):
                if criteria is None or generators_state[i] % criteria[i] == 0:
                    generators_vals[i].append(generators_state[i])
            if all(len(x) > idx_pair for x in generators_vals):
                binaries = tuple(map(lambda x: bin(x)[-16:].zfill(16), [x[idx_pair] for x in generators_vals]))
                if binaries[0] == binaries[1]:
                    num_pairs += 1
                idx_pair += 1
        return num_pairs

    @staticmethod
    def solve_part2(generators_state: Tuple[int, int], n: int=int(5e6), criteria: Tuple[int, int]=(4,8)) -> int:
        return Day15.solve_part1(generators_state, n=n, criteria=criteria)


if __name__ == "__main__":
    Day15().solve_all()
