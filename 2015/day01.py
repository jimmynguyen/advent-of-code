# https://adventofcode.com/2015/day/1
import util


def read_file(filename):
    return util.read_file(filename)[0]


def solve(directions,solver):
    return solver(directions)


def get_basement_position(directions):
    floor = 0
    for i,x in enumerate(directions):
        if x == "(":
            floor += 1
        else:
            floor -= 1
        if floor == -1:
            return i + 1
    return None


if __name__ == "__main__":
    day = 1
    inputs = [
        lambda x: x.count("(") - x.count(")"),
        get_basement_position
    ]
    test_inputs1_part1 = ["(())","()()","(((","(()(()(","))(((((","())","))(",")))",")())())"]
    test_inputs1_part2 = [")","()())"]
    test_inputs1 = test_inputs1_part1 + test_inputs1_part2
    test_inputs2 = [inputs[0]] * len(test_inputs1_part1) + [inputs[1]] * len(test_inputs1_part2)
    test_outputs_part1 = [0,0,3,3,3,-1,-1,-3,-3]
    test_outputs_part2 = [1,5]
    test_outputs = test_outputs_part1 + test_outputs_part2
    util.solve(day,inputs,test_outputs,solve,read_file=read_file,test_inputs1=test_inputs1,test_inputs2=test_inputs2)