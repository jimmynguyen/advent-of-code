from day04 import Day04
import unittest


class TestDay04(unittest.TestCase):
    def test_part1(self):
        input = Day04().read_file("tests/test_day04.1.txt")
        self.assertEqual(Day04.solve_part1(input),2)

    def test_part2(self):
        input = Day04().read_file("tests/test_day04.2.txt")
        self.assertEqual(Day04.solve_part2(input),4)

if __name__ == "__main__":
    unittest.main()
