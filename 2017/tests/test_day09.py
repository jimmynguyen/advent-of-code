from day09 import Day09
import unittest


class TestDay09(unittest.TestCase):
    def test_part1(self):
        inputs = [
            "{}",
            "{{{}}}",
            "{{},{}}",
            "{{{},{},{{}}}}",
            "{<{},{},{{}}>}",
            "{<a>,<a>,<a>,<a>}",
            "{{<ab>},{<ab>},{<ab>},{<ab>}}",
            "{{<a>},{<a>},{<a>},{<a>}}",
            "{{<!>},{<!>},{<!>},{<a>}}"
        ]
        outputs = [1,6,5,16,1,1,9,9,3]
        for input, output in zip(inputs, outputs):
            actual = Day09.solve_part1(input)
            self.assertEqual(actual, output, f"input={input}, expected={output}, actual={actual}")

    def test_part2(self):
        inputs = [
            "<>",
            "<random characters>",
            "<<<<>",
            "<{!>}>",
            "<!!>",
            "<!!!>>",
            "<{o\"i!a,<{i<a>"
        ]
        outputs = [0,17,3,2,0,0,10]
        for input, output in zip(inputs, outputs):
            actual = Day09.solve_part2(input)
            self.assertEqual(actual, output, f"input={input}, expected={output}, actual={actual}")
