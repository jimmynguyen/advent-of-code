from day02 import Day02
import unittest


class TestDay02(unittest.TestCase):
    def setUp(self):
        self.input = Day02().read_file("tests/test_day02.txt")

    def test_part1(self):
        self.assertEqual(Day02.solve_part1(self.input),101)

    def test_part2(self):
        self.assertEqual(Day02.solve_part2(self.input),48)
