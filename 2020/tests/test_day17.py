from day17 import Day17
import unittest


class TestDay17(unittest.TestCase):
    def setUp(self):
        self.input = Day17().read_file("tests/test_day17.txt")

    def test_part1(self):
        self.assertEqual(Day17.solve_part1(self.input),112)

    def test_part2(self):
        self.assertEqual(Day17.solve_part2(self.input),848)
