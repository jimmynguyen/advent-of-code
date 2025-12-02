# https://adventofcode.com/2018/day/12
from solutions.challenge import Challenge
import re


ParsedChallengeInput = tuple[str,dict[str,str]]


class Day12(Challenge):
    @staticmethod
    def parse_file(lines: list[str]) -> ParsedChallengeInput:
        initial_state = lines[0][len("initial state: "):]
        rules = dict(tuple(re.split(" => ", line)) for line in lines[2:])
        return initial_state, rules

    def read_file(self,filename) -> ParsedChallengeInput:
        return self.parse_file(super().read_file(filename))

    @staticmethod
    def solve_part1(
        parsed_input: ParsedChallengeInput,
        pattern_length: int = 5,
        num_generations: int = 20,
        num_sum_diff_repeats_threshold: int = 100,
        offset: int = -3,
    ):
        initial_state, rules = parsed_input
        # ensure state starts and ends with ...
        current_state = "..." + initial_state + "..."

        sum_plants = lambda state: sum(idx + offset for idx, character in enumerate(state) if character == "#")
        diff_history = []
        curr_sum = sum_plants(current_state)
        for idx_generation in range(num_generations):
            prev_sum = curr_sum
            if idx_generation % 1000 == 0:
                print(idx_generation)
            new_state = "." * len(current_state)
            indexed_patterns = [
                (idx, current_state[idx:idx+pattern_length])
                for idx in range(len(current_state))
                if current_state[idx:idx+pattern_length] in rules
            ]
            for idx, pattern in indexed_patterns:
                new_state = new_state[:idx+2] + rules[pattern] + new_state[idx+3:]
            # ensure state ends with ...
            current_state = new_state.rstrip(".") + "..."
            curr_sum = sum_plants(new_state)
            curr_diff = curr_sum - prev_sum
            if len(diff_history) > 0 and diff_history[-1] == curr_diff:
                diff_history.append(curr_diff)
            else:
                diff_history = [curr_diff]
            if len(diff_history) == num_sum_diff_repeats_threshold:
                break

        return sum_plants(current_state) + curr_diff * (num_generations - idx_generation - 1)

    @staticmethod
    def solve_part2(
        parsed_input: ParsedChallengeInput,
    ):
        return Day12.solve_part1(parsed_input, num_generations=50000000000)


if __name__ == "__main__":
    Day12().solve_all()
