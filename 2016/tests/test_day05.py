from day05 import Day05
import unittest


class TestDay05(unittest.TestCase):
    def setUp(self) -> None:
        self.input = "abc"

    def test_part1(self):
        self.assertEqual(Day05.solve_part1(self.input),"18f47a30")

    def test_part2(self):
        self.assertEqual(Day05.solve_part2(self.input),"05ace8e3")

if __name__ == "__main__":
    unittest.main()
