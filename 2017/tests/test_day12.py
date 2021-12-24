from day12 import Day12
import unittest


class TestDay12(unittest.TestCase):
    def setUp(self) -> None:
        self.input = Day12().read_file("tests/test_day12.txt")

    def test_part1(self) -> None:
        output = 6
        actual = Day12.solve_part1(self.input)
        self.assertEqual(actual, output, f"input={self.input}, expected={output}, actual={actual}")

    def test_part2(self) -> None:
        output = 2
        actual = Day12.solve_part2(self.input)
        self.assertEqual(actual, output, f"input={self.input}, expected={output}, actual={actual}")

if __name__ == "__main__":
    unittest.main()
