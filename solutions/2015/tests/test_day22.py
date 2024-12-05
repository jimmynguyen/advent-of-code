from day22 import Day22
import unittest


class TestDay22(unittest.TestCase):
    def test_part1(self):
        input = Day22().read_file("tests/test_day22.1.txt")
        self.assertEqual(Day22.solve_part1(input,hit_points=10,mana=250),226)
        input = Day22().read_file("tests/test_day22.2.txt")
        self.assertEqual(Day22.solve_part1(input,hit_points=10,mana=250),641)

if __name__ == "__main__":
    unittest.main()
