from day07 import Day07
import unittest


class TestDay07(unittest.TestCase):
    def setUp(self):
        self.input = Day07().read_file("tests/test_day07.txt")

    def test_part1(self):
        self.assertEqual(Day07.solve_part1(self.input), 95437)

    def test_part2(self):
        self.assertEqual(Day07.solve_part2(self.input), 24933642)

if __name__ == "__main__":
    unittest.main()
