from day18 import Day18
import unittest


class TestDay18(unittest.TestCase):
    def test_part1(self) -> None:
        input = Day18().read_file("tests/test_day18.1.txt")
        output = 4
        actual = Day18.solve_part1(input)
        self.assertEqual(actual, output, f"input={input}, expected={output}, actual={actual}")

    def test_part2(self) -> None:
        input = Day18().read_file("tests/test_day18.2.txt")
        output = 3
        actual = Day18.solve_part2(input)
        self.assertEqual(actual, output, f"input={input}, expected={output}, actual={actual}")
