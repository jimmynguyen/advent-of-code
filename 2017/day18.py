# https://adventofcode.com/2017/day/18
from challenge import Challenge
from typing import Sequence


class Day18(Challenge):
    @staticmethod
    def solve_part1(instructions: Sequence[str]) -> int:
        regs = {}
        freq = None
        pc = 0
        while pc < len(instructions):
            ins = instructions[pc]
            op, params = tuple(tuple(x.split()) if " " in x else x for x in ins.split(" ", maxsplit=1))
            if isinstance(params, tuple):
                x, y = params
                y = regs[y] if y in regs else int(y)
                if not x.isnumeric() and x not in regs:
                    regs[x] = 0
                if op == "set":
                    regs[x] = y
                elif op == "add":
                    regs[x] += y
                elif op == "mul":
                    regs[x] *= y
                elif op == "mod":
                    regs[x] %= y
                elif op == "jgz":
                    if (regs[x] if x in regs else int(x)) > 0:
                        pc += y
                        continue
                else:
                    raise ValueError(f"invalid instruction: {ins}")
            else:
                x = params
                x = regs[x] if x in regs else int(x)
                if op == "snd":
                    freq = x
                elif op == "rcv" and x > 0:
                    return freq
            pc += 1

    @staticmethod
    def solve_part2(instructions: Sequence[str]) -> int:
        regs = [{"p": 0}, {"p": 1}]
        freq = [[], []]
        pc = [0, 0]
        num_snds = 0
        while all(x < len(instructions) for x in pc) and not all(instructions[x].startswith("rcv") and len(freq[(i + 1) % len(freq)]) == 0 for i, x in enumerate(pc)):
            for idx_pc in range(len(pc)):
                if pc[idx_pc] >= len(instructions):
                    continue
                ins = instructions[pc[idx_pc]]
                op, params = tuple(tuple(x.split()) if " " in x else x for x in ins.split(" ", maxsplit=1))
                if isinstance(params, tuple):
                    x, y = params
                    y = regs[idx_pc][y] if y in regs[idx_pc] else int(y)
                    if not x.isnumeric() and x not in regs[idx_pc]:
                        regs[idx_pc][x] = 0
                    if op == "set":
                        regs[idx_pc][x] = y
                    elif op == "add":
                        regs[idx_pc][x] += y
                    elif op == "mul":
                        regs[idx_pc][x] *= y
                    elif op == "mod":
                        regs[idx_pc][x] %= y
                    elif op == "jgz":
                        if (regs[idx_pc][x] if x in regs[idx_pc] else int(x)) > 0:
                            pc[idx_pc] += y
                            continue
                    else:
                        raise ValueError(f"invalid instruction: {ins}")
                else:
                    x = params
                    if op == "snd":
                        freq[idx_pc].append(regs[idx_pc][x] if x in regs[idx_pc] else int(x))
                        if idx_pc == 1:
                            num_snds += 1
                    elif op == "rcv":
                        if len(freq[(idx_pc + 1) % len(freq)]) > 0:
                            regs[idx_pc][x] = freq[(idx_pc + 1) % len(freq)].pop(0)
                        else:
                            continue
                pc[idx_pc] += 1
        return num_snds


if __name__ == "__main__":
    Day18().solve_all()
