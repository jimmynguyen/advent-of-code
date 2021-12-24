from day21 import Day21
import unittest


class TestDay21(unittest.TestCase):
    def setUp(self):
        self.input = Day21().read_file("tests/test_day21.txt")

    def test_part1(self):
        self.assertEqual(Day21.solve_part1(self.input,"abcde"),"decab")

    def test_part2(self):
        self.assertEqual(Day21.solve_part2(self.input,"decab"),"abcde")

if __name__ == "__main__":
    unittest.main()
