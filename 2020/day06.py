# https://adventofcode.com/2020/day/6
import util


def count(group):
    answers = [set(x) for x in group.split(" ")]
    return len(answers[0].intersection(*answers[1:]))


def read_file(filename):
    return [x.replace("\n"," ") for x in util.read_file(filename,"\n\n")]


def solve(groups,count):
    answer = 0
    for group in groups:
        answer += count(group)
    return answer


if __name__ == "__main__":
    day = 6
    inputs = [
        lambda x: len(set(x.replace(" ",""))),
        count
    ]
    test_outputs = [11,6]
    util.solve(day,inputs,test_outputs,solve,read_file)