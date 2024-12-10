from day10 import Day10
import unittest


class TestDay10(unittest.TestCase):
    def test_part1_1(self):
        input = Day10().read_file("tests/test_day10.1.1.txt")
        self.assertEqual(Day10.solve_part1(input),1)

    def test_part1_2(self):
        input = Day10().read_file("tests/test_day10.1.2.txt")
        self.assertEqual(Day10.solve_part1(input),2)

    def test_part1_3(self):
        input = Day10().read_file("tests/test_day10.1.3.txt")
        self.assertEqual(Day10.solve_part1(input),4)

    def test_part1_4(self):
        input = Day10().read_file("tests/test_day10.1.4.txt")
        self.assertEqual(Day10.solve_part1(input),3)

    def test_part1_5(self):
        input = Day10().read_file("tests/test_day10.1.5.txt")
        self.assertEqual(Day10.solve_part1(input),36)

    def test_part2_1(self):
        input = Day10().read_file("tests/test_day10.2.1.txt")
        self.assertEqual(Day10.solve_part2(input),3)

    def test_part2_2(self):
        input = Day10().read_file("tests/test_day10.2.2.txt")
        self.assertEqual(Day10.solve_part2(input),13)

    def test_part2_3(self):
        input = Day10().read_file("tests/test_day10.2.3.txt")
        self.assertEqual(Day10.solve_part2(input),227)

    def test_part2_4(self):
        input = Day10().read_file("tests/test_day10.2.4.txt")
        self.assertEqual(Day10.solve_part2(input),81)


if __name__ == "__main__":
    unittest.main()
