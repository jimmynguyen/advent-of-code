# https://adventofcode.com/2018/day/9
from solutions.challenge import Challenge
import re
from collections import deque, defaultdict


ParsedChallengeInput = tuple[int,int]


def print_circle(
    circle: list[int],
    idx_current: int,
    player: int
):
    circle_str = f"[{player}] "
    for idx, marble in enumerate(circle):
        if idx == idx_current:
            circle_str += f"({marble}) "
        else:
            circle_str += f"{marble} "
    circle_str = circle_str[:-1]
    print(circle_str)


class Day09(Challenge):
    @staticmethod
    def parse_file(line: str) -> ParsedChallengeInput:
        pattern = r"(\d*?) players; last marble is worth (\d*?) points"
        match = re.search(pattern, line)
        return int(match.group(1)), int(match.group(2))

    def read_file(self,filename) -> ParsedChallengeInput:
        return self.parse_file(super().read_file(filename))

    @staticmethod
    def solve_part1(
        parsed_input: ParsedChallengeInput,
        verbose: bool = False,
    ):
        if verbose:
            print(parsed_input)
        num_players, last_marble = parsed_input
        circle = deque([0])
        player_scores = defaultdict(int)
        for marble in range(1, last_marble+1):
            player = marble % num_players
            if marble % 23 == 0:
                circle.rotate(7)
                player_scores[player] += marble + circle.pop()
                circle.rotate(-1)
            else:
                circle.rotate(-1)
                circle.append(marble)
            if verbose:
                print_circle(circle, len(circle) - 1, player)

        if verbose:
            print("player_scores:", player_scores)

        return max(player_scores.values())

    @staticmethod
    def solve_part2(
        parsed_input: ParsedChallengeInput,
        last_marble_multiplier: int = 100,
        verbose: bool = False,
    ):
        num_players, last_marble = parsed_input
        return Day09.solve_part1((num_players, last_marble * last_marble_multiplier), verbose)


if __name__ == "__main__":
    Day09().solve_all()
