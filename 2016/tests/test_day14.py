from day14 import Day14
import unittest


class TestDay14(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(Day14.solve_part1("abc"),22728)

    def test_part2(self):
        self.assertEqual(Day14.solve_part2("abc"),22551)
