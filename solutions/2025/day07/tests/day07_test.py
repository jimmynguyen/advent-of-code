from day07.day07 import Day07
import unittest


class TestDay07(unittest.TestCase):
    def test_part1(self):
        input = Day07().read_file("day07/tests/day07.test.txt")
        self.assertEqual(Day07.solve_part1(input), 21)

    def test_part2(self):
        input = Day07().read_file("day07/tests/day07.test.txt")
        self.assertEqual(Day07.solve_part2(input), 40)


if __name__ == "__main__":
    unittest.main()
