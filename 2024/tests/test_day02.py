from day02 import Day02
import unittest


class TestDay02(unittest.TestCase):
    def test_part1(self):
        input = Day02().read_file("tests/test_day02.1.txt")
        self.assertEqual(Day02.solve_part1(input),2)

    def test_part2(self):
        input = Day02().read_file("tests/test_day02.2.txt")
        self.assertEqual(Day02.solve_part2(input),4)

if __name__ == "__main__":
    unittest.main()
