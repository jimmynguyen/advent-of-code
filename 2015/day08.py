# https://adventofcode.com/2015/day/8
import util


def count_decoded_characters(string):
    count = 0
    i = 0
    string = string[1:-1]
    while i < len(string):
        if string[i] == "\\":
            if string[i+1] == "\\":
                i += 1
            elif string[i+1] == "\"":
                i += 1
            elif string[i+1] == "x":
                i += 3
        count += 1
        i += 1
    return count


def count_encoded_characters(string):
    count = 0
    i = 0
    while i < len(string):
        if string[i] == "\\":
            count += 1
        elif string[i] == "\"":
            count += 1
        count += 1
        i += 1
    return count + 2


def solve(strings,count_memory_characters):
    chr_count = 0
    mem_count = 0
    for string in strings:
        chr_count += len(string)
        mem_count += count_memory_characters(string)
    return abs(-chr_count + mem_count)


if __name__ == "__main__":
    day = 8
    inputs = [
        count_decoded_characters,
        count_encoded_characters
    ]
    test_outputs = [12,19]
    util.solve(day,inputs,test_outputs,solve)