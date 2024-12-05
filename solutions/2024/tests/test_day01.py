from day01 import Day01
import unittest


class TestDay01(unittest.TestCase):
    def test_part1(self):
        input = Day01().read_file("tests/test_day01.1.txt")
        self.assertEqual(Day01.solve_part1(input),11)

    def test_part2(self):
        input = Day01().read_file("tests/test_day01.2.txt")
        self.assertEqual(Day01.solve_part2(input),31)

if __name__ == "__main__":
    unittest.main()
