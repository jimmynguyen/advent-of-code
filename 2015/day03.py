# https://adventofcode.com/2015/day/3
import util


def read_file(filename):
    return util.read_file(filename)[0]


def solve(directions,position):
    visited = set(position)
    for i in range(0,len(directions),len(position)):
        for j in range(len(position)):
            direction = get_direction(directions[i+j])
            position[j] = tuple([sum(x) for x in zip(position[j],direction)])
            visited.add(position[j])
    return len(visited)


def get_direction(d):
    if d == "^":
        direction = (0,1)
    elif d == "v":
        direction = (0,-1)
    elif d == "<":
        direction = (-1,0)
    elif d == ">":
        direction = (1,0)
    else:
        raise Exception("Invalid direction {}".format(d))
    return direction


if __name__ == "__main__":
    day = 3
    inputs = [
        [(0,0)],
        [(0,0),(0,0)]
    ]
    test_inputs1_part1 = [">","^>v<","^v^v^v^v^v"]
    test_inputs1_part2 = ["^v","^>v<","^v^v^v^v^v"]
    test_inputs1 = test_inputs1_part1 + test_inputs1_part2
    test_inputs2 = [[x+tuple() for x in inputs[0]] for _ in range(len(test_inputs1_part1))] + [[x+tuple() for x in inputs[1]] for _ in range(len(test_inputs1_part2))]
    test_outputs_part1 = [2,4,2]
    test_outputs_part2 = [3,3,11]
    test_outputs = test_outputs_part1 + test_outputs_part2
    util.solve(day,inputs,test_outputs,solve,read_file=read_file,test_inputs1=test_inputs1,test_inputs2=test_inputs2)