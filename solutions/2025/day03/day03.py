# https://adventofcode.com/2025/day/3
from solutions.challenge import Challenge


def compute_bank_output_joltage(
    battery_bank: list[int],
    num_batteries_remaining: int,
    bank_output_joltage: str = "",
):
    if num_batteries_remaining == 0:
        return bank_output_joltage
    battery_bank_with_exclusions = list(battery_bank)
    for _ in range(len(battery_bank)):
        max_battery = max(battery_bank_with_exclusions)
        idx_max_battery = battery_bank_with_exclusions.index(max_battery)
        if len(battery_bank) - idx_max_battery > num_batteries_remaining - 1:
            new_bank_output_joltage = compute_bank_output_joltage(
                battery_bank[idx_max_battery+1:],
                num_batteries_remaining-1,
                bank_output_joltage + str(max_battery)
            )
            if new_bank_output_joltage is not None:
                return new_bank_output_joltage
        # exclude idx_max_battery from battery bank on next max search
        battery_bank_with_exclusions[idx_max_battery] = -1
    raise Exception("Failed to compute bank output joltage")


class Day03(Challenge):
    def read_file(self,filename) -> list[list[int]]:
        return [
            list(map(int, line))
            for line
            in super().read_file(filename, delimiter="\n")
        ]

    @staticmethod
    def solve_part1(
        battery_banks: list[list[int]],
        num_batteries_on: int = 2,
    ):
        total_output_joltage = 0
        for battery_bank in battery_banks:
            bank_output_joltage = compute_bank_output_joltage(battery_bank, num_batteries_on)
            total_output_joltage += int(bank_output_joltage)
        return total_output_joltage

    @staticmethod
    def solve_part2(
        battery_banks: list[list[int]],
    ):
        return Day03.solve_part1(battery_banks, num_batteries_on=12)


if __name__ == "__main__":
    Day03().solve_all()
