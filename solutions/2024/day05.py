# https://adventofcode.com/2024/day/5
from typing import List, Tuple
from solutions.challenge import Challenge


class Day05(Challenge):
    def read_file(self, filename: str) -> Tuple[List[str], List[str]]:
        rules, updates = [x.split("\n") for x in super().read_file(filename, delimiter="\n\n")]
        return rules, updates

    @staticmethod
    def is_valid(pages: List[str], rules: List[str]) -> bool:
        valid = True
        for rule in rules:
            page_before, page_after = rule.split("|")
            if page_before in pages and page_after in pages:
                page_before_idx = pages.index(page_before)
                page_after_idx = pages.index(page_after)
                if page_after_idx < page_before_idx:
                    valid = False
                    break
        return valid

    @staticmethod
    def solve_part1(input: Tuple[List[str], List[str]]) -> int:
        rules, updates = input
        result = 0
        for update in updates:
            pages = update.split(",")
            if Day05.is_valid(pages, rules):
                result += int(pages[len(pages)//2])
        return result

    @staticmethod
    def solve_part2(input: Tuple[List[str], List[str]]) -> int:
        rules, updates = input
        invalid_updates = []
        for update in updates:
            pages = update.split(",")
            if not Day05.is_valid(pages, rules):
                invalid_updates.append(pages)
        result = 0
        for pages in invalid_updates:
            i = 1
            while i <= len(pages):
                if not Day05.is_valid(pages[:i], rules):
                    j = i
                    while not Day05.is_valid(pages[:i], rules):
                        page = pages.pop(j-1)
                        pages.insert(j-2, page)
                        j -= 1
                i += 1
            result += int(pages[len(pages)//2])
        return result


if __name__ == "__main__":
    Day05().solve_all()
