from day05 import Day05
import unittest


class TestDay05(unittest.TestCase):
    def test_part2(self):
        input = [0,3,0,1,-3]
        self.assertEqual(Day05.solve_part2(input),10)

if __name__ == "__main__":
    unittest.main()
