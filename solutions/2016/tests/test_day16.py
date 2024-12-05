from day16 import Day16
import unittest


class TestDay16(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(Day16.solve_part1("10000",length=20),"01100")

if __name__ == "__main__":
    unittest.main()
