# https://adventofcode.com/2023/day/3
from math import prod
from typing import List
from challenge import Challenge


class Day03(Challenge):
    def read_file(self, filename: str) -> List[str]:
        return super().read_file(filename)

    @staticmethod
    def solve_part1(lines: List[str]) -> int:
        result = 0
        m, n = len(lines), len(lines[0])
        i = 0
        while i < m:
            j = 0
            while j < n:
                if lines[i][j].isnumeric():
                    k = j
                    part_number = lines[i][k]
                    k += 1
                    while k < n and lines[i][k].isnumeric():
                        part_number += lines[i][k]
                        k += 1
                    is_part_number = j > 0 and lines[i][j-1] != "." \
                        or k < n and lines[i][k] != "." \
                        or i > 0 and any(lines[i-1][_j] != "." and not lines[i-1][_j].isnumeric() for _j in range(max(j-1, 0), min(k+1, len(lines[i])))) \
                        or i < m-1 and any(lines[i+1][_j] != "." and not lines[i+1][_j].isnumeric() for _j in range(max(j-1, 0), min(k+1, len(lines[i]))))
                    if is_part_number:
                        result += int(part_number)
                    j = k
                else:
                    j += 1
            i += 1
        return result

    @staticmethod
    def solve_part2(lines: List[str]) -> int:
        result = 0
        m, n = len(lines), len(lines[0])
        i = 0
        while i < m:
            j = 0
            while j < n:
                if lines[i][j] == "*":
                    part_numbers = []
                    if j > 0 and lines[i][j-1].isnumeric():
                        _i = i
                        _j = j-1
                        part_number = lines[_i][_j]
                        _j -= 1
                        while _j >= 0 and lines[_i][_j].isnumeric():
                            part_number = lines[_i][_j] + part_number
                            _j -= 1
                        part_numbers.append(int(part_number))
                    if j < n-1 and lines[i][j+1].isnumeric():
                        _i = i
                        _j = j+1
                        part_number = lines[_i][_j]
                        _j += 1
                        while _j < n and lines[_i][_j].isnumeric():
                            part_number += lines[_i][_j]
                            _j += 1
                        part_numbers.append(int(part_number))
                    if len(part_numbers) <= 2 and i > 0:
                        _i = i-1
                        is_bot_processed = False
                        is_bot_right_processed = False
                        if j > 0 and lines[_i][j-1].isnumeric():
                            _j = j-1
                            part_number = lines[_i][_j]
                            _j -= 1
                            while _j >= 0 and lines[_i][_j].isnumeric():
                                part_number = lines[_i][_j] + part_number
                                _j -= 1
                            _j = j
                            while _j < n and lines[_i][_j].isnumeric():
                                if not is_bot_processed:
                                    is_bot_processed = True
                                if not is_bot_right_processed and _j >= j+1:
                                    is_bot_right_processed = True
                                part_number += lines[_i][_j]
                                _j += 1
                            part_numbers.append(int(part_number))
                        if not is_bot_processed and lines[_i][j].isnumeric():
                            _j = j
                            part_number = lines[_i][_j]
                            _j += 1
                            while _j < n and lines[_i][_j].isnumeric():
                                if not is_bot_right_processed and _j >= j+1:
                                    is_bot_right_processed = True
                                part_number += lines[_i][_j]
                                _j += 1
                            part_numbers.append(int(part_number))
                        if not is_bot_right_processed and j < n-1 and lines[_i][j+1].isnumeric():
                            _j = j+1
                            part_number = lines[_i][_j]
                            _j += 1
                            while _j < n and lines[_i][_j].isnumeric():
                                part_number += lines[_i][_j]
                                _j += 1
                            part_numbers.append(int(part_number))
                    if len(part_numbers) <= 2 and i < m-1:
                        _i = i+1
                        is_bot_processed = False
                        is_bot_right_processed = False
                        if j > 0 and lines[_i][j-1].isnumeric():
                            _j = j-1
                            part_number = lines[_i][_j]
                            _j -= 1
                            while _j >= 0 and lines[_i][_j].isnumeric():
                                part_number = lines[_i][_j] + part_number
                                _j -= 1
                            _j = j
                            while _j < n and lines[_i][_j].isnumeric():
                                if not is_bot_processed:
                                    is_bot_processed = True
                                if not is_bot_right_processed and _j >= j+1:
                                    is_bot_right_processed = True
                                part_number += lines[_i][_j]
                                _j += 1
                            part_numbers.append(int(part_number))
                        if not is_bot_processed and lines[_i][j].isnumeric():
                            _j = j
                            part_number = lines[_i][_j]
                            _j += 1
                            while _j < n and lines[_i][_j].isnumeric():
                                if not is_bot_right_processed and _j >= j+1:
                                    is_bot_right_processed = True
                                part_number += lines[_i][_j]
                                _j += 1
                            part_numbers.append(int(part_number))
                        if not is_bot_right_processed and j < n-1 and lines[_i][j+1].isnumeric():
                            _j = j+1
                            part_number = lines[_i][_j]
                            _j += 1
                            while _j < n and lines[_i][_j].isnumeric():
                                part_number += lines[_i][_j]
                                _j += 1
                            part_numbers.append(int(part_number))
                    if len(part_numbers) == 2:
                        result += prod(part_numbers)
                j += 1
            i += 1
        return result


if __name__ == "__main__":
    Day03().solve_all()
