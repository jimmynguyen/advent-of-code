from day08 import Day08
import unittest


class TestDay08(unittest.TestCase):
    def test_part1(self):
        input = Day08().read_file("tests/test_day08.1.txt")
        self.assertEqual(Day08.solve_part1(input),14)

    def test_part2_1(self):
        input = Day08().read_file("tests/test_day08.2.1.txt")
        self.assertEqual(Day08.solve_part2(input),9)

    def test_part2_2(self):
        input = Day08().read_file("tests/test_day08.2.2.txt")
        self.assertEqual(Day08.solve_part2(input),34)


if __name__ == "__main__":
    unittest.main()
