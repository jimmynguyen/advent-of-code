# https://adventofcode.com/2020/day/2
import util


def parse(input,delimiter):
    _parse = lambda l,delimiter: tuple(map(lambda x: x.strip(),l.split(delimiter)))
    return [_parse(l,delimiter) for l in input] if isinstance(input,list) else _parse(input,delimiter)


def solve(lines,validate):
    num_valid = 0
    for policy,password in parse(lines,":"):
        a,policy = parse(policy,"-")
        b,letter = parse(policy," ")
        if validate(password,int(a),int(b),letter):
            num_valid += 1
    return num_valid


if __name__ == "__main__":
    day = 2
    validators = [
        lambda s,a,b,c: s.count(c) in range(a,b+1),
        lambda s,a,b,c: (s[a-1] == c and s[b-1] != c) or (s[a-1] != c and s[b-1] == c)
    ]
    test_outputs = [2,1]
    util.solve(day,validators,test_outputs,solve)