# https://adventofcode.com/2020/day/5
from challenge import Challenge


class Day05(Challenge):
    @staticmethod
    def find_seat(seat_ids):
        seat_ids = set(sorted(seat_ids))
        all_seat_ids = set(range(min(seat_ids),max(seat_ids)))
        remaining = list(all_seat_ids.difference(seat_ids))
        return remaining[0]

    @staticmethod
    def solve(tickets,find_seat):
        seat_ids = []
        for ticket in tickets:
            rows = list(range(128))
            cols = list(range(8))
            for c in ticket:
                if c == "F":
                    rows = rows[:len(rows)//2]
                elif c == "B":
                    rows = rows[len(rows)//2:]
                elif c == "L":
                    cols = cols[:len(cols)//2]
                elif c == "R":
                    cols = cols[len(cols)//2:]
            seat_ids.append(rows[0] * 8 + cols[0])
        return find_seat(seat_ids)

    @staticmethod
    def solve_part1(input):
        return Day05.solve(input,max)

    @staticmethod
    def solve_part2(input):
        return Day05.solve(input,Day05.find_seat)


if __name__ == "__main__":
    Day05().solve_all()
