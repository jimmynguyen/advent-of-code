from day09 import Day09
import unittest


class TestDay09(unittest.TestCase):
    def test_part1(self):
        inputs = ["ADVENT","A(1x5)BC","(3x3)XYZ","A(2x2)BCD(2x2)EFG","(6x1)(1x3)A","X(8x2)(3x3)ABCY"]
        outputs = [6,7,9,11,6,18]
        for i,(input,output) in enumerate(zip(inputs,outputs)):
            actual = Day09.solve_part1(input)
            self.assertEqual(actual,output,f"Failed part 1 test #{i+1}: input={input}, expected={output}, actual={actual}")

    def test_part2(self):
        inputs = ["(3x3)XYZ","X(8x2)(3x3)ABCY","(27x12)(20x12)(13x14)(7x10)(1x12)A","(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN"]
        outputs = [9,20,241920,445]
        for i,(input,output) in enumerate(zip(inputs,outputs)):
            actual = Day09.solve_part2(input)
            self.assertEqual(actual,output,f"Failed part 2 test #{i+1}: input={input}, expected={output}, actual={actual}")
