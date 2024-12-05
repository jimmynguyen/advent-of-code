# https://adventofcode.com/2020/day/15
from solutions.challenge import Challenge


class Day15(Challenge):
    def read_file(self,filename):
        return [int(x) for x in super().read_file(filename).split(",")]

    @staticmethod
    def solve(sequence,nth_number):
        age = dict()
        last_number = None
        for i in range(nth_number):
            if i < len(sequence):
                last_number = sequence[i]
                age[last_number] = [i]
            else:
                if len(age[last_number]) == 1:
                    last_number = 0
                else:
                    last_number = age[last_number][1] - age[last_number][0]
                if last_number not in age:
                    age[last_number] = [i]
                else:
                    age[last_number] = [age[last_number][-1],i]
        return last_number

    @staticmethod
    def solve_part1(input):
        return Day15.solve(input,2020)

    @staticmethod
    def solve_part2(input):
        return Day15.solve(input,30000000)


if __name__ == "__main__":
    Day15().solve_all()
