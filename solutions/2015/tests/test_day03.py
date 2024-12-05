from day03 import Day03
import unittest


class TestDay03(unittest.TestCase):
    def test_part1(self):
        inputs = [">","^>v<","^v^v^v^v^v"]
        outputs = [2,4,2]
        for input,output in zip(inputs,outputs):
            self.assertEqual(Day03.solve_part1(input),output)

    def test_part2(self):
        inputs = ["^v","^>v<","^v^v^v^v^v"]
        outputs = [3,3,11]
        for input,output in zip(inputs,outputs):
            self.assertEqual(Day03.solve_part2(input),output)

if __name__ == "__main__":
    unittest.main()
