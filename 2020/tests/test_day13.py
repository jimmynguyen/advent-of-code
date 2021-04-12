from day13 import Day13
import unittest


class TestDay13(unittest.TestCase):
    def test_part1(self):
        input = Day13().read_file("tests/test_day13.1.txt")
        self.assertEqual(Day13.solve_part1(input),295)

    def test_part2(self):
        outputs = [1068781,3417,754018,779210,1261476,1202161486]
        for i,output in enumerate(outputs):
            input = Day13().read_file(f"tests/test_day13.{i+2}.txt")
            self.assertEqual(Day13.solve_part2(input),output)
