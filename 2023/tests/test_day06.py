from day06 import Day06
import unittest


class TestDay06(unittest.TestCase):
    def test_part1(self):
        input = Day06().read_file("tests/test_day06.1.txt")
        self.assertEqual(Day06.solve_part1(input),288)

    def test_part2(self):
        input = Day06().read_file("tests/test_day06.2.txt")
        self.assertEqual(Day06.solve_part2(input),71503)


if __name__ == "__main__":
    unittest.main()
