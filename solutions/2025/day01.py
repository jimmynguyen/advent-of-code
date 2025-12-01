# https://adventofcode.com/2025/day/1
from solutions.challenge import Challenge


class Day01(Challenge):
    def read_file(self,filename) -> list[int]:
        return [
            int(line.replace("L", "-").replace("R", ""))
            for line
            in super().read_file(filename)
        ]

    @staticmethod
    def solve(steps: list[int], dial_init: int, part2: bool = False):
        dial = dial_init
        total_zero_count = 0
        for step in steps:
            end_zero_count = 0
            pass_zero_count = 0

            while step > 100:
                step -= 100
                pass_zero_count += 1

            while step < -100:
                step += 100
                pass_zero_count += 1

            if step > 0:
                if dial + step >= 100:
                    if dial != 0 and dial+step-100 != 0:
                        pass_zero_count += 1
                    dial += step - 100
                else:
                    dial += step
            elif step < 0:
                if dial + step < 0:
                    if dial != 0 and dial+step+100 != 0:
                        pass_zero_count += 1
                    dial += step + 100
                else:
                    dial += step

            if dial == 0:
                end_zero_count += 1

            total_zero_count += end_zero_count

            if part2:
                total_zero_count += pass_zero_count

        return total_zero_count

    @staticmethod
    def solve_part1(steps: list[int], dial_init: int = 50):
        return Day01.solve(steps, dial_init)

    @staticmethod
    def solve_part2(steps: list[int], dial_init: int = 50, part2: bool = True):
        return Day01.solve(steps, dial_init, part2)


if __name__ == "__main__":
    Day01().solve_all()
