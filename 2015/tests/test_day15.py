from day15 import Day15
import unittest


class TestDay15(unittest.TestCase):
    def setUp(self):
        self.input = Day15().read_file("tests/test_day15.txt")

    def test_part1(self):
        self.assertEqual(Day15.solve_part1(self.input),62842880)

    def test_part2(self):
        self.assertEqual(Day15.solve_part2(self.input),57600000)
