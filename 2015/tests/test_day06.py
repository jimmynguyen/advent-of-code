from day06 import Day06
import unittest


class TestDay06(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(Day06.solve_part1(Day06().read_file("tests/test_day06.1.txt")),998996)

    def test_part2(self):
        self.assertEqual(Day06.solve_part2(Day06().read_file("tests/test_day06.2.txt")),2000000)
