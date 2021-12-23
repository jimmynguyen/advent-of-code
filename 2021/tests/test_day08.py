from day08 import Day08
import unittest


class TestDay08(unittest.TestCase):
    def setUp(self):
        self.input = Day08().read_file("tests/test_day08.txt")

    def test_part1(self):
        self.assertEqual(Day08.solve_part1(self.input), 26)

    def test_part2(self):
        self.assertEqual(Day08.solve_part2(self.input), 61229)
