from day06 import Day06
import unittest


class TestDay06(unittest.TestCase):
    def setUp(self):
        self.input = Day06().read_file("tests/test_day06.txt")

    def test_part1(self):
        self.assertEqual(Day06.solve_part1(self.input), 5934)

    def test_part2(self):
        self.assertEqual(Day06.solve_part2(self.input), 26984457539)

if __name__ == "__main__":
    unittest.main()
