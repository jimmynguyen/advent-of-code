from day13 import Day13
import unittest


class TestDay13(unittest.TestCase):
    def setUp(self) -> None:
        self.input = Day13().read_file("tests/test_day13.txt")

    def test_part1(self) -> None:
        output = 24
        actual = Day13.solve_part1(self.input)
        self.assertEqual(actual, output, f"input={self.input}, expected={output}, actual={actual}")

    def test_part2(self) -> None:
        output = 10
        actual = Day13.solve_part2(self.input)
        self.assertEqual(actual, output, f"input={self.input}, expected={output}, actual={actual}")
