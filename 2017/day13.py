# https://adventofcode.com/2017/day/13
from challenge import Challenge
from typing import Dict


class Day13(Challenge):
    def read_file(self, filename: str) -> Dict[int, int]:
        return {int(x.split(": ")[0]): int(x.split(": ")[1]) for x in super().read_file(filename)}

    @staticmethod
    def solve_part1(firewall: Dict[int, int], delay: int = 0) -> int:
        severity = 0
        for t in range(max(firewall.keys())+1):
            if t in firewall:
                x = list(range(firewall[t]))
                x += x[-2:0:-1]
                if x[(t + delay) % len(x)] == 0:
                    if delay > 0:
                        return 1
                    severity += t * firewall[t]
        return severity

    @staticmethod
    def solve_part2(firewall: Dict[int, int]) -> int:
        delay = 0
        while Day13.solve_part1(firewall, delay) > 0:
            delay += 1
        return delay


if __name__ == "__main__":
    Day13().solve_all()
