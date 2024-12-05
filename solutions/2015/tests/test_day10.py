from day10 import Day10
import unittest


class TestDay10(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(Day10.solve(1,5),6)

if __name__ == "__main__":
    unittest.main()
