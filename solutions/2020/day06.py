# https://adventofcode.com/2020/day/6
from solutions.challenge import Challenge


class Day06(Challenge):
    def read_file(self,filename,delimiter="\n\n"):
        return [x.replace("\n"," ") for x in super().read_file(filename,delimiter)]

    @staticmethod
    def count(group):
        answers = [set(x) for x in group.split(" ")]
        return len(answers[0].intersection(*answers[1:]))

    @staticmethod
    def solve(groups,count):
        answer = 0
        for group in groups:
            answer += count(group)
        return answer

    @staticmethod
    def solve_part1(input):
        return Day06.solve(input,lambda x: len(set(x.replace(" ",""))))

    @staticmethod
    def solve_part2(input):
        return Day06.solve(input,Day06.count)


if __name__ == "__main__":
    Day06().solve_all()
