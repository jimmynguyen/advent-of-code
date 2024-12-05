# https://adventofcode.com/2024/day/4
from typing import List
from solutions.challenge import Challenge


class Day04(Challenge):
    def read_file(self, filename: str) -> str:
        return super().read_file(filename)

    @staticmethod
    def solve_part1(lines: List[str]) -> int:
        m, n = len(lines), len(lines[0])
        search = "XMAS"
        result = 0
        i = 0
        while i < m:
            j = 0
            while j < n:
                if lines[i][j] == search[0]:
                    # top, left
                    idx_search = 1
                    k = i - 1
                    l = j - 1
                    while k >= 0 and l >= 0 and idx_search < len(search) and lines[k][l] == search[idx_search]:
                        k -= 1
                        l -= 1
                        idx_search += 1
                    if idx_search == len(search):
                        result += 1
                    # top
                    idx_search = 1
                    k = i - 1
                    while k >= 0 and idx_search < len(search) and lines[k][j] == search[idx_search]:
                        k -= 1
                        idx_search += 1
                    if idx_search == len(search):
                        result += 1
                    # top, right
                    idx_search = 1
                    k = i - 1
                    l = j + 1
                    while k >= 0 and l < n and idx_search < len(search) and lines[k][l] == search[idx_search]:
                        k -= 1
                        l += 1
                        idx_search += 1
                    if idx_search == len(search):
                        result += 1
                    # left
                    idx_search = 1
                    l = j - 1
                    while l >= 0 and idx_search < len(search) and lines[i][l] == search[idx_search]:
                        l -= 1
                        idx_search += 1
                    if idx_search == len(search):
                        result += 1
                    # right
                    idx_search = 1
                    l = j + 1
                    while l < n and idx_search < len(search) and lines[i][l] == search[idx_search]:
                        l += 1
                        idx_search += 1
                    if idx_search == len(search):
                        result += 1
                    # bot, right
                    idx_search = 1
                    k = i + 1
                    l = j + 1
                    while k < m and l < n and idx_search < len(search) and lines[k][l] == search[idx_search]:
                        k += 1
                        l += 1
                        idx_search += 1
                    if idx_search == len(search):
                        result += 1
                    # bot
                    idx_search = 1
                    k = i + 1
                    while k < m and idx_search < len(search) and lines[k][j] == search[idx_search]:
                        k += 1
                        idx_search += 1
                    if idx_search == len(search):
                        result += 1
                    # bot, left
                    idx_search = 1
                    k = i + 1
                    l = j - 1
                    while k < m and l >= 0 and idx_search < len(search) and lines[k][l] == search[idx_search]:
                        k += 1
                        l -= 1
                        idx_search += 1
                    if idx_search == len(search):
                        result += 1
                j += 1
            i += 1
        return result

    @staticmethod
    def solve_part2(lines: List[str]) -> int:
        m, n = len(lines), len(lines[0])
        result = 0
        i = 0
        while i < m:
            j = 0
            while j < n:
                if lines[i][j] == "A":
                    # top left, top right, bot left, bot right
                    if i > 0 and j > 0 and lines[i-1][j-1] == "M" \
                        and i > 0 and j < n-1 and lines[i-1][j+1] == "S" \
                        and i < m-1 and j > 0 and lines[i+1][j-1] == "M" \
                        and i < m-1 and j < n-1 and lines[i+1][j+1] == "S":
                        result += 1
                    # top left, top right, bot left, bot right
                    if i > 0 and j > 0 and lines[i-1][j-1] == "M" \
                        and i > 0 and j < n-1 and lines[i-1][j+1] == "M" \
                        and i < m-1 and j > 0 and lines[i+1][j-1] == "S" \
                        and i < m-1 and j < n-1 and lines[i+1][j+1] == "S":
                        result += 1
                    # top left, top right, bot left, bot right
                    if i > 0 and j > 0 and lines[i-1][j-1] == "S" \
                        and i > 0 and j < n-1 and lines[i-1][j+1] == "M" \
                        and i < m-1 and j > 0 and lines[i+1][j-1] == "S" \
                        and i < m-1 and j < n-1 and lines[i+1][j+1] == "M":
                        result += 1
                    # top left, top right, bot left, bot right
                    if i > 0 and j > 0 and lines[i-1][j-1] == "S" \
                        and i > 0 and j < n-1 and lines[i-1][j+1] == "S" \
                        and i < m-1 and j > 0 and lines[i+1][j-1] == "M" \
                        and i < m-1 and j < n-1 and lines[i+1][j+1] == "M":
                        result += 1
                j += 1
            i += 1
        return result


if __name__ == "__main__":
    Day04().solve_all()
