from day25 import Day25
import unittest


class TestDay25(unittest.TestCase):
    def setUp(self) -> None:
        self.input = Day25().read_file("tests/test_day25.txt")

    def test_part1(self) -> None:
        self.assertEqual(Day25.solve_part1(self.input),12231762)

if __name__ == "__main__":
    unittest.main()
