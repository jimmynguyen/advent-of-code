from day09 import Day09
import unittest


class TestDay09(unittest.TestCase):
    def setUp(self):
        self.input = Day09().read_file("tests/test_day09.txt")

    def test_part1(self):
        self.assertEqual(Day09.solve_part1(self.input), 15)

    def test_part2(self):
        self.assertEqual(Day09.solve_part2(self.input), 1134)

if __name__ == "__main__":
    unittest.main()
