from day09 import Day09
import unittest


class TestDay09(unittest.TestCase):
    def test_part1(self):
        input = Day09().read_file("tests/test_day09.1.txt")
        self.assertEqual(Day09.solve_part1(input),1928)

    def test_part2(self):
        input = Day09().read_file("tests/test_day09.2.txt")
        self.assertEqual(Day09.solve_part2(input),2858)


if __name__ == "__main__":
    unittest.main()
