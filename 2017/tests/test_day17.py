from day17 import Day17
import unittest


class TestDay17(unittest.TestCase):
    def setUp(self) -> None:
        self.input = 3

    def test_part1(self) -> None:
        output = 638
        actual = Day17.solve_part1(self.input)
        self.assertEqual(actual, output, f"input={self.input}, expected={output}, actual={actual}")
