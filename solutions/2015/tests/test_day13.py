from day13 import Day13
import unittest


class TestDay13(unittest.TestCase):
    def setUp(self):
        self.input = Day13().read_file("tests/test_day13.txt")

    def test_part1(self):
        self.assertEqual(Day13.solve_part1(self.input),330)

if __name__ == "__main__":
    unittest.main()
