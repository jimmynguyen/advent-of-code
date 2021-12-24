from day20 import Day20
import unittest


class TestDay20(unittest.TestCase):
    def setUp(self):
        self.input = Day20().read_file("tests/test_day20.txt")

    def test_part1(self):
        self.assertEqual(Day20.solve_part1(self.input),3)

    def test_part2(self):
        self.assertEqual(Day20.solve_part2(self.input,10),2)

if __name__ == "__main__":
    unittest.main()
