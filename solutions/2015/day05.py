# https://adventofcode.com/2015/day/5
from solutions.challenge import Challenge


class Day05(Challenge):
    @staticmethod
    def solve(children,is_nice):
        return sum([is_nice(x) for x in children])

    @staticmethod
    def solve_part1(input):
        return Day05.solve(input,lambda child: sum([x in "aeiou" for x in child]) >= 3 \
            and any([child[i] == child[i+1] for i in range(len(child)-1)]) \
            and not any([x in child for x in ["ab","cd","pq","xy"]]))

    @staticmethod
    def solve_part2(input):
        return Day05.solve(input,lambda child: any([(child[i:i+2] in child[:i]) or (child[i:i+2] in child[i+2:]) for i in range(len(child)-1)]) \
            and any([child[i] == child[i+2] for i in range(len(child)-2)]))


if __name__ == "__main__":
    Day05().solve_all()
