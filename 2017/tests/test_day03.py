from day03 import Day03
import unittest


class TestDay03(unittest.TestCase):
    def test_part1(self):
        inputs = [1,12,23,1024]
        outputs = [0,3,2,31]
        for input,output in zip(inputs,outputs):
            self.assertEqual(Day03.solve_part1(input),output)

if __name__ == "__main__":
    unittest.main()
