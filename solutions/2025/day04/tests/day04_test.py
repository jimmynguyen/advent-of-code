from day04.day04 import Day04
import unittest


class TestDay04(unittest.TestCase):
    def test_part1(self):
        input = Day04().read_file("day04/tests/day04.test.txt")
        self.assertEqual(Day04.solve_part1(input), 13)

    def test_part2(self):
        input = Day04().read_file("day04/tests/day04.test.txt")
        self.assertEqual(Day04.solve_part2(input), 43)


if __name__ == "__main__":
    unittest.main()
