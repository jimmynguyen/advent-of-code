# https://adventofcode.com/2020/day/15
import util


def solve(sequence,nth_number):
    age = dict()
    last_number = None
    for i in range(nth_number):
        if i < len(sequence):
            last_number = sequence[i]
            age[last_number] = [i]
        else:
            if len(age[last_number]) == 1:
                last_number = 0
            else:
                last_number = age[last_number][1] - age[last_number][0]
            if last_number not in age:
                age[last_number] = [i]
            else:
                age[last_number] = [age[last_number][-1],i]
    return last_number


if __name__ == "__main__":
    day = 15
    day_inputs = [2,0,6,12,1,3]
    inputs = [2020,30000000]
    test_inputs1_part1 = [[0,3,6],[1,3,2],[2,1,3],[1,2,3],[2,3,1],[3,2,1],[3,1,2]]
    test_inputs1_part2 = [[0,3,6],[1,3,2],[2,1,3],[1,2,3],[2,3,1],[3,2,1],[3,1,2]]
    test_inputs1 = test_inputs1_part1 + test_inputs1_part2
    test_inputs2 = [inputs[0]] * len(test_inputs1_part1) + [inputs[1]] * len(test_inputs1_part2)
    test_outputs = [436,1,10,27,78,438,1836,175594,2578,3544142,261214,6895259,18,362]
    util.solve(day,inputs,test_outputs,solve,day_inputs=day_inputs,test_inputs1=test_inputs1,test_inputs2=test_inputs2)