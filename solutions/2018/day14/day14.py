# https://adventofcode.com/2018/day/14
from solutions.challenge import Challenge


ParsedChallengeInput = str


def print_board(
    board: list[int],
    pos: tuple[int,int],
):
    print("".join(f" {score} " if idx not in pos else f"({score})" if idx == pos[0] else f"[{score}]" for idx, score in enumerate(board)))


class Day14(Challenge):
    def read_file(self,filename) -> ParsedChallengeInput:
        return super().read_file(filename)


    @staticmethod
    def solve_part1(
        parsed_input: ParsedChallengeInput,
        num_recipes_offset: int = 10,
        verbose: bool = False,
        part2: bool = False,
    ):
        if not part2:
            num_recipes = int(parsed_input)
        else:
            pattern = list(map(int, parsed_input))
        board = [3,7]
        pos = (0, 1)
        if verbose:
            print_board(board, pos)
        while part2 or len(board) < num_recipes + num_recipes_offset:
            idx1, idx2 = pos
            board += list(map(int, str(board[idx1] + board[idx2])))
            pos = ((idx1 + board[idx1] + 1) % len(board), (idx2 + board[idx2] + 1) % len(board))
            if verbose:
                print_board(board, pos)
            if part2:
                if len(board) > len(pattern) and board[-len(pattern):] == pattern:
                    return len(board[:-len(pattern)])
                elif len(board)-1 > len(pattern) and board[-len(pattern)-1:-1] == pattern:
                    return len(board[:-len(pattern)-1])
        return "".join(str(score) for score in board[num_recipes:num_recipes+num_recipes_offset])


    @staticmethod
    def solve_part2(
        parsed_input: ParsedChallengeInput,
    ):
        return Day14.solve_part1(parsed_input, part2=True)


if __name__ == "__main__":
    Day14().solve_all()
