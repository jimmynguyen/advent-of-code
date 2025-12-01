from day09.day09 import Day09
import unittest


class TestDay09(unittest.TestCase):
    def test_part1(self):
        for line, highest_score in [
            ("9 players; last marble is worth 25 points", 32),
            ("10 players; last marble is worth 1618 points", 8317),
            ("13 players; last marble is worth 7999 points", 146373),
            ("17 players; last marble is worth 1104 points", 2764),
            ("21 players; last marble is worth 6111 points", 54718),
            ("30 players; last marble is worth 5807 points", 37305),
        ]:
            parsed_input = Day09.parse_file(line)
            self.assertEqual(Day09.solve_part1(parsed_input), highest_score)


if __name__ == "__main__":
    unittest.main()
