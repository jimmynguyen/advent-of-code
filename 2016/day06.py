# https://adventofcode.com/2016/day/6
from challenge import Challenge


class Day06(Challenge):
    @staticmethod
    def solve(messages,part2=False):
        d = [dict() for _ in range(len(messages[0]))]
        for message in messages:
            for i,x in enumerate(message):
                if x not in d[i]:
                    d[i][x] = 0
                d[i][x] += 1
        return "".join([sorted(x.items(),key=lambda x:(x[1] if part2 else -x[1],x[0]))[0][0] for x in d])


    @staticmethod
    def solve_part1(input):
        return Day06.solve(input)

    @staticmethod
    def solve_part2(input):
        return Day06.solve(input,part2=True)


if __name__ == "__main__":
    Day06().solve_all()
