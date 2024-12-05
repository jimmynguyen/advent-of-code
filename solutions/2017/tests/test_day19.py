from day19 import Day19
import unittest


class TestDay19(unittest.TestCase):
    def setUp(self) -> None:
        self.input = Day19().read_file("tests/test_day19.txt")

    def test_part1(self) -> None:
        output = "ABCDEF"
        actual = Day19.solve_part1(self.input)
        self.assertEqual(actual, output, f"input={self.input}, expected={output}, actual={actual}")

    def test_part2(self) -> None:
        output = 38
        actual = Day19.solve_part2(self.input)
        self.assertEqual(actual, output, f"input={self.input}, expected={output}, actual={actual}")
