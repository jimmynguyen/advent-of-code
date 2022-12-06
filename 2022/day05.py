# https://adventofcode.com/2022/day/5
from typing import Dict, List, Tuple
from challenge import Challenge
from collections import defaultdict, namedtuple

Instruction = namedtuple("Instruction", ["num_crates", "src_stack", "dst_stack"])

class Day05(Challenge):
    def read_file(self, filename: str) -> Tuple[Dict[int, List[str]], List[Instruction]]:
        stack_rows, procedure = tuple(x.split("\n") for x in super().read_file(filename, delimiter="\n\n", strip=False))

        stack_dict = defaultdict(list)
        stack_ids = list(map(int, stack_rows[-1].split()))
        for stack_row in stack_rows[:-1]:
            for idx, (start, end) in enumerate(zip(range(0, len(stack_row), 4), range(3, len(stack_row) + 1, 4))):
                crate = stack_row[start:end].strip()
                if len(crate) > 0:
                    stack_dict[stack_ids[idx]].insert(0, crate[1])
        stack_dict = {k: v for k, v in sorted(stack_dict.items(), key=lambda x: x[0])}

        instructions = []
        for step in procedure:
            num_crates, src_to_dst = tuple(step.lstrip("move ").split(" from "))
            src_stack, dst_stack = tuple(map(int, src_to_dst.split(" to ")))
            instructions.append(Instruction(int(num_crates), src_stack, dst_stack))

        return stack_dict, instructions

    @staticmethod
    def solve(input: Tuple[Dict[int, List[str]], List[Instruction]], move_multiple_crates: bool) -> str:
        stack_dict, instructions = input
        for instruction in instructions:
            crates = [stack_dict[instruction.src_stack].pop() for _ in range(instruction.num_crates)]
            if move_multiple_crates:
                crates = reversed(crates)
            stack_dict[instruction.dst_stack] += crates
        return "".join(stack[-1] for _, stack in stack_dict.items())

    @staticmethod
    def solve_part1(input: Tuple[Dict[int, List[str]], List[Instruction]]) -> str:
        return Day05.solve(input, move_multiple_crates=False)

    @staticmethod
    def solve_part2(input: Tuple[Dict[int, List[str]], List[Instruction]]) -> str:
        return Day05.solve(input, move_multiple_crates=True)


if __name__ == "__main__":
    Day05().solve_all()
