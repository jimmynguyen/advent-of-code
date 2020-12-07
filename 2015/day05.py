# https://adventofcode.com/2015/day/5
import util


def is_nice_1(child):
    return sum([x in "aeiou" for x in child]) >= 3 \
        and any([child[i] == child[i+1] for i in range(0,len(child)-1)]) \
        and not any([x in child for x in ["ab","cd","pq","xy"]])


def is_nice_2(child):
    return any([(child[i:i+2] in child[:i]) or (child[i:i+2] in child[i+2:]) for i in range(len(child)-1)]) \
        and any([child[i] == child[i+2] for i in range(len(child)-2)])


def solve(children,is_nice):
    return sum([is_nice(x) for x in children])


if __name__ == "__main__":
    day = 5
    inputs = [is_nice_1,is_nice_2]
    test_outputs = [2,2]
    util.solve(day,inputs,test_outputs,solve)