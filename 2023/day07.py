# https://adventofcode.com/2023/day/7
from enum import Enum
from typing import List, Tuple
from challenge import Challenge
from collections import Counter
from functools import cmp_to_key


ParsedChallengeInput = List[Tuple[str, int]]


PART1_CARD_ORDER = "23456789TJQKA"
PART2_CARD_ORDER = "J23456789TQKA"


class HandType(Enum):
    HIGH_CARD = 1
    ONE_PAIR = 2
    TWO_PAIR = 3
    THREE_OF_A_KIND = 4
    FULL_HOUSE = 5
    FOUR_OF_A_KIND = 6
    FIVE_OF_A_KIND = 7


def is_sublist(lst: List[str], sub_lst: List[str]) -> bool:
    lst_copy = list(lst)
    for item in sub_lst:
        try:
            lst_copy.remove(item)
        except ValueError:
            return False
    return True


def get_hand_type(hand: str, handle_joker: bool) -> HandType:
    has_joker = "J" in hand
    card_counts = Counter(hand).most_common()
    counts = [count for _, count in card_counts]
    if 5 in counts:
        return HandType.FIVE_OF_A_KIND
    if 4 in counts:
        if not handle_joker or not has_joker:
            return HandType.FOUR_OF_A_KIND
        return HandType.FIVE_OF_A_KIND
    if is_sublist(counts, [2, 3]):
        if not handle_joker or not has_joker:
            return HandType.FULL_HOUSE
        return HandType.FIVE_OF_A_KIND
    if is_sublist(counts, [1, 1, 3]):
        if not handle_joker or not has_joker:
            return HandType.THREE_OF_A_KIND
        return HandType.FOUR_OF_A_KIND
    if is_sublist(counts, [1, 2, 2]):
        if not handle_joker or not has_joker:
            return HandType.TWO_PAIR
        if card_counts[0][0] == "J" or card_counts[1][0] == "J":
            return HandType.FOUR_OF_A_KIND
        if card_counts[2][0] == "J":
            return HandType.FULL_HOUSE
        raise Exception("Invalid state")
    if 2 in counts:
        if not handle_joker or not has_joker:
            return HandType.ONE_PAIR
        return HandType.THREE_OF_A_KIND
    if not handle_joker or not has_joker:
        return HandType.HIGH_CARD
    return HandType.ONE_PAIR


def compare_hands(
    hand1: str,
    hand2: str,
    handle_joker: bool = False,
    card_order: str = PART1_CARD_ORDER,
) -> int:
    hand1_type, hand2_type = get_hand_type(hand1, handle_joker), get_hand_type(hand2, handle_joker)
    if hand1_type != hand2_type:
        return hand1_type.value - hand2_type.value
    for card1, card2 in zip(hand1, hand2):
        result = compare_card(card1, card2, card_order)
        if result != 0:
            return result
    return 0


def compare_card(card1: str, card2: str, card_order: str) -> int:
    card1_order = card_order.index(card1)
    card2_order = card_order.index(card2)
    if card1_order == -1 or card2_order == -1:
        raise Exception("Illegal state")
    return card1_order - card2_order


class Day07(Challenge):
    def read_file(self, filename: str) -> ParsedChallengeInput:
        return [
            (hand, int(bid))
            for hand, bid in [
                line.split()
                for line in super().read_file(filename)
            ]
        ]

    @staticmethod
    def solve_part1(hands: ParsedChallengeInput) -> int:
        ranked_hands = sorted(hands, key=cmp_to_key(lambda hand1, hand2: compare_hands(hand1[0], hand2[0])))
        result = 0
        for rank, (_, bid) in enumerate(ranked_hands):
            result += (rank + 1) * bid
        return result

    @staticmethod
    def solve_part2(hands: ParsedChallengeInput) -> int:
        ranked_hands = sorted(hands, key=cmp_to_key(lambda hand1, hand2: compare_hands(hand1[0], hand2[0], handle_joker=True, card_order=PART2_CARD_ORDER)))
        result = 0
        for rank, (_, bid) in enumerate(ranked_hands):
            result += (rank + 1) * bid
        return result


if __name__ == "__main__":
    Day07().solve_all()
