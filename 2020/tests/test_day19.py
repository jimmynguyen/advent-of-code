from day19 import Day19
import unittest


class TestDay19(unittest.TestCase):
    def test_part1(self):
        input = Day19().read_file("tests/test_day19.1.txt")
        self.assertEqual(Day19.solve_part1(input),2)

    def test_part2(self):
        input = Day19().read_file("tests/test_day19.2.txt")
        self.assertEqual(Day19.solve_part2(input),12)
