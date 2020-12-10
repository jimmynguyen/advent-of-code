# https://adventofcode.com/2020/day/9
from itertools import combinations
import util


def probe_weakness(numbers,history_length):
    for n in range(history_length,len(numbers)):
        if not any([sum(x) == numbers[n] for x in combinations(numbers[n-history_length:n],2)]):
            return numbers[n]
    raise Exception("Invalid test case")


def identify_weakness(numbers,history_length):
    invalid_number = probe_weakness(numbers,history_length)
    for n in range(2,len(numbers)):
        for i in range(len(numbers)-n):
            x = numbers[i:i+n]
            if sum(x) == invalid_number:
                return max(x) + min(x)
    raise Exception("Invalid test case")


def solve(numbers,args):
    solver,history_length = args
    numbers = [int(x) for x in numbers]
    return solver(numbers,history_length)


if __name__ == "__main__":
    day = 9
    inputs = [(probe_weakness,25),(identify_weakness,25)]
    test_inputs2 = [(probe_weakness,5),(identify_weakness,5)]
    test_outputs = [127,62]
    util.solve(day,inputs,test_outputs,solve,test_inputs2=test_inputs2)