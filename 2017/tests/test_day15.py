from day15 import Day15
import unittest


class TestDay15(unittest.TestCase):
    def setUp(self) -> None:
        self.input = (65, 8921)

    def test_part1(self) -> None:
        output = 588
        actual = Day15.solve_part1(self.input)
        self.assertEqual(actual, output, f"input={self.input}, expected={output}, actual={actual}")

    def test_part2(self) -> None:
        output = 309
        actual = Day15.solve_part2(self.input)
        self.assertEqual(actual, output, f"input={self.input}, expected={output}, actual={actual}")
