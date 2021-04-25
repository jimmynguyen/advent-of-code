# https://adventofcode.com/2017/day/10
from challenge import Challenge
from math import prod


class Day10(Challenge):
    @staticmethod
    def run_knot_hash(lengths, idx=0, skip_size=0, num_elements=256, num_rounds=1):
        lst = list(range(num_elements))
        for _ in range(num_rounds):
            for length in lengths:
                if length > num_elements:
                    continue
                if idx + length > num_elements:
                    overflow = (idx + length) % num_elements
                    section = lst[idx:] + lst[:overflow]
                    section = section[::-1]
                    lst = section[num_elements - idx:] + lst[overflow:idx] + section[:num_elements - idx]
                else:
                    lst = lst[:idx] + lst[idx:idx + length][::-1] + lst[idx + length:]
                idx = (idx + length + skip_size) % num_elements
                skip_size += 1
        return lst

    @staticmethod
    def solve_part1(sequence, num_elements=256):
        lengths = [int(x) for x in sequence.split(",")]
        lst = Day10.run_knot_hash(lengths, num_elements=num_elements)
        return prod(lst[:2])

    @staticmethod
    def solve_part2(sequence, num_rounds=64):
        lengths = [ord(x) for x in sequence] + [17, 31, 73, 47, 23]
        sparse_hash = Day10.run_knot_hash(lengths, num_rounds=num_rounds)
        dense_hash = ""
        for i in range(0, len(sparse_hash), 16):
            y = sparse_hash[i]
            for x in sparse_hash[i+1:i + 16]:
                y ^= x
            dense_hash += hex(y)[2:] if len(hex(y)[2:]) == 2 else f"0{hex(y)[2:]}"
        return dense_hash


if __name__ == "__main__":
    Day10().solve_all()
