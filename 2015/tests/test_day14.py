from day14 import Day14
import unittest


class TestDay14(unittest.TestCase):
    def setUp(self):
        self.input = Day14().read_file("tests/test_day14.txt")

    def test_part1(self):
        self.assertEqual(Day14.solve(self.input,(Day14.compute_max_score,1000)),1120)

    def test_part2(self):
        self.assertEqual(Day14.solve(self.input,(Day14.compute_max_score_2,1000)),689)
