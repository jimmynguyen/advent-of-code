from day06 import Day06
import unittest


class TestDay06(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(Day06.solve_part1("mjqjpqmgbljsphdztnvjfqwrcgsmlb"), 7)
        self.assertEqual(Day06.solve_part1("bvwbjplbgvbhsrlpgdmjqwftvncz"), 5)
        self.assertEqual(Day06.solve_part1("nppdvjthqldpwncqszvftbrmjlhg"), 6)
        self.assertEqual(Day06.solve_part1("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"), 10)
        self.assertEqual(Day06.solve_part1("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"), 11)

    def test_part2(self):
        self.assertEqual(Day06.solve_part2("mjqjpqmgbljsphdztnvjfqwrcgsmlb"), 19)
        self.assertEqual(Day06.solve_part2("bvwbjplbgvbhsrlpgdmjqwftvncz"), 23)
        self.assertEqual(Day06.solve_part2("nppdvjthqldpwncqszvftbrmjlhg"), 23)
        self.assertEqual(Day06.solve_part2("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"), 29)
        self.assertEqual(Day06.solve_part2("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"), 26)

if __name__ == "__main__":
    unittest.main()
