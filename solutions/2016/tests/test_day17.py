from day17 import Day17
import unittest


class TestDay17(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(Day17.solve_part1("ihgpwlah"),"DDRRRD")
        self.assertEqual(Day17.solve_part1("kglvqrro"),"DDUDRLRRUDRD")
        self.assertEqual(Day17.solve_part1("ulqzkmiv"),"DRURDRUDDLLDLUURRDULRLDUUDDDRR")

    def test_part2(self):
        self.assertEqual(Day17.solve_part2("ihgpwlah"),370)
        self.assertEqual(Day17.solve_part2("kglvqrro"),492)
        self.assertEqual(Day17.solve_part2("ulqzkmiv"),830)

if __name__ == "__main__":
    unittest.main()
