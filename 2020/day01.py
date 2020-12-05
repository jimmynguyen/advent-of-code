# https://adventofcode.com/2020/day/1
# --- Day 1: Report Repair ---
# After saving Christmas five years in a row, you've decided to take a vacation at a nice resort on a tropical island. Surely, Christmas will go on without you.
# 
# The tropical island has its own currency and is entirely cash-only. The gold coins used there have a little picture of a starfish; the locals just call them stars. None of the currency exchanges seem to have heard of them, but somehow, you'll need to find fifty of these coins by the time you arrive so you can pay the deposit on your room.
# 
# To save your vacation, you need to get all fifty stars by December 25th.
# 
# Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!
# 
# Before you leave, the Elves in accounting just need you to fix your expense report (your puzzle input); apparently, something isn't quite adding up.
# 
# Specifically, they need you to find the two entries that sum to 2020 and then multiply those two numbers together.
# 
# For example, suppose your expense report contained the following:
# 
# 1721
# 979
# 366
# 299
# 675
# 1456
# 
# In this list, the two entries that sum to 2020 are 1721 and 299. Multiplying them together produces 1721 * 299 = 514579, so the correct answer is 514579.
# 
# Of course, your expense report is much larger. Find the two entries that sum to 2020; what do you get if you multiply them together?
from itertools import combinations
from math import prod


def unit_test(nums,n,expected_factors,expected_product):
    factors,product = solve(nums,n)
    return factors == expected_factors and product == expected_product


def unit_test_part1():
    nums = [1721,979,366,299,675,1456]
    n = 2
    expected_factors = [299,1721]
    expected_product = 514579
    return unit_test(nums,n,expected_factors,expected_product)


def unit_test_part2():
    nums = [979,366,675]
    n = 3
    expected_factors = [366,675,979]
    expected_product = 241861950
    return unit_test(nums,n,expected_factors,expected_product)


def get_input(filename):
    with open(filename) as file:
        return list(map(int,file.readlines()))


def solve(nums,n):
    combos = combinations(nums,n)
    for c in combos:
        if sum(c) == 2020:
            return sorted(c),prod(c)
    return None,None


if __name__ == "__main__":
    assert unit_test_part1(),"part 1 unit test failed"
    assert unit_test_part2(),"part 2 unit test failed"
    nums = get_input("day01.txt")
    print("Part 1 answer:",solve(nums,2)[1])
    print("Part 2 answer:",solve(nums,3)[1])