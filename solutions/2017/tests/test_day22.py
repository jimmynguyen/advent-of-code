from day22 import Day22
import unittest


class TestDay22(unittest.TestCase):
    def setUp(self):
        self.input = Day22().read_file("tests/test_day22.txt")

    def test_part1(self):
        self.assertEqual(Day22.solve_part1(self.input), 5587)

    def test_part2(self):
        self.assertEqual(Day22.solve_part2(self.input), 2511944)

if __name__ == "__main__":
    unittest.main()
