from day19 import Day19
import unittest


class TestDay19(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(Day19.solve_part1(5),3)

    def test_part2(self):
        self.assertEqual(Day19.solve_part2(5),2)
        self.assertEqual(Day19.solve_part2(6),3)
        self.assertEqual(Day19.solve_part2(7),5)
