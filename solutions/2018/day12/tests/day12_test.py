from day12.day12 import Day12
import unittest


class TestDay12(unittest.TestCase):
    def test_part1(self):
        parsed_input = Day12().read_file("day12/tests/day12.test.txt")
        self.assertEqual(Day12.solve_part1(parsed_input), 325)


if __name__ == "__main__":
    unittest.main()
