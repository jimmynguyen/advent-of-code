# https://adventofcode.com/2020/day/2
from challenge import Challenge


class Day02(Challenge):
    @staticmethod
    def parse(input,delimiter):
        _parse = lambda l,delimiter: tuple(map(lambda x: x.strip(),l.split(delimiter)))
        return [_parse(l,delimiter) for l in input] if isinstance(input,list) else _parse(input,delimiter)

    @staticmethod
    def solve(lines,validate):
        num_valid = 0
        for policy,password in Day02.parse(lines,":"):
            a,policy = Day02.parse(policy,"-")
            b,letter = Day02.parse(policy," ")
            if validate(password,int(a),int(b),letter):
                num_valid += 1
        return num_valid

    @staticmethod
    def solve_part1(input):
        return Day02.solve(input,lambda s,a,b,c: s.count(c) in range(a,b+1))

    @staticmethod
    def solve_part2(input):
        return Day02.solve(input,lambda s,a,b,c: (s[a-1] == c and s[b-1] != c) or (s[a-1] != c and s[b-1] == c))


if __name__ == "__main__":
    Day02().solve_all()
