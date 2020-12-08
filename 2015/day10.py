# https://adventofcode.com/2015/day/10
import util


def solve(seq,num_passes):
    seq = str(seq)
    for _ in range(num_passes):
        res = ""
        i = 0
        subseq = None
        while i < len(seq):
            subseq = seq[i]
            while i < len(seq)-1 and seq[i] == seq[i+1]:
                i += 1
                subseq += seq[i]
            res += str(len(subseq)) + subseq[0]
            i += 1
        seq = res
    return len(seq)


if __name__ == "__main__":
    day = 10
    day_inputs = 1321131112
    inputs = [40,50]
    test_inputs1 = [1]
    test_inputs2 = [5]
    test_outputs = [6]
    util.solve(day,inputs,test_outputs,solve,day_inputs=day_inputs,test_inputs1=test_inputs1,test_inputs2=test_inputs2)