# https://adventofcode.com/2018/day/13
from solutions.challenge import Challenge
from collections import defaultdict


ParsedChallengeInput = tuple[
    dict[tuple[int,int],str],
    int,
    int,
    list[tuple[int,int,str,str]],
]


def draw_grid(
    grid: dict[tuple[int,int],str],
    nrows: int,
    ncols: int,
    carts: list[tuple[int,int,str,str]] = [],
):
    carts = {(y, x): direction for y, x, direction, _ in carts}
    cols = [str(x).rjust(len(str(ncols))) for x in range(ncols)]
    for idx in range(len(str(ncols))):
        print((" " * (len(str(nrows)) + 1)) + "".join(x[idx] for x in cols))
    print("\n".join(f"{str(y).rjust(len(str(nrows)))}:" + "".join(grid[(y, x)] if (y, x) not in carts else carts[(y, x)] for x in range(ncols)) for y in range(nrows)))


def is_collision(
    next_pos: tuple[int,int],
    carts: list[tuple[int,int,str,str]]
):
    return any(next_pos == cart[:2] for cart in carts)


class Day13(Challenge):
    @staticmethod
    def parse_file(lines: list[str]) -> ParsedChallengeInput:
        grid = defaultdict(lambda: " ")
        carts = []
        for y, line in enumerate(lines):
            for x, character in enumerate(line):
                if character in ["^","v","<",">"]:
                    carts.append((y, x, character, "L")) # y, x, direction, next_turn
                    if character in ["^","v"]:
                        grid[(y, x)] = "|"
                    else:
                        grid[(y, x)] = "-"
                elif character != " ":
                    grid[(y, x)] = character
        return grid, len(lines), len(lines[0]), carts

    def read_file(self,filename) -> ParsedChallengeInput:
        return self.parse_file(super().read_file(filename, strip=False))

    @staticmethod
    def solve_part1(
        parsed_input: ParsedChallengeInput,
        find_last_cart_pos: bool = False,
        verbose: bool = False,
        max_iterations: int = 1000,
    ):
        grid, nrows, ncols, carts = parsed_input
        for iteration in range(max_iterations):
            if verbose:
                draw_grid(grid, nrows, ncols, carts)
            crashed = set()
            for idx_cart, (y, x, direction, next_turn) in enumerate(carts):
                if (y, x) in crashed:
                    continue
                match direction:
                    case "^":
                        next_pos = (y-1, x)
                        if is_collision(next_pos, carts):
                            if not find_last_cart_pos:
                                return next_pos[::-1]
                            crashed.add(next_pos)
                        match grid[next_pos]:
                            case "|":
                                carts[idx_cart] = next_pos + (direction, next_turn)
                            case "/":
                                carts[idx_cart] = next_pos + (">", next_turn)
                            case "\\":
                                carts[idx_cart] = next_pos + ("<", next_turn)
                            case "+":
                                match next_turn:
                                    case "L":
                                        carts[idx_cart] = next_pos + ("<", "S")
                                    case "S":
                                        carts[idx_cart] = next_pos + (direction, "R")
                                    case "R":
                                        carts[idx_cart] = next_pos + (">", "L")
                                    case _:
                                        raise Exception(f"Unexpected value for next_turn={next_turn}")
                            case _:
                                raise Exception(f"Unexpected value for grid[{next_pos}]={grid[next_pos]}")
                    case "v":
                        next_pos = (y+1, x)
                        if is_collision(next_pos, carts):
                            if not find_last_cart_pos:
                                return next_pos[::-1]
                            crashed.add(next_pos)
                        match grid[next_pos]:
                            case "|":
                                carts[idx_cart] = next_pos + (direction, next_turn)
                            case "/":
                                carts[idx_cart] = next_pos + ("<", next_turn)
                            case "\\":
                                carts[idx_cart] = next_pos + (">", next_turn)
                            case "+":
                                match next_turn:
                                    case "L":
                                        carts[idx_cart] = next_pos + (">", "S")
                                    case "S":
                                        carts[idx_cart] = next_pos + (direction, "R")
                                    case "R":
                                        carts[idx_cart] = next_pos + ("<", "L")
                                    case _:
                                        raise Exception(f"Unexpected value for next_turn={next_turn}")
                            case _:
                                raise Exception(f"Unexpected value for grid[{next_pos}]={grid[next_pos]}")
                    case "<":
                        next_pos = (y, x-1)
                        if is_collision(next_pos, carts):
                            if not find_last_cart_pos:
                                return next_pos[::-1]
                            crashed.add(next_pos)
                        match grid[next_pos]:
                            case "-":
                                carts[idx_cart] = next_pos + (direction, next_turn)
                            case "/":
                                carts[idx_cart] = next_pos + ("v", next_turn)
                            case "\\":
                                carts[idx_cart] = next_pos + ("^", next_turn)
                            case "+":
                                match next_turn:
                                    case "L":
                                        carts[idx_cart] = next_pos + ("v", "S")
                                    case "S":
                                        carts[idx_cart] = next_pos + (direction, "R")
                                    case "R":
                                        carts[idx_cart] = next_pos + ("^", "L")
                                    case _:
                                        raise Exception(f"Unexpected value for next_turn={next_turn}")
                            case _:
                                raise Exception(f"Unexpected value for grid[{next_pos}]={grid[next_pos]}")
                    case ">":
                        next_pos = (y, x+1)
                        if is_collision(next_pos, carts):
                            if not find_last_cart_pos:
                                return next_pos[::-1]
                            crashed.add(next_pos)
                        match grid[next_pos]:
                            case "-":
                                carts[idx_cart] = next_pos + (direction, next_turn)
                            case "/":
                                carts[idx_cart] = next_pos + ("^", next_turn)
                            case "\\":
                                carts[idx_cart] = next_pos + ("v", next_turn)
                            case "+":
                                match next_turn:
                                    case "L":
                                        carts[idx_cart] = next_pos + ("^", "S")
                                    case "S":
                                        carts[idx_cart] = next_pos + (direction, "R")
                                    case "R":
                                        carts[idx_cart] = next_pos + ("v", "L")
                                    case _:
                                        raise Exception(f"Unexpected value for next_turn={next_turn}")
                            case _:
                                raise Exception(f"Unexpected value for grid[{next_pos}]={grid[next_pos]}")
                    case _:
                        raise Exception(f"Unexpected value for direction={direction}")
            carts = [c for c in carts if (c[0], c[1]) not in crashed]
            if len(carts) == 1:
                if verbose:
                    print(f"Found last cart after {iteration} iterations")
                return carts[0][:2][::-1]
            carts = sorted(carts, key=lambda cart: cart[:2])
        raise Exception("Expected collision to occur but found none")

    @staticmethod
    def solve_part2(
        parsed_input: ParsedChallengeInput,
    ):
        return Day13.solve_part1(parsed_input, find_last_cart_pos=True, max_iterations=15000, verbose=False)


if __name__ == "__main__":
    Day13().solve_all()
