# https://adventofcode.com/2021/day/6
from solutions.challenge import Challenge


class Day06(Challenge):
    def read_file(self, filename):
        return list(map(int, super().read_file(filename).split(",")))

    @staticmethod
    def increment_one_day(ages):
        return [x - 1 if x > 0 else 6 for x in ages] + ([8] * sum([1 for x in ages if x == 0]))

    @staticmethod
    def get_count(age, days, age_days_to_counts):
        key = (age, days)
        if key in age_days_to_counts:
            return age_days_to_counts[key]
        ages = Day06.increment_one_day([age])
        total = 0
        if days - 1 == 0:
            total += len(ages)
        else:
            for x in ages:
                total += Day06.get_count(x, days - 1, age_days_to_counts)
        age_days_to_counts[key] = total
        return total

    @staticmethod
    def solve(ages, days):
        age_counts = {}
        for age in ages:
            age_counts[age] = age_counts.get(age, 0) + 1
        total = 0
        age_days_to_counts = {}
        for age, count in age_counts.items():
            total += count * Day06.get_count(age, days, age_days_to_counts)
        return total

    @staticmethod
    def solve_part1(input):
        return Day06.solve(input, 80)

    @staticmethod
    def solve_part2(input):
        return Day06.solve(input, 256)


if __name__ == "__main__":
    Day06().solve_all()
