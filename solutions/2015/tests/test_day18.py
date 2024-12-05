from day18 import Day18
import unittest


class TestDay18(unittest.TestCase):
    def setUp(self):
        self.input = Day18().read_file("tests/test_day18.txt")

    def test_part1(self):
        self.assertEqual(Day18.solve(self.input,(4,False)),4)

    def test_part2(self):
        self.assertEqual(Day18.solve(self.input,(5,True)),17)

if __name__ == "__main__":
    unittest.main()
