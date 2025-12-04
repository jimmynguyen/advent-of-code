# https://adventofcode.com/2017/day/25
from solutions.challenge import Challenge
import re
from collections import defaultdict


ParsedChallengeInput = tuple[str,int,dict[str,dict[int,tuple[int,str,str]]]]


class Day25(Challenge):
    def read_file(self, filename: str) -> ParsedChallengeInput:
        lines = super().read_file(filename, delimiter="\n\n")
        match = re.search(
            r"Begin in state (.*?).\nPerform a diagnostic checksum after (.*?) steps.",
            lines[0]
        )
        init_state, num_steps = match.group(1), int(match.group(2))
        rules = defaultdict(dict)
        for line in lines[1:]:
            match = re.search(
                r"In state (.*?):\nIf the current value is (.*?):\n- Write the value (.*?)\.\n- Move one slot to the (.*?)\.\n- Continue with state (.*?)\.\nIf the current value is (.*?):\n- Write the value (.*?)\.\n- Move one slot to the (.*?)\.\n- Continue with state (.*?)\.",
                line
            )
            state = match.group(1)
            option1 = int(match.group(2))
            option1_val = int(match.group(3))
            option1_dir = match.group(4)
            option1_nxt = match.group(5)
            option2 = int(match.group(6))
            option2_val = int(match.group(7))
            option2_dir = match.group(8)
            option2_nxt = match.group(9)
            rules[state][option1] = (option1_val, option1_dir, option1_nxt)
            rules[state][option2] = (option2_val, option2_dir, option2_nxt)
        return init_state, num_steps, rules


    @staticmethod
    def solve_part1(
        parsed_input: ParsedChallengeInput,
        find_longest: bool = False,
    ) -> int:
        state, num_steps, rules = parsed_input
        tape = defaultdict(lambda: 0)
        idx_current = 0
        for _ in range(num_steps):
            tape[idx_current], dir, state = rules[state][tape[idx_current]]
            idx_current += {"left": -1, "right": 1}[dir]
        return sum(tape.values())


    @staticmethod
    def solve_part2(
        parsed_input: ParsedChallengeInput,
    ) -> int:
        return Day25.solve_part1(parsed_input, find_longest=True)


if __name__ == "__main__":
    Day25().solve_all()
