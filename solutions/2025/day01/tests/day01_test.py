from day01.day01 import Day01
import unittest


class TestDay01(unittest.TestCase):
    def test_part1(self):
        input = Day01().read_file("day01/tests/day01.test.txt")
        self.assertEqual(Day01.solve_part1(input),3)

    def test_part2(self):
        input = Day01().read_file("day01/tests/day01.test.txt")
        self.assertEqual(Day01.solve_part2(input),6)

    def test_part2_2(self):
        input = [1000]
        self.assertEqual(Day01.solve_part2(input),10)

    def test_part2_3(self):
        input = [-68]
        self.assertEqual(Day01.solve_part2(input),1)

    def test_part2_4(self):
        input = [-50]
        self.assertEqual(Day01.solve_part2(input),1)

    def test_part2_5(self):
        input = [-1000]
        self.assertEqual(Day01.solve_part2(input),10)

    def test_part2_6(self):
        input = [-633]
        self.assertEqual(Day01.solve_part2(input,1),7)


if __name__ == "__main__":
    unittest.main()
