from dayXX import DayXX
import unittest


class TestDayXX(unittest.TestCase):
    def setUp(self):
        self.input = DayXX().read_file("tests/test_dayXX.txt")

    def test_part1(self):
        self.assertEqual(DayXX.solve_part1(self.input), None)

    def test_part2(self):
        self.assertEqual(DayXX.solve_part2(self.input), None)

if __name__ == "__main__":
    unittest.main()
