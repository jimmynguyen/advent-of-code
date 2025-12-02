from day11.day11 import Day11, compute_power_level
import unittest


class TestDay11(unittest.TestCase):
    def test_compute_power_level(self):
        for (x, y, grid_serial_number), expected_power_level in [
            ((3, 5, 8), 4),
            ((122, 79, 57), -5),
            ((217, 196, 39), 0),
            ((101, 153, 71), 4),
        ]:
            actual_power_level = compute_power_level(x, y, grid_serial_number)
            self.assertEqual(actual_power_level, expected_power_level, f"Expected compute_power_level({x}, {y}, {grid_serial_number}) to equal {expected_power_level} but was {actual_power_level}")

    def test_part1(self):
        self.assertEqual(Day11.solve_part1(None, 18), (33, 45))


if __name__ == "__main__":
    unittest.main()
