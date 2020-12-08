# https://adventofcode.com/2015/day/17
from itertools import combinations
import util


def solve(containers,args):
    liters,find_min_num_containers = args
    containers = [int(x) for x in containers]
    combos = [x for n in range(1,len(containers)) for x in combinations(containers,n) if sum(x) == liters]
    if find_min_num_containers:
        min_num_containers = min(len(x) for x in combos)
        combos = [x for x in combos if len(x) == min_num_containers]
    return len(combos)

if __name__ == "__main__":
    day = 17
    inputs = [(150,False),(150,True)]
    test_inputs2 = [(25,False),(25,True)]
    test_outputs = [4,3]
    util.solve(day,inputs,test_outputs,solve,test_inputs2=test_inputs2)