from day07 import Day07
import unittest


class TestDay07(unittest.TestCase):
    def test_part1(self):
        input = Day07().read_file("tests/test_day07.1.txt")
        self.assertEqual(Day07.solve_part1(input),4)

    def test_part2(self):
        input = Day07().read_file("tests/test_day07.2.txt")
        self.assertEqual(Day07.solve_part2(input),126)
        input = Day07().read_file("tests/test_day07.3.txt")
        self.assertEqual(Day07.solve_part2(input),32)
