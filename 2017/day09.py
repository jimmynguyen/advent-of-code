# https://adventofcode.com/2017/day/9
from challenge import Challenge


class Day09(Challenge):
    @staticmethod
    def solve_part1(stream, return_score=True):
        score, level, num_garbage = 0, 0, 0
        negate, garbage = False, False
        for x in stream:
            if negate:
                negate = False
                continue
            if garbage:
                if x == "!":
                    negate = True
                elif x == ">":
                    garbage = False
                else:
                    num_garbage += 1
                continue
            if x == "{":
                level += 1
            elif x == "}":
                score += level
                level -= 1
            elif x == "<":
                garbage = True
        return score if return_score else num_garbage

    @staticmethod
    def solve_part2(stream):
        return Day09.solve_part1(stream, return_score=False)


if __name__ == "__main__":
    Day09().solve_all()
