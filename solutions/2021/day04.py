# https://adventofcode.com/2021/day/4
from solutions.challenge import Challenge


class Day04(Challenge):
    def read_file(self, filename):
        lines = super().read_file(filename, delimiter="\n\n")
        random_numbers = list(map(int, lines[0].split(",")))
        visited = {}
        for line in lines[1:]:
            board = tuple(tuple(int(y) for y in x.split()) for x in line.split("\n"))
            visited[board] = [[False for _ in x] for x in board]
        return random_numbers, visited

    @staticmethod
    def is_bingo(visited_board):
        if any(all(x) for x in visited_board):
            return True
        cols = [[] for _ in visited_board[0]]
        for col_index, _ in enumerate(visited_board[0]):
            for row in visited_board:
                cols[col_index].append(row[col_index])
        return any(all(x) for x in cols)

    @staticmethod
    def compute_score(board, visited, n):
        score = 0
        for row_index, visited_row in enumerate(visited):
            for col_index, visited_col in enumerate(visited_row):
                if not visited_col:
                    score += board[row_index][col_index]
        return score * n

    @staticmethod
    def solve(input, winner_place):
        random_numbers, visited = input
        boards_won = []
        for n in random_numbers:
            for board in visited.keys():
                if board in boards_won:
                    continue
                for row_index, row in enumerate(board):
                    for col_index, col in enumerate(row):
                        if col == n:
                            visited[board][row_index][col_index] = True
                if Day04.is_bingo(visited[board]):
                    if len(boards_won) == winner_place - 1:
                        return Day04.compute_score(board, visited[board], n)
                    boards_won.append(board)

    @staticmethod
    def solve_part1(input):
        return Day04.solve(input, 1)

    @staticmethod
    def solve_part2(input):
        return Day04.solve(input, len(input[1].keys()))


if __name__ == "__main__":
    Day04().solve_all()
