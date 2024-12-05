from day04 import Day04
import unittest


class TestDay04(unittest.TestCase):
    def setUp(self):
        self.input = Day04().read_file("tests/test_day04.txt")

    def test_part1(self):
        self.assertEqual(Day04.solve_part1(self.input), 2)

    def test_part2(self):
        self.assertEqual(Day04.solve_part2(self.input), 4)

if __name__ == "__main__":
    unittest.main()
