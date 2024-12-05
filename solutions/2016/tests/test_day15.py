from day15 import Day15
import unittest


class TestDay15(unittest.TestCase):
    def setUp(self) -> None:
        self.input = Day15().read_file("tests/test_day15.txt")

    def test_part1(self):
        self.assertEqual(Day15.solve_part1(self.input),5)

if __name__ == "__main__":
    unittest.main()
