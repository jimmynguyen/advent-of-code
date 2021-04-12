from day05 import Day05
import unittest


class TestDay05(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(Day05.solve_part1(Day05().read_file("tests/test_day05.1.txt")),2)

    def test_part2(self):
        self.assertEqual(Day05.solve_part2(Day05().read_file("tests/test_day05.2.txt")),2)
