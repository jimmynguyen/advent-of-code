# https://adventofcode.com/2016/day/23
from solutions.challenge import Challenge


class Day23(Challenge):
    @staticmethod
    def simplify_instructions(instructions):
        return instructions[:2] + [
                "mul a a b",
                "mul c 2 b",
                "noop",
                "dec b",
                instructions[16],
                "cpy -6 c"
            ] + instructions[18:21] + [
                "mul c c d",
                "noop",
                "add a a c"
            ]

    @staticmethod
    def solve(instructions,reg_a,simplify,verbose=False):
        if simplify:
            instructions = Day23.simplify_instructions(instructions)
        regs = {"a":reg_a,"b":0,"c":0,"d":0}
        toggled = set()
        pc = 0
        while pc < len(instructions):
            ins = instructions[pc]
            if verbose: print(pc,ins,toggled,regs)
            if ins.startswith(Instruction.CPY) or ins.startswith(Instruction.JMP):
                x,y = tuple(map(lambda x:int(x) if x.isnumeric() or x[1:].isnumeric() else x,ins.replace(Instruction.CPY,"").replace(Instruction.JMP,"").strip().split(" ")))
                x = x if isinstance(x,int) else regs[x]
                is_jmp = ins.startswith(Instruction.JMP)
                if (pc not in toggled and is_jmp) or (pc in toggled and not is_jmp):
                    y = y if isinstance(y,int) else regs[y]
                    pc += y-1 if x != 0 else 0
                elif y in regs:
                    regs[y] = x
            elif ins.startswith(Instruction.INC) or ins.startswith(Instruction.DEC) or (pc in toggled and ins.startswith(Instruction.TGL)):
                x = ins.replace(Instruction.INC,"").replace(Instruction.DEC,"").replace(Instruction.TGL,"").strip()
                is_inc = ins.startswith(Instruction.INC)
                if (pc not in toggled and is_inc) or (pc in toggled and not is_inc):
                    regs[x] += 1
                else:
                    regs[x] -= 1
            elif ins.startswith(Instruction.TGL):
                x = ins.replace(Instruction.TGL,"").strip()
                x = int(x) if x.isnumeric() else regs[x]
                toggled.add(pc+x)
            elif ins.startswith(Instruction.ADD) or ins.startswith(Instruction.MUL):
                x,y,z = tuple(ins.replace(Instruction.ADD,"").replace(Instruction.MUL,"").strip().split(" "))
                y = int(y) if y.isnumeric() else regs[y]
                z = int(z) if z.isnumeric() else regs[z]
                if ins.startswith(Instruction.MUL):
                    regs[x] = y*z
                else:
                    regs[x] = y+z
            elif ins.startswith(Instruction.NOOP):
                pass
            else:
                raise ValueError(f"Invalid instruction: {ins}")
            pc += 1
        return regs["a"]

    @staticmethod
    def solve_part1(instructions,reg_a=7,simplify=True):
        return Day23.solve(instructions,reg_a,simplify)

    @staticmethod
    def solve_part2(instructions,reg_a=12,simplify=True):
        return Day23.solve(instructions,reg_a,simplify)


class Instruction:
    CPY = "cpy"
    INC = "inc"
    DEC = "dec"
    JMP = "jnz"
    TGL = "tgl"
    ADD = "add"
    MUL = "mul"
    NOOP = "noop"


if __name__ == "__main__":
    Day23().solve_all()
