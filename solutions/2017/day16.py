# https://adventofcode.com/2017/day/16
from solutions.challenge import Challenge
from typing import Sequence


class Day16(Challenge):
    def read_file(self, filename) -> Sequence[str]:
        return super().read_file(filename).split(",")

    @staticmethod
    def dance(instructions: Sequence[str], initial_state: Sequence[str]) -> Sequence[str]:
        state = [x for x in initial_state]
        for ins in instructions:
            if ins.startswith("s"):
                x = int(ins[1:])
                state = state[-x:] + state[:-x]
            elif ins.startswith("x"):
                x, y = tuple(map(int, ins[1:].split("/")))
                state[x], state[y] = state[y], state[x]
            elif ins.startswith("p"):
                x, y = tuple(ins[1:].split("/"))
                x, y = state.index(x), state.index(y)
                state[x], state[y] = state[y], state[x]
            else:
                raise ValueError(f"invalid instruction: {ins}")
        return state

    @staticmethod
    def solve_part1(instructions: Sequence[str], num_programs: int=16, num_dances: int=1) -> int:
        state = [chr(i + ord("a")) for i in range(num_programs)]
        history = []
        for _ in range(num_dances):
            if state in history:
                state = history[1000000000 % len(history)]
                break
            history.append(state)
            state = Day16.dance(instructions, state)
        return "".join(state)

    @staticmethod
    def solve_part2(instructions: Sequence[str], num_programs: int=16, num_dances: int=int(1e9)) -> int:
        return Day16.solve_part1(instructions, num_programs=num_programs, num_dances=num_dances)


if __name__ == "__main__":
    Day16().solve_all()
