# https://adventofcode.com/2023/day/5
import sys
from typing import List, Tuple
from challenge import Challenge


class AlmanacMap:
    def __init__(self, lines: List[str]) -> None:
        self.src_type, self.dst_type = tuple(lines[0][:-len(" map:")].split("-")[::2])
        self.entries = sorted(
            [tuple(map(int, line.split())) for line in lines[1:]],
            key=lambda x: x[1]
        )

    def lookup(self, keys: List[int]) -> List[int]:
        values = []
        for key in keys:
            value = None
            for dst, src_min, src_len in self.entries:
                if src_min <= key and key < src_min + src_len:
                    value = dst + key - src_min
                    break
            values.append(key if value is None else value)
        return values

    def lookup_ranges(self, key_ranges: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
        value_ranges = []
        for key_min, key_len in key_ranges:
            key = key_min
            while key < key_min + key_len:
                key_upper_limit = sys.maxsize
                value_min = None
                for dst, src_min, src_len in self.entries:
                    if src_min <= key and key < src_min + src_len:
                        value_min = dst + key - src_min
                        value_len = min(src_min + src_len - key, key_min + key_len - key)
                        break
                    if key < src_min:
                        key_upper_limit = min(key_upper_limit, src_min)
                if value_min is None:
                    value_min = key
                    value_len = min(key_upper_limit - key, key_min + key_len - key)
                value_ranges.append((value_min, value_len))
                key += value_len
        return value_ranges


class Day05(Challenge):
    def read_file(self, filename: str) -> Tuple[List[int], List[AlmanacMap]]:
        lines = super().read_file(filename, delimiter="\n\n")
        seeds = list(map(int, lines[0][len("seeds: "):].split()))
        almanac = [AlmanacMap(line.split("\n")) for line in lines[1:]]
        return seeds, almanac

    @staticmethod
    def solve_part1(input: Tuple[List[int], List[AlmanacMap]]) -> int:
        seeds, almanac = input
        keys = list(seeds)
        for almanac_map in almanac:
            values = almanac_map.lookup(keys)
            keys = values
        return min(keys)

    @staticmethod
    def solve_part2(input: Tuple[List[int], List[AlmanacMap]]) -> int:
        seed_ranges, almanac = input
        key_ranges = list(zip(seed_ranges[::2], seed_ranges[1::2]))
        for almanac_map in almanac:
            value_ranges = almanac_map.lookup_ranges(key_ranges)
            key_ranges = value_ranges
        return min(key_ranges, key=lambda x: x[0])[0]


if __name__ == "__main__":
    Day05().solve_all()
