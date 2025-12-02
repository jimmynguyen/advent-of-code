# https://adventofcode.com/2018/day/11
from solutions.challenge import Challenge
import numpy as np


def compute_power_level(
    x: int | np.ndarray,
    y: int | np.ndarray,
    grid_serial_number: int,
) -> int | np.ndarray:
    """
    The power level in a given fuel cell can be found through the following process:

    - Find the fuel cell's rack ID, which is its X coordinate plus 10.
    - Begin with a power level of the rack ID times the Y coordinate.
    - Increase the power level by the value of the grid serial number (your puzzle input).
    - Set the power level to itself multiplied by the rack ID.
    - Keep only the hundreds digit of the power level (so 12345 becomes 3; numbers with no hundreds digit become 0).
    - Subtract 5 from the power level.
    """
    rack_id = x + 10
    power_level = (rack_id * y + grid_serial_number) * rack_id
    power_level = (power_level // 100) % 10
    return power_level - 5


class Day11(Challenge):
    @staticmethod
    def solve_part1(
        _,
        grid_serial_number: int = 9306,
        grid_size: int = 300,
        window_size: int = 3,
        output_power_level: bool = False,
    ):
        y, x = np.indices((grid_size, grid_size), dtype=int) + 1
        power_level = compute_power_level(x, y, grid_serial_number)
        window_grid_size = grid_size-window_size+1
        window_power_level = np.zeros(shape=(window_grid_size, window_grid_size), dtype=int)
        for i in range(window_size):
            for j in range(window_size):
                window_power_level += power_level[i:window_grid_size+i, j:window_grid_size+j]
        y, x = np.unravel_index(np.argmax(window_power_level), window_power_level.shape)
        return (int(x+1), int(y+1), window_power_level[y, x]) if output_power_level else (int(x+1), int(y+1))

    @staticmethod
    def solve_part2(
        _,
        grid_serial_number: int = 9306,
        grid_size: int = 300,
    ):
        max_power_level = float("-inf")
        max_power_level_identifier = None
        for window_size in range(1, grid_size+1):
            x, y, power_level = Day11.solve_part1(_, grid_serial_number, grid_size=grid_size, window_size=window_size, output_power_level=True)
            if power_level > max_power_level:
                max_power_level = power_level
                max_power_level_identifier = (x, y, window_size)
        return max_power_level_identifier


if __name__ == "__main__":
    Day11().solve_all()
