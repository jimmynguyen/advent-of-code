from day15 import Day15
import unittest


class TestDay15(unittest.TestCase):
    def setUp(self):
        self.inputs = [[0,3,6],[1,3,2],[2,1,3],[1,2,3],[2,3,1],[3,2,1],[3,1,2]]

    def test_part1(self):
        outputs = [436,1,10,27,78,438,1836]
        for input,output in zip(self.inputs,outputs):
            self.assertEqual(Day15.solve_part1(input),output)

    def test_part2(self):
        outputs = [175594,2578,3544142,261214,6895259,18,362]
        for input,output in zip(self.inputs,outputs):
            self.assertEqual(Day15.solve_part2(input),output)

if __name__ == "__main__":
    unittest.main()
