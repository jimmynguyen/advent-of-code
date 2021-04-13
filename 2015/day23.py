# https://adventofcode.com/2015/day/23
from challenge import Challenge


class Day23(Challenge):
    @staticmethod
    def solve(instructions,reg_a=0,verbose=False):
        regs = {"a":reg_a,"b":0}
        pc = 0
        while pc < len(instructions):
            ins = instructions[pc]
            if verbose: print(pc,ins,regs)
            op,param = tuple(ins.split(" ",maxsplit=1))
            if op == "hlf":
                regs[param] = regs[param]//2
            elif op == "tpl":
                regs[param] *= 3
            elif op == "inc":
                regs[param] += 1
            elif op == "jmp":
                pc += int(param)
                continue
            elif op == "jie":
                r,offset = tuple(param.split(", ",maxsplit=1))
                if regs[r]%2 == 0:
                    pc += int(offset)
                    continue
            elif op == "jio":
                r,offset = tuple(param.split(", ",maxsplit=1))
                if regs[r] == 1:
                    pc += int(offset)
                    continue
            else:
                raise ValueError(f"Invalid operation: {op}")
            pc += 1
        return regs["b"]


    @staticmethod
    def solve_part1(input):
        return Day23.solve(input,reg_a=0)

    @staticmethod
    def solve_part2(input):
        return Day23.solve(input,reg_a=1)


if __name__ == "__main__":
    Day23().solve_all()
