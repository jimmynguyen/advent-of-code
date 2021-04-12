from day12 import Day12
import unittest


class TestDay12(unittest.TestCase):
    def test_part1(self):
        inputs = ["[1,2,3]","{\"a\":2,\"b\":4}","[[[3]]]","{\"a\":{\"b\":4},\"c\":-1}","{\"a\":[-1,1]}","[-1,{\"a\":1}]","[]","{}"]
        outputs = [6,6,3,3,0,0,0,0]
        for input,output in zip(inputs,outputs):
            self.assertEqual(Day12.solve_part1(input),output)

    def test_part2(self):
        inputs = ["[1,2,3]","[1,{\"c\":\"red\",\"b\":2},3]","{\"d\":\"red\",\"e\":[1,2,3,4],\"f\":5}","[1,\"red\",5]"]
        outputs = [6,4,0,6]
        for input,output in zip(inputs,outputs):
            self.assertEqual(Day12.solve_part2(input),output)
