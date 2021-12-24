from day18 import Day18
import unittest


class TestDay18(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(Day18.solve_part1("..^^.",3),6)
        self.assertEqual(Day18.solve_part1(".^^.^.^^^^",10),38)

if __name__ == "__main__":
    unittest.main()
