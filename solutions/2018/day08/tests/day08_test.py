from day08.day08 import Day08
import unittest


class TestDay08(unittest.TestCase):
    def test_part1(self):
        input = Day08().read_file("day08/tests/day08.test.txt")
        self.assertEqual(Day08.solve_part1(input), 138)

    def test_part2(self):
        input = Day08().read_file("day08/tests/day08.test.txt")
        self.assertEqual(Day08.solve_part2(input), 66)

if __name__ == "__main__":
    unittest.main()
