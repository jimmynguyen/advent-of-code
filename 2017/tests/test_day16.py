from day16 import Day16
import unittest


class TestDay16(unittest.TestCase):
    def setUp(self) -> None:
        self.input = ["s1", "x3/4", "pe/b"]

    def test_part1(self) -> None:
        output = "baedc"
        actual = Day16.solve_part1(self.input, num_programs=5)
        self.assertEqual(actual, output, f"input={self.input}, expected={output}, actual={actual}")

    def test_part2(self) -> None:
        output = "ceadb"
        actual = Day16.solve_part2(self.input, num_programs=5, num_dances=2)
        self.assertEqual(actual, output, f"input={self.input}, expected={output}, actual={actual}")
