from day14.day14 import Day14
import unittest


class TestDay14(unittest.TestCase):
    def test_part1(self):
        for num_recipes, expected_score in [
            (9, "5158916779"),
            (5, "0124515891"),
            (18, "9251071085"),
            (2018, "5941429882")
        ]:
            self.assertEqual(Day14.solve_part1(num_recipes), expected_score)


    def test_part2(self):
        for sequence, expected_num_recipes in [
            ("51589", 9),
            ("01245", 5),
            ("92510", 18),
            ("59414", 2018)
        ]:
            self.assertEqual(Day14.solve_part2(sequence), expected_num_recipes)


if __name__ == "__main__":
    unittest.main()
