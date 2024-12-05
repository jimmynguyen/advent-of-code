from day03 import Day03
import unittest


class TestDay03(unittest.TestCase):
    def setUp(self):
        self.input = Day03().read_file("tests/test_day03.txt")

    def test_part1(self):
        self.assertEqual(Day03.solve_part1(self.input),7)

    def test_part2(self):
        self.assertEqual(Day03.solve_part2(self.input),336)

if __name__ == "__main__":
    unittest.main()
