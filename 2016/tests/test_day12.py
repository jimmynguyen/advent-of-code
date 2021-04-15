from day12 import Day12
import unittest


class TestDay12(unittest.TestCase):
    def setUp(self) -> None:
        self.input = Day12().read_file("tests/test_day12.txt")

    def test_part1(self):
        self.assertEqual(Day12.solve_part1(self.input),42)
