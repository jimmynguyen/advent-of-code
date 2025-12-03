from day03.day03 import Day03
import unittest


class TestDay03(unittest.TestCase):
    def test_part1(self):
        input = Day03().read_file("day03/tests/day03.test.txt")
        self.assertEqual(Day03.solve_part1(input), 357)

    def test_part2(self):
        input = Day03().read_file("day03/tests/day03.test.txt")
        self.assertEqual(Day03.solve_part2(input), 3121910778619)


if __name__ == "__main__":
    unittest.main()
