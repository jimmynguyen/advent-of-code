# https://adventofcode.com/2015/day/20
import numba
import util


@numba.njit
def count_presents_with_inf_elves(elf,house):
    return (10 * elf) if house % elf == 0 else 0


@numba.njit
def count_presents_with_max_elves(elf,house,max_elves=50):
    return (11 * elf) if house % elf == 0 and elf * max_elves >= house else 0


@numba.njit
def solve(goal,count_presents):
    num_presents = 0
    house = 0
    while num_presents < goal:
        house += 1
        num_presents = 0
        for elf in range(1,house+1):
            num_presents += count_presents(elf,house)
    return house


if __name__ == "__main__":
    day = 20
    day_inputs = 36000000
    inputs = [
        count_presents_with_inf_elves,
        count_presents_with_max_elves
    ]
    test_inputs1 = [10,30,40,70,60,120,80,150,130]
    test_inputs2 = [count_presents_with_inf_elves] * len(test_inputs1)
    test_outputs = [1,2,3,4,4,6,6,8,8]
    util.solve(day,inputs,test_outputs,solve,day_inputs=day_inputs,test_inputs1=test_inputs1,test_inputs2=test_inputs2)