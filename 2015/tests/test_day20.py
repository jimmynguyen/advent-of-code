from day20 import Day20
import unittest


class TestDay20(unittest.TestCase):
    def test_part1(self):
        inputs = [10,30,40,70,60,120,80,150,130]
        outputs = [1,2,3,4,4,6,6,8,8]
        for input,output in zip(inputs,outputs):
            self.assertEqual(Day20.solve_part1(input),output)

if __name__ == "__main__":
    unittest.main()
