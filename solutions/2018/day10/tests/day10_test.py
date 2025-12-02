from day10.day10 import Day10
import unittest


class TestDay10(unittest.TestCase):
    def test_part1(self):
        input = Day10().read_file("day10/tests/day10.test.txt")
        self.assertEqual(Day10.solve_part1(input, figsize=(2, 1.3)), "HI")

    def test_part2(self):
        input = Day10().read_file("day10/tests/day10.test.txt")
        self.assertEqual(Day10.solve_part2(input, figsize=(2, 1.3)), 3)


if __name__ == "__main__":
    unittest.main()
