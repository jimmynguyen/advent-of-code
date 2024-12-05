from day03 import Day03
import unittest


class TestDay03(unittest.TestCase):
    def test_part1(self):
        input = Day03().read_file("tests/test_day03.1.txt")
        self.assertEqual(Day03.solve_part1(input),161)

    def test_part2(self):
        input = Day03().read_file("tests/test_day03.2.txt")
        self.assertEqual(Day03.solve_part2(input),48)


if __name__ == "__main__":
    unittest.main()
