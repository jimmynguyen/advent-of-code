# https://adventofcode.com/2023/day/2
from solutions.challenge import Challenge


class Day02(Challenge):
    def read_file(self,filename):
        return super().read_file(filename)

    @staticmethod
    def solve_part1(lines):
        result = 0
        for line in lines:
            id, draws = line[len("Game "):].split(": ")
            id = int(id)
            invalid = False
            for draw in draws.split("; "):
                red_count, grn_count, blu_count = 12, 13, 14
                for color_count in draw.split(", "):
                    count, color = color_count.split(" ")
                    count = int(count)

                    if color == "red":
                        red_count -= count
                    elif color == "green":
                        grn_count -= count
                    elif color == "blue":
                        blu_count -= count
                    else:
                        raise Exception(f"unexpected color: {color}")

                    if any([x < 0 for x in [red_count, grn_count, blu_count]]):
                        invalid = True
                        break
                if invalid:
                    break
            if not invalid:
                result += id
        return result

    @staticmethod
    def solve_part2(lines):
        result = 0
        for line in lines:
            id, draws = line[len("Game "):].split(": ")
            id = int(id)
            min_red_required, min_grn_required, min_blu_required = 0, 0, 0
            for draw in draws.split("; "):
                for color_count in draw.split(", "):
                    count, color = color_count.split(" ")
                    count = int(count)

                    if color == "red":
                        min_red_required = max(min_red_required, count)
                    elif color == "green":
                        min_grn_required = max(min_grn_required, count)
                    elif color == "blue":
                        min_blu_required = max(min_blu_required, count)
                    else:
                        raise Exception(f"unexpected color: {color}")
            result += min_red_required * min_grn_required * min_blu_required
        return result


if __name__ == "__main__":
    Day02().solve_all()
