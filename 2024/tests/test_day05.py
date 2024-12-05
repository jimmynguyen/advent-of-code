from day05 import Day05
import unittest


class TestDay05(unittest.TestCase):
    def test_part1(self):
        input = Day05().read_file("tests/test_day05.1.txt")
        self.assertEqual(Day05.solve_part1(input),143)

    def test_part2(self):
        input = Day05().read_file("tests/test_day05.2.txt")
        self.assertEqual(Day05.solve_part2(input),123)


if __name__ == "__main__":
    unittest.main()
