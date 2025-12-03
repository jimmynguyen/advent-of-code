from day13.day13 import Day13
import unittest


class TestDay13(unittest.TestCase):
    def test_part1(self):
        parsed_input = Day13().read_file("day13/tests/day13.test_part1.txt")
        self.assertEqual(Day13.solve_part1(parsed_input), (7, 3))

    def test_part2(self):
        parsed_input = Day13().read_file("day13/tests/day13.test_part2.txt")
        self.assertEqual(Day13.solve_part2(parsed_input), (6, 4))


if __name__ == "__main__":
    unittest.main()
