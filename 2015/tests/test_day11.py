from day11 import Day11
import unittest


class TestDay11(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(Day11.solve("abcdefgh",1),"abcdffaa")

    def test_part2(self):
        self.assertEqual(Day11.solve("ghijklmn",1),"ghjaabcc")
