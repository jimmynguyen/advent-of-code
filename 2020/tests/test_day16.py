from day16 import Day16
import unittest


class TestDay16(unittest.TestCase):
    def test_part1(self):
        input = Day16().read_file("tests/test_day16.1.txt")
        self.assertEqual(Day16.solve_part1(input),71)

    def test_part2(self):
        input = Day16().read_file("tests/test_day16.2.txt")
        self.assertEqual(Day16.solve_part2(input),1716)

if __name__ == "__main__":
    unittest.main()
