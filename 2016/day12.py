# https://adventofcode.com/2016/day/12
from challenge import Challenge


class Day12(Challenge):
    @staticmethod
    def solve(instructions,reg_c=0,verbose=False):
        regs = {"a":0,"b":0,"c":reg_c,"d":0}
        pc = 0
        while pc < len(instructions):
            ins = instructions[pc]
            if ins.startswith(Instruction.COPY) or ins.startswith(Instruction.JUMP):
                x,y = tuple(map(lambda x:int(x) if x.isnumeric() or x[1:].isnumeric() else x,ins.replace(Instruction.COPY,"").replace(Instruction.JUMP,"").strip().split(" ")))
                x = x if isinstance(x,int) else regs[x]
                if ins.startswith(Instruction.JUMP):
                    pc += y-1 if x != 0 else 0
                else:
                    regs[y] = x
            elif ins.startswith(Instruction.INCREASE) or ins.startswith(Instruction.DECREASE):
                x = ins.replace(Instruction.INCREASE,"").replace(Instruction.DECREASE,"").strip()
                regs[x] += 1 if ins.startswith(Instruction.INCREASE) else -1
            else:
                raise ValueError(f"Invalid instruction: {ins}")
            pc += 1
        return regs["a"]

    @staticmethod
    def solve_part1(input):
        return Day12.solve(input)

    @staticmethod
    def solve_part2(input):
        return Day12.solve(input,reg_c=1)


class Instruction:
    COPY = "cpy"
    INCREASE = "inc"
    DECREASE = "dec"
    JUMP = "jnz"


if __name__ == "__main__":
    Day12().solve_all()
