from day07 import Day07
import unittest


class TestDay07(unittest.TestCase):
    def setUp(self):
        self.input = Day07().read_file("tests/test_day07.txt")

    def test_part1(self):
        self.assertEqual(Day07.solve_part1(self.input),72)
