# https://adventofcode.com/2020/day/9
from challenge import Challenge
from itertools import combinations


class Day09(Challenge):
    @staticmethod
    def probe_weakness(numbers,history_length):
        for n in range(history_length,len(numbers)):
            if not any([sum(x) == numbers[n] for x in combinations(numbers[n-history_length:n],2)]):
                return numbers[n]
        raise Exception("Invalid test case")

    @staticmethod
    def identify_weakness(numbers,history_length):
        invalid_number = Day09.probe_weakness(numbers,history_length)
        for n in range(2,len(numbers)):
            for i in range(len(numbers)-n):
                x = numbers[i:i+n]
                if sum(x) == invalid_number:
                    return max(x) + min(x)
        raise Exception("Invalid test case")

    @staticmethod
    def solve(numbers,args):
        solver,history_length = args
        numbers = [int(x) for x in numbers]
        return solver(numbers,history_length)

    @staticmethod
    def solve_part1(input,history_length=25):
        return Day09.solve(input,(Day09.probe_weakness,history_length))

    @staticmethod
    def solve_part2(input,history_length=25):
        return Day09.solve(input,(Day09.identify_weakness,history_length))


if __name__ == "__main__":
    Day09().solve_all()
