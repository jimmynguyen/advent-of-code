from day07 import Day07
import unittest


class TestDay07(unittest.TestCase):
    def test_part1(self):
        input = Day07().read_file("tests/test_day07.1.txt")
        self.assertEqual(Day07.solve_part1(input),2)

    def test_part2(self):
        input = Day07().read_file("tests/test_day07.2.txt")
        self.assertEqual(Day07.solve_part2(input),3)

if __name__ == "__main__":
    unittest.main()
