from day06.day06 import Day06
import unittest


class TestDay06(unittest.TestCase):
    def test_part1(self):
        input = Day06().read_file("day06/tests/day06.test.txt")
        self.assertEqual(Day06.solve_part1(input), 4277556)

    def test_part2(self):
        input = Day06().read_file("day06/tests/day06.test.txt")
        self.assertEqual(Day06.solve_part2(input), 3263827)


if __name__ == "__main__":
    unittest.main()
