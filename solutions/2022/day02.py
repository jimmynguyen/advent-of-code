# https://adventofcode.com/2022/day/2
from solutions.challenge import Challenge


class Day02(Challenge):
    LOSING_HAND = {
        "R": "S",
        "P": "R",
        "S": "P"
    }
    WINNING_HAND = {v: k for k, v in LOSING_HAND.items()}

    def read_file(self,filename):
        return [tuple(x.split()) for x in super().read_file(filename)]

    @staticmethod
    def compute_outcome_score(hand1, hand2):
        if hand1 == hand2:
            return 3 # draw
        elif hand1 == "R" and hand2 == Day02.LOSING_HAND[hand1] \
            or hand1 == "P" and hand2 == Day02.LOSING_HAND[hand1] \
            or hand1 == "S" and hand2 == Day02.LOSING_HAND[hand1]:
            return 0 # loss
        else:
            return 6 # win

    @staticmethod
    def score_part1_round(part1_round: tuple):
        opponent_hand, hand = part1_round
        opponent_hand = "RPS"["ABC".index(opponent_hand)]
        hand = "RPS"["XYZ".index(hand)]
        hand_score = "RPS".index(hand) + 1
        return hand_score + Day02.compute_outcome_score(opponent_hand, hand)

    @staticmethod
    def score_part2_round(part2_round: tuple):
        opponent_hand, outcome = part2_round
        opponent_hand = "RPS"["ABC".index(opponent_hand)]

        if outcome == "X": # loss
            hand = Day02.LOSING_HAND[opponent_hand]
        elif outcome == "Y": # draw
            hand = opponent_hand
        elif outcome == "Z": # win
            hand = Day02.WINNING_HAND[opponent_hand]
        else:
            raise ValueError(f"Invalid outcome: {outcome}")

        hand_score = "RPS".index(hand) + 1
        return hand_score + Day02.compute_outcome_score(opponent_hand, hand)

    @staticmethod
    def solve(rounds, score_round):
        return sum(map(score_round, rounds))

    @staticmethod
    def solve_part1(input):
        return Day02.solve(input, Day02.score_part1_round)

    @staticmethod
    def solve_part2(input):
        return Day02.solve(input, Day02.score_part2_round)


if __name__ == "__main__":
    Day02().solve_all()
