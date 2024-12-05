# https://adventofcode.com/2022/day/3
from typing import List
from solutions.challenge import Challenge


class Day03(Challenge):
    def read_file(self, filename: str) -> List[str]:
        return super().read_file(filename)

    @staticmethod
    def compute_priority(item_type: str) -> int:
        if item_type.islower():
            return ord(item_type) - ord('a') + 1
        else:
            return ord(item_type) - ord('A') + 27

    @staticmethod
    def solve_part1(rucksacks: List[str]) -> int:
        rucksacks = [(set(rucksack[:len(rucksack)//2]), set(rucksack[len(rucksack)//2:])) for rucksack in rucksacks]
        total_priority = 0
        for compartment1, compartment2 in rucksacks:
            item_type = list(compartment1.intersection(compartment2))[0]
            total_priority += Day03.compute_priority(item_type)
        return total_priority

    @staticmethod
    def solve_part2(rucksacks: List[str]) -> int:
        rucksack_groups = list(zip(*[iter(map(set, rucksacks))]*3))
        total_priority = 0
        for rucksack1, rucksack2, rucksack3 in rucksack_groups:
            badge_item_type = list(rucksack1.intersection(rucksack2).intersection(rucksack3))[0]
            total_priority += Day03.compute_priority(badge_item_type)
        return total_priority


if __name__ == "__main__":
    Day03().solve_all()
