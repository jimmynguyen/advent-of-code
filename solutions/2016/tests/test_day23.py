from day23 import Day23
import unittest


class TestDay23(unittest.TestCase):
    def setUp(self):
        self.input = Day23().read_file("tests/test_day23.txt")

    def test_part1(self):
        self.assertEqual(Day23.solve_part1(self.input,simplify=False),3)

if __name__ == "__main__":
    unittest.main()
