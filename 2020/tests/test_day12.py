from day12 import Day12
import unittest


class TestDay12(unittest.TestCase):
    def setUp(self):
        self.input = Day12().read_file("tests/test_day12.txt")

    def test_part1(self):
        self.assertEqual(Day12.solve_part1(self.input),25)

    def test_part2(self):
        self.assertEqual(Day12.solve_part2(self.input),286)
