from day01 import Day01
import unittest


class TestDay01(unittest.TestCase):
    def setUp(self):
        self.input = Day01().read_file("tests/test_day01.txt")

    def test_part1(self):
        self.assertEqual(Day01.solve_part1(self.input),514579)

    def test_part2(self):
        self.assertEqual(Day01.solve_part2(self.input),241861950)

if __name__ == "__main__":
    unittest.main()
