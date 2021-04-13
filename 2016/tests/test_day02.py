from day02 import Day02
import unittest


class TestDay02(unittest.TestCase):
    def test_part1(self):
        input = ["ULL","RRDDD","LURDL","UUUUD"]
        output = "1985"
        self.assertEqual(Day02.solve_part1(input),output)

    def test_part2(self):
        input = ["ULL","RRDDD","LURDL","UUUUD"]
        output = "5DB3"
        self.assertEqual(Day02.solve_part2(input),output)
