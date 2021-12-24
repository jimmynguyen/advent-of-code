from day11 import Day11
import unittest


class TestDay11(unittest.TestCase):
    def setUp(self) -> None:
        self.input = Day11().read_file("tests/test_day11.txt")

    def test_part1(self):
        self.assertEqual(Day11.solve_part1(self.input),11)

if __name__ == "__main__":
    unittest.main()
