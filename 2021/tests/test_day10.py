from day10 import Day10
import unittest


class TestDay10(unittest.TestCase):
    def setUp(self):
        self.input = Day10().read_file("tests/test_day10.txt")

    def test_part1(self):
        self.assertEqual(Day10.solve_part1(self.input), 26397)

    def test_part2(self):
        self.assertEqual(Day10.solve_part2(self.input), 288957)

if __name__ == "__main__":
    unittest.main()
