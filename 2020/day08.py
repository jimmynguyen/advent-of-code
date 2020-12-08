# https://adventofcode.com/2020/day/8
import util


def solve_1(instructions):
    accumulator = 0
    executed = []
    pc = 0
    while pc not in executed:
        if pc >= len(instructions):
            break
        executed.append(pc)
        instruction = instructions[pc]
        if instruction.startswith("nop"):
            pc += 1
        elif instruction.startswith("acc"):
            pc += 1
            argument = instruction.replace("acc ","")
            if argument[0] == "-":
                accumulator -= int(argument[1:])
            elif argument[0] == "+":
                accumulator += int(argument[1:])
            else:
                raise Exception("Invalid acc argument")
        elif instruction.startswith("jmp"):
            argument = instruction.replace("jmp ","")
            if argument[0] == "-":
                pc -= int(argument[1:])
            elif argument[0] == "+":
                pc += int(argument[1:])
            else:
                raise Exception("Invalid jmp argument")
        else:
            raise Exception("Invalid instruction")
    return accumulator,pc


def solve_2(instructions):
    change_list = []
    for i,instruction in enumerate(instructions):
        if instruction.startswith("nop") or instruction.startswith("jmp"):
            change_list.append((i,instruction.replace("nop","jmp") if instruction.startswith("nop") else instruction.replace("jmp","nop")))
    for i,replaced in change_list:
        _instructions = instructions.copy()
        _instructions[i] = replaced
        accumulator,pc = solve_1(_instructions)
        if pc == len(_instructions):
            return accumulator,pc
    return None,None


def solve(instructions,solver):
    accumulator,_ = solver(instructions)
    return accumulator


if __name__ == "__main__":
    day = 8
    inputs = [solve_1,solve_2]
    test_outputs = [5,8]
    util.solve(day,inputs,test_outputs,solve)