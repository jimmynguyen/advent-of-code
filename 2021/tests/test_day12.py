from day12 import Day12
import unittest


class TestDay12(unittest.TestCase):
    def setUp(self):
        self.inputs = [Day12().read_file(f"tests/test_day12.{i + 1}.txt") for i in range(3)]

    def test_part1(self):
        for input, output in zip(self.inputs, [10, 19, 226]):
            self.assertEqual(Day12.solve_part1(input), output)

    def test_part2(self):
        for input, output in zip(self.inputs, [36, 103, 3509]):
            self.assertEqual(Day12.solve_part2(input), output)

if __name__ == "__main__":
    unittest.main()
