# https://adventofcode.com/2015/day/12
import json
import util


def sum_numbers(data,ignore_red):
    sum = 0
    if isinstance(data,list):
        for x in data:
            sum += sum_numbers(x,ignore_red)
    elif isinstance(data,dict):
        if ignore_red and any([x == "red" for x in data.values()]):
            pass
        else:
            for x in data.values():
                sum += sum_numbers(x,ignore_red)
    elif isinstance(data,str):
        pass
    else:
        sum += data
    return sum


def solve(data,ignore_red):
    data = json.loads(data)
    return sum_numbers(data,ignore_red)


if __name__ == "__main__":
    day = 12
    inputs = [False,True]
    test_inputs1_part1 = ["[1,2,3]","{\"a\":2,\"b\":4}","[[[3]]]","{\"a\":{\"b\":4},\"c\":-1}","{\"a\":[-1,1]}","[-1,{\"a\":1}]","[]","{}"]
    test_inputs1_part2 = ["[1,2,3]","[1,{\"c\":\"red\",\"b\":2},3]","{\"d\":\"red\",\"e\":[1,2,3,4],\"f\":5}","[1,\"red\",5]"]
    test_inputs1 = test_inputs1_part1 + test_inputs1_part2
    test_inputs2 = [False] * len(test_inputs1_part1) + [True] * len(test_inputs1_part2)
    test_outputs = [6,6,3,3,0,0,0,0,6,4,0,6]
    util.solve(day,inputs,test_outputs,solve,read_file=lambda x: util.read_file(x)[0],test_inputs1=test_inputs1,test_inputs2=test_inputs2)