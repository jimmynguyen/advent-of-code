from day05.day05 import Day05
import unittest


class TestDay05(unittest.TestCase):
    def test_part1(self):
        input = Day05().read_file("day05/tests/day05.test.txt")
        self.assertEqual(Day05.solve_part1(input), 3)

    def test_part2(self):
        input = Day05().read_file("day05/tests/day05.test.txt")
        self.assertEqual(Day05.solve_part2(input), 14)


if __name__ == "__main__":
    unittest.main()
