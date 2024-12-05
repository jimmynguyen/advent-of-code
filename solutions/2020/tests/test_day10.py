from day10 import Day10
import unittest


class TestDay10(unittest.TestCase):
    def test_part1(self):
        input = Day10().read_file("tests/test_day10.1.txt")
        self.assertEqual(Day10.solve_part1(input),35)
        input = Day10().read_file("tests/test_day10.2.txt")
        self.assertEqual(Day10.solve_part1(input),220)

    def test_part2(self):
        input = Day10().read_file("tests/test_day10.3.txt")
        self.assertEqual(Day10.solve_part2(input),8)
        input = Day10().read_file("tests/test_day10.4.txt")
        self.assertEqual(Day10.solve_part2(input),19208)

if __name__ == "__main__":
    unittest.main()
