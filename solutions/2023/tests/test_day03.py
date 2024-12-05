from day03 import Day03
import unittest


class TestDay03(unittest.TestCase):
    def test_part1(self):
        input = Day03().read_file("tests/test_day03.1.txt")
        self.assertEqual(Day03.solve_part1(input),4361)

    def test_part2(self):
        input = Day03().read_file("tests/test_day03.2.txt")
        self.assertEqual(Day03.solve_part2(input),467835)

    def test_part2_custom(self):
        input = Day03().read_file("tests/test_day03.3.txt")
        self.assertEqual(Day03.solve_part2(input),20405)


if __name__ == "__main__":
    unittest.main()
