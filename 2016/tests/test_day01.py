from day01 import Day01
import unittest


class TestDay01(unittest.TestCase):
    def test_part1(self):
        inputs = ["R2, L3","R2, R2, R2","R5, L5, R5, R3"]
        outputs = [5,2,12]
        for input,output in zip(inputs,outputs):
            self.assertEqual(Day01.solve_part1(input),output)

    def test_part2(self):
        inputs = ["R8, R4, R4, R8"]
        outputs = [4]
        for input,output in zip(inputs,outputs):
            self.assertEqual(Day01.solve_part2(input),output)

if __name__ == "__main__":
    unittest.main()
