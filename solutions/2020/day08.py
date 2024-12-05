# https://adventofcode.com/2020/day/8
from solutions.challenge import Challenge


class Day08(Challenge):
    @staticmethod
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

    @staticmethod
    def solve_2(instructions):
        change_list = []
        for i,instruction in enumerate(instructions):
            if instruction.startswith("nop") or instruction.startswith("jmp"):
                change_list.append((i,instruction.replace("nop","jmp") if instruction.startswith("nop") else instruction.replace("jmp","nop")))
        for i,replaced in change_list:
            _instructions = instructions.copy()
            _instructions[i] = replaced
            accumulator,pc = Day08.solve_1(_instructions)
            if pc == len(_instructions):
                return accumulator,pc
        return None,None

    @staticmethod
    def solve(instructions,solver):
        accumulator,_ = solver(instructions)
        return accumulator

    @staticmethod
    def solve_part1(input):
        return Day08.solve(input,Day08.solve_1)

    @staticmethod
    def solve_part2(input):
        return Day08.solve(input,Day08.solve_2)


if __name__ == "__main__":
    Day08().solve_all()
