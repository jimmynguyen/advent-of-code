# https://adventofcode.com/2023/day/4
from typing import List
from solutions.challenge import Challenge


class Day04(Challenge):
    def read_file(self, filename: str) -> List[str]:
        return super().read_file(filename)

    @staticmethod
    def get_num_matches(card: str) -> int:
        winning_numbers, numbers = tuple(map(lambda numbers: set(map(lambda x: int(x.strip()), numbers.split())), card.split(":")[1].strip().split(" | ")))
        return len(winning_numbers.intersection(numbers))

    @staticmethod
    def solve_part1(cards: List[str]) -> int:
        result = 0
        for card in cards:
            num_matches = Day04.get_num_matches(card)
            if num_matches > 0:
                result += pow(2, num_matches-1)
        return result

    @staticmethod
    def solve_part2(cards: List[str]) -> int:
        result = 0
        queue = list(range(0, len(cards)))
        cache = {}
        while len(queue) > 0:
            idx_card = queue.pop(0)
            card = cards[idx_card]
            cache[idx_card] = list(range(idx_card + 1, idx_card + Day04.get_num_matches(card) + 1))
            if any(idx == idx_card for idx in queue):
                idx_card_count = 1 + sum(1 if idx == idx_card else 0 for idx in queue)
                queue = [idx for idx in queue if idx != idx_card]
            else:
                idx_card_count = 1
            queue.extend(cache[idx_card] * idx_card_count)
            result += idx_card_count
        return result


if __name__ == "__main__":
    Day04().solve_all()
