from day23 import Day23
import unittest


class TestDay23(unittest.TestCase):
    def test_part1(self):
        input = Day23().read_file("tests/test_day23.txt")
        self.assertEqual(Day23.solve_part1(input),0)

if __name__ == "__main__":
    unittest.main()
