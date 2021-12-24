from day04 import Day04
import unittest


class TestDay04(unittest.TestCase):
    def test_part1(self):
        inputs = ["abcdef","pqrstuv"]
        outputs = [609043,1048970]
        for input,output in zip(inputs,outputs):
            self.assertEqual(Day04.solve_part1(input),output)

    def test_part2(self):
        inputs = []
        outputs = []
        for input,output in zip(inputs,outputs):
            self.assertEqual(Day04.solve_part2(input),output)

if __name__ == "__main__":
    unittest.main()
