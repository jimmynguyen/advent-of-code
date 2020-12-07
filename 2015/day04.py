# https://adventofcode.com/2015/day/4
import hashlib 
import util


def read_file(filename):
    return util.read_file(filename)[0]


def solve(key,prefix):
    template = key + "{}"
    num = 1
    while not hashlib.md5(bytes(template.format(num),"utf-8")).hexdigest().startswith(prefix):
        num += 1
    return num


if __name__ == "__main__":
    day = 4
    day_inputs = "ckczppom"
    inputs = [
        "0" * 5,
        "0" * 6
    ]
    test_inputs1_part1 = ["abcdef","pqrstuv"]
    test_inputs1_part2 = []
    test_inputs1 = test_inputs1_part1 + test_inputs1_part2
    test_inputs2 = [inputs[0]]*len(test_inputs1_part1)
    test_outputs_part1 = [609043,1048970]
    test_outputs_part2 = []
    test_outputs = test_outputs_part1 + test_outputs_part2
    util.solve(day,inputs,test_outputs,solve,read_file=read_file,day_inputs=day_inputs,test_inputs1=test_inputs1,test_inputs2=test_inputs2)