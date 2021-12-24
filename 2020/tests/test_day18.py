from day18 import Day18
import unittest


class TestDay18(unittest.TestCase):
    def test_part1(self):
        input = Day18().read_file("tests/test_day18.1.txt")
        self.assertEqual(Day18.solve_part1(input),26335)

    def test_part2(self):
        input = Day18().read_file("tests/test_day18.2.txt")
        self.assertEqual(Day18.solve_part2(input),693942)

if __name__ == "__main__":
    unittest.main()
