from day10 import Day10
import unittest


class TestDay10(unittest.TestCase):
    def test_part1(self):
        input = "3,4,1,5"
        output = 12
        actual = Day10.solve_part1(input, num_elements=5)
        self.assertEqual(actual, output, f"input={input}, expected={output}, actual={actual}")

    def test_part2(self):
        inputs = [
            "",
            "AoC 2017",
            "1,2,3",
            "1,2,4"
        ]
        outputs = [
            "a2582a3a0e66e6e86e3812dcb672a272",
            "33efeb34ea91902bb2f59c9920caa6cd",
            "3efbe78a8d82f29979031a4aa0b16a9d",
            "63960835bcdc130f0b66d7ff4f6a5a8e"
        ]
        for input, output in zip(inputs, outputs):
            actual = Day10.solve_part2(input)
            self.assertEqual(actual, output, f"input={input}, expected={output}, actual={actual}")
