from day11 import Day11
import unittest


class TestDay11(unittest.TestCase):
    def test_part1(self):
        inputs = ["ne,ne,ne", "ne,ne,sw,sw", "ne,ne,s,s", "se,sw,se,sw,sw"]
        outputs = [3, 0, 2, 3]
        for input, output in zip(inputs,outputs):
            actual = Day11.solve_part1(input)
            self.assertEqual(actual, output, f"input={input}, expected={output}, actual={actual}")

if __name__ == "__main__":
    unittest.main()
