from day09 import Day09
import unittest


class TestDay09(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(Day09.solve_part1(Day09().read_file("tests/test_day09.1.txt")), 13)

    def test_part2(self):
        self.assertEqual(Day09.solve_part2(Day09().read_file("tests/test_day09.1.txt")), 1)

    def test_part3(self):
        self.assertEqual(Day09.solve_part2(Day09().read_file("tests/test_day09.2.txt")), 36)

if __name__ == "__main__":
    unittest.main()
