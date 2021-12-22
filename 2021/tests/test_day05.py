from day05 import Day05
import unittest


class TestDay05(unittest.TestCase):
    def setUp(self):
        self.input = Day05().read_file("tests/test_day05.txt")

    def test_part1(self):
        self.assertEqual(Day05.solve_part1(self.input), 5)

    def test_part2(self):
        self.assertEqual(Day05.solve_part2(self.input), 12)
