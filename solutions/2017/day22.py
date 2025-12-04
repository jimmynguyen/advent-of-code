# https://adventofcode.com/2017/day/22
from solutions.challenge import Challenge
from collections import defaultdict


def turn(
    node: str,
    dir: str,
):
    match node:
        case "#":
            match dir:
                case "^":
                    return ">"
                case ">":
                    return "v"
                case "v":
                    return "<"
                case "<":
                    return "^"
                case _:
                    raise Exception(f"Found unexpected dir={dir}")
        case ".":
            match dir:
                case "^":
                    return "<"
                case "<":
                    return "v"
                case "v":
                    return ">"
                case ">":
                    return "^"
                case _:
                    raise Exception(f"Found unexpected dir={dir}")
        case "W":
            return dir
        case "F":
            match dir:
                case "^":
                    return "v"
                case "v":
                    return "^"
                case "<":
                    return ">"
                case ">":
                    return "<"
                case _:
                    raise Exception(f"Found unexpected dir={dir}")
        case _:
            raise Exception(f"Found unexpected node={node}")


def draw_grid(
    grid: dict[tuple[int,int],str],
):
    x_min = min(x for _, x in grid.keys())
    x_max = max(x for _, x in grid.keys())
    y_min = min(y for y, _ in grid.keys())
    y_max = max(y for y, _ in grid.keys())
    print("\n".join("".join(grid[(y, x)] for x in range(x_min, x_max + 1)) for y in range(y_min, y_max + 1)) + "\n")


class Day22(Challenge):
    def read_file(self, filename: str) -> tuple[dict[tuple[int,int],str],int]:
        lines = super().read_file(filename)
        grid = defaultdict(lambda: ".")
        for y, line in enumerate(lines):
            for x, character in enumerate(line):
                grid[(y, x)] = character
        return grid, len(lines)


    @staticmethod
    def solve(
        parsed_input: tuple[dict[tuple[int,int],str],int],
        num_iterations: int = 10000,
        part2: bool = False,
        verbose: bool = False,
    ) -> int:
        grid, grid_size = parsed_input
        if verbose:
            draw_grid(grid)
        pos = (grid_size // 2, grid_size // 2)
        dir = "^"
        infection_count = 0
        for _ in range(num_iterations):
            dir = turn(grid[pos], dir)
            grid[pos] = {".": "#", "#": "."}[grid[pos]] if not part2 else {".": "W", "W": "#", "#": "F", "F": "."}[grid[pos]]
            infection_count += 1 if grid[pos] == "#" else 0
            pos = (pos[0] + defaultdict(lambda: 0, {"^": -1, "v": 1})[dir], pos[1] + defaultdict(lambda: 0, {">": 1, "<": -1})[dir])
            if verbose:
                draw_grid(grid)
        return infection_count


    @staticmethod
    def solve_part1(
        parsed_input: tuple[dict[tuple[int,int],str],int],
        num_iterations: int = 10000,
    ) -> int:
        return Day22.solve(parsed_input, num_iterations=num_iterations)


    @staticmethod
    def solve_part2(
        parsed_input: tuple[dict[tuple[int,int],str],int],
        num_iterations: int = 10000000,
    ) -> int:
        return Day22.solve(parsed_input, num_iterations=num_iterations, part2=True)


if __name__ == "__main__":
    Day22().solve_all()
