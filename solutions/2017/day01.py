# https://adventofcode.com/2017/day/1
from solutions.challenge import Challenge


class Day01(Challenge):
    @staticmethod
    def solve_part1(captcha,n=1):
        return sum(int(x) for x,y in zip(captcha,captcha[n:]+captcha[0:n]) if x == y)

    @staticmethod
    def solve_part2(captcha):
        return Day01.solve_part1(captcha,n=len(captcha)//2)


if __name__ == "__main__":
    Day01().solve_all()
