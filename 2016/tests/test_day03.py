from day03 import Day03
import unittest


class TestDay03(unittest.TestCase):
    def test_part1(self):
        input = ["5 10 25"]
        output = 0
        self.assertEqual(Day03.solve_part1(input),output)

    def test_part2(self):
        input = ["101 301 501","102 302 502","103 303 503","201 401 601","202 402 602","203 403 603"]
        output = 6
        self.assertEqual(Day03.solve_part2(input),output)
