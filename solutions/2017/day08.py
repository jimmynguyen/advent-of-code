# https://adventofcode.com/2017/day/8
from solutions.challenge import Challenge
from math import inf


class Day08(Challenge):
    def read_file(self,filename):
        return [tuple(y.split() for y in x.split(" if ")) for x in super().read_file(filename)]

    @staticmethod
    def solve_part1(instructions,final_max=True):
        regs = {}
        max_reg_val = -inf
        for (ins_reg,ins_op,ins_val),(cond_reg,cond_op,cond_val) in instructions:
            if ins_reg not in regs:
                regs[ins_reg] = 0
            if cond_reg not in regs:
                regs[cond_reg] = 0

            ins_val = int(ins_val)
            cond_val = int(cond_val)

            if cond_op == "==":
                cond = regs[cond_reg] == cond_val
            elif cond_op == "<":
                cond = regs[cond_reg] < cond_val
            elif cond_op == ">":
                cond = regs[cond_reg] > cond_val
            elif cond_op == "<=":
                cond = regs[cond_reg] <= cond_val
            elif cond_op == ">=":
                cond = regs[cond_reg] >= cond_val
            elif cond_op == "!=":
                cond = regs[cond_reg] != cond_val
            else:
                raise ValueError(f"invalid condition operator: {cond_op}")

            if cond:
                if ins_op == "inc":
                    regs[ins_reg] += ins_val
                elif ins_op == "dec":
                    regs[ins_reg] -= ins_val
                else:
                    raise ValueError(f"invalid condition operator: {ins_op}")
            if not final_max:
                max_reg_val = max(max_reg_val,max(regs.values()))
        return max(regs.values()) if final_max else max_reg_val

    @staticmethod
    def solve_part2(instructions):
        return Day08.solve_part1(instructions,final_max=False)


if __name__ == "__main__":
    Day08().solve_all()
