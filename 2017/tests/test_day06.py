from day06 import Day06
import unittest


class TestDay06(unittest.TestCase):
    def test_part1(self):
        input = [0,2,7,0]
        self.assertEqual(Day06.solve_part1(input),5)

    def test_part2(self):
        input = [0,2,7,0]
        self.assertEqual(Day06.solve_part2(input),4)
