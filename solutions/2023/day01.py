# https://adventofcode.com/2023/day/1
from solutions.challenge import Challenge


class Day01(Challenge):
    def read_file(self,filename):
        return super().read_file(filename)

    @staticmethod
    def solve(lines,part2=False):
        result = 0
        for line in lines:
            first_digit = None
            last_digit = None
            for idx in range(len(line)):
                c = line[idx]
                if c.isnumeric():
                    if first_digit is None:
                        first_digit = int(c)
                    last_digit = int(c)
                elif part2:
                    for idx_word, word in enumerate(["one","two","three","four","five","six","seven","eight","nine"]):
                        if idx + len(word) <= len(line) and line[idx:idx+len(word)] == word:
                            if first_digit is None:
                                first_digit = idx_word + 1
                            last_digit = idx_word + 1
            result += first_digit * 10 + last_digit
        return result

    @staticmethod
    def solve_part1(input):
        return Day01.solve(input)

    @staticmethod
    def solve_part2(input):
        return Day01.solve(input,part2=True)


if __name__ == "__main__":
    Day01().solve_all()
