from day01 import Day01
import unittest


class TestDay01(unittest.TestCase):
    def test_part1(self):
        inputs = ["(())","()()","(((","(()(()(","))(((((","())","))(",")))",")())())"]
        outputs = [0,0,3,3,3,-1,-1,-3,-3]
        for input,output in zip(inputs,outputs):
            self.assertEqual(Day01.solve_part1(input),output)

    def test_part2(self):
        inputs = [")","()())"]
        outputs = [1,5]
        for input,output in zip(inputs,outputs):
            self.assertEqual(Day01.solve_part2(input),output)
