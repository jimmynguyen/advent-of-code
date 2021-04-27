from day14 import Day14
import unittest


class TestDay14(unittest.TestCase):
    def setUp(self) -> None:
        self.input = "flqrgnkx"

    def test_part1(self) -> None:
        output = 8108
        actual = Day14.solve_part1(self.input)
        self.assertEqual(actual, output, f"input={self.input}, expected={output}, actual={actual}")

    def test_part2(self) -> None:
        output = 1242
        actual = Day14.solve_part2(self.input)
        self.assertEqual(actual, output, f"input={self.input}, expected={output}, actual={actual}")
