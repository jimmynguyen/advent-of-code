# https://adventofcode.com/2023/day/6
from typing import List
from solutions.challenge import Challenge


ParsedChallengeInput = List[str]


class Day06(Challenge):
    def read_file(self, filename: str) -> ParsedChallengeInput:
        return super().read_file(filename)

    @staticmethod
    def solve_part1(input: ParsedChallengeInput) -> int:
        durations, distances = tuple(list(map(int, line.split(":")[1].strip().split())) for line in input)
        result = 1
        for duration, distance in zip(durations, distances):
            for hold_duration in range(0, duration + 1):
                speed = hold_duration
                traveled_distance = speed * (duration - hold_duration)
                if traveled_distance > distance:
                    min_duration = hold_duration
                    break
            for hold_duration in range(duration, min_duration, -1):
                speed = hold_duration
                traveled_distance = speed * (duration - hold_duration)
                if traveled_distance > distance:
                    max_duration = hold_duration
                    break
            num_wins = max_duration - min_duration + 1
            result *= num_wins
        return result


    @staticmethod
    def solve_part2(input: ParsedChallengeInput) -> int:
        duration, distance = tuple(int(line.split(":")[1].strip().replace(" ", "")) for line in input)
        for hold_duration in range(0, duration + 1):
            speed = hold_duration
            traveled_distance = speed * (duration - hold_duration)
            if traveled_distance > distance:
                min_duration = hold_duration
                break
        for hold_duration in range(duration, min_duration, -1):
            speed = hold_duration
            traveled_distance = speed * (duration - hold_duration)
            if traveled_distance > distance:
                max_duration = hold_duration
                break
        return max_duration - min_duration + 1


if __name__ == "__main__":
    Day06().solve_all()
