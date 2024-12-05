from day14 import Day14
import unittest


class TestDay14(unittest.TestCase):
    def test_part1(self):
        input = Day14().read_file("tests/test_day14.1.txt")
        self.assertEqual(Day14.solve_part1(input),165)

    def test_part2(self):
        input = Day14().read_file("tests/test_day14.2.txt")
        self.assertEqual(Day14.solve_part2(input),208)

if __name__ == "__main__":
    unittest.main()
