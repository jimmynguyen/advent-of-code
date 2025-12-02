from day02.day02 import Day02
import unittest


class TestDay02(unittest.TestCase):
    def test_part1(self):
        input = Day02().read_file("day02/tests/day02.test.txt")
        self.assertEqual(Day02.solve_part1(input), 1227775554)

    def test_part2(self):
        input = Day02().read_file("day02/tests/day02.test.txt")
        self.assertEqual(Day02.solve_part2(input), 4174379265)


if __name__ == "__main__":
    unittest.main()
