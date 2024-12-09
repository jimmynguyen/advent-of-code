from day08 import Day08
import unittest


class TestDay08(unittest.TestCase):
    def test_part1_1(self):
        input = Day08().read_file("tests/test_day08.1.1.txt")
        self.assertEqual(Day08.solve_part1(input),2)

    def test_part1_2(self):
        input = Day08().read_file("tests/test_day08.1.2.txt")
        self.assertEqual(Day08.solve_part1(input),6)

    def test_part2(self):
        input = Day08().read_file("tests/test_day08.2.txt")
        self.assertEqual(Day08.solve_part2(input),6)


if __name__ == "__main__":
    unittest.main()
