# https://adventofcode.com/2020/day/14
import util


def update_memory_1(memory,mask,assignments):
    for address,value in assignments:
        value = format(int(value),'#036b').replace("b","0")
        result = ""
        for i,bit in enumerate(mask):
            if bit == "X":
                result += value[i]
            else:
                result += bit
        memory[address] = int(result,2)
    return memory


def update_memory_2(memory,mask,assignments):
    for address,value in assignments:
        address = format(int(address),'#036b').replace("b","0")
        addresses = [""]
        for i,bit in enumerate(mask):
            _addresses = []
            for addr in addresses:
                if bit == "0":
                    _addresses.append(addr + address[i])
                elif bit == "X":
                    _addresses.append(addr + "0")
                    _addresses.append(addr + "1")
                else:
                    _addresses.append(addr + bit)
            addresses = _addresses
        for addr in addresses:
            memory[int(addr,2)] = int(value)
    return memory


def solve(lines,update_memory):
    starts = [i for i,x in enumerate(lines) if x.startswith("mask")]
    ends = starts[1:] + [len(lines)]
    memory = dict()
    for start,end in zip(starts,ends):
        mask = lines[start].split("mask = ")[1]
        assignments = lines[start+1:end]
        assignments = [tuple(x.split("mem[")[1].split("] = ")) for x in assignments]
        memory = update_memory(memory,mask,assignments)
    return sum(memory.values())


if __name__ == "__main__":
    day = 14
    inputs = [update_memory_1,update_memory_2]
    test_outputs = [165,208]
    util.solve(day,inputs,test_outputs,solve)