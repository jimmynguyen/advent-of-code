from day24 import Day24
import unittest


class TestDay24(unittest.TestCase):
    def setUp(self):
        self.input = Day24().read_file("tests/test_day24.txt")

    def test_part1(self):
        self.assertEqual(Day24.solve_part1(self.input), 31)

    def test_part2(self):
        self.assertEqual(Day24.solve_part2(self.input), 19)

if __name__ == "__main__":
    unittest.main()
