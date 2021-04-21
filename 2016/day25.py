# https://adventofcode.com/2016/day/25
from challenge import Challenge


class Day25(Challenge):
    @staticmethod
    def solve(instructions,reg_a=0,forever=1e6):
        while True:
            reg_a += 1
            regs = {"a":reg_a,"b":0,"c":0,"d":0}
            pc = 0
            out = None
            t = 0
            while pc < len(instructions) and t < forever:
                ins = instructions[pc]
                if ins.startswith(Instruction.CPY) or ins.startswith(Instruction.JMP):
                    x,y = tuple(map(lambda x:int(x) if x.isnumeric() or x[1:].isnumeric() else x,ins.replace(Instruction.CPY,"").replace(Instruction.JMP,"").strip().split()))
                    x = x if isinstance(x,int) else regs[x]
                    is_jmp = ins.startswith(Instruction.JMP)
                    if is_jmp:
                        y = y if isinstance(y,int) else regs[y]
                        pc += y-1 if x != 0 else 0
                    elif y in regs:
                        regs[y] = x
                elif ins.startswith(Instruction.INC) or ins.startswith(Instruction.DEC) or ins.startswith(Instruction.OUT):
                    x = ins.replace(Instruction.INC,"").replace(Instruction.DEC,"").replace(Instruction.OUT,"").strip()
                    if ins.startswith(Instruction.INC):
                        regs[x] += 1
                    elif ins.startswith(Instruction.DEC):
                        regs[x] -= 1
                    else:
                        x = x if isinstance(x,int) else regs[x]
                        if out is None or ((out,x) == (0,1)) or ((out,x) == (1,0)):
                            out = x
                        else:
                            break
                else:
                    raise ValueError(f"Invalid instruction: {ins}")
                pc += 1
                t += 1
            if t >= forever:
                return reg_a

    @staticmethod
    def solve_part1(instructions):
        return Day25.solve(instructions)

    @staticmethod
    def solve_part2(input):
        pass


class Instruction:
    CPY = "cpy"
    INC = "inc"
    DEC = "dec"
    JMP = "jnz"
    OUT = "out"


if __name__ == "__main__":
    Day25().solve_all()
