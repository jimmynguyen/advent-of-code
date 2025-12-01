# https://adventofcode.com/2016/day/9
from solutions.challenge import Challenge
import re


class Day09(Challenge):
    @staticmethod
    def get_sequence_length(sequence,recursive=False):
        match = re.search(r"\(\d+x\d+\)",sequence)
        if not match:
            return len(sequence)
        start,end = match.span()
        num_chars,num_repeats = tuple(map(int,sequence[start+1:end-1].split("x")))
        return start + (num_repeats * (Day09.get_sequence_length(sequence[end:end+num_chars],recursive) if recursive else len(sequence[end:end+num_chars]))) + Day09.get_sequence_length(sequence[end+num_chars:],recursive)

    @staticmethod
    def solve_part1(sequence,verbose=False):
        return Day09.get_sequence_length(sequence,recursive=False)

    @staticmethod
    def solve_part2(sequence):
        return Day09.get_sequence_length(sequence,recursive=True)


if __name__ == "__main__":
    Day09().solve_all()
