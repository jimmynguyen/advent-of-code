from day13 import Day13
import unittest


class TestDay13(unittest.TestCase):
    def setUp(self) -> None:
        self.input = Day13().read_file("tests/test_day13.txt")

    def test_part1(self):
        self.assertEqual(Day13.solve_part1(self.input,dst=(7,4)),11)
