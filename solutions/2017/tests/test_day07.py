from day07 import Day07
import unittest


class TestDay07(unittest.TestCase):
    def setUp(self) -> None:
        self.input = Day07().read_file("tests/test_day07.txt")

    def test_part1(self):
        self.assertEqual(Day07.solve_part1(self.input),"tknk")

    def test_part2(self):
        self.assertEqual(Day07.solve_part2(self.input),60)

if __name__ == "__main__":
    unittest.main()
