from day11 import Day11
import unittest


class TestDay11(unittest.TestCase):
    def setUp(self):
        self.input = Day11().read_file("tests/test_day11.txt")

    def test_part1(self):
        self.assertEqual(Day11.solve_part1(self.input),37)

    def test_part2(self):
        self.assertEqual(Day11.solve_part2(self.input),26)

if __name__ == "__main__":
    unittest.main()
