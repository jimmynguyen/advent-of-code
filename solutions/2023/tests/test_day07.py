from day07 import Day07
import unittest


class TestDay07(unittest.TestCase):
    def test_part1(self):
        input = Day07().read_file("tests/test_day07.1.1.txt")
        self.assertEqual(Day07.solve_part1(input),6440)

    def test_part1_custom1(self):
        input = Day07().read_file("tests/test_day07.1.2.txt")
        self.assertEqual(Day07.solve_part1(input),1343)

    def test_part1_custom2(self):
        input = Day07().read_file("tests/test_day07.1.3.txt")
        self.assertEqual(Day07.solve_part1(input),6592)

    def test_part2(self):
        input = Day07().read_file("tests/test_day07.2.1.txt")
        self.assertEqual(Day07.solve_part2(input),5905)

    def test_part2_custo1(self):
        input = Day07().read_file("tests/test_day07.2.2.txt")
        self.assertEqual(Day07.solve_part2(input),1369)

    def test_part2_custom2(self):
        input = [("QJJJA", 1), ("QQQAA", 1)]
        self.assertEqual(Day07.solve_part2(input),3)

    def test_part2_custom3(self):
        input = Day07().read_file("tests/test_day07.2.3.txt")
        self.assertEqual(Day07.solve_part2(input),6839)


if __name__ == "__main__":
    unittest.main()
