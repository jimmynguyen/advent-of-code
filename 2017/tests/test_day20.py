from day20 import Day20
import unittest


class TestDay20(unittest.TestCase):
    def test_part1(self) -> None:
        self.assertEqual(Day20.solve_part1(Day20().read_file("tests/test_day20.1.txt")), 0)

    def test_part2(self) -> None:
        self.assertEqual(Day20.solve_part2(Day20().read_file("tests/test_day20.2.txt")), 1)
