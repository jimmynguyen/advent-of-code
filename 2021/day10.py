# https://adventofcode.com/2021/day/10
from challenge import Challenge


class Day10(Challenge):
    CHARACTER_MATCH = {"(": ")", "[": "]", "{": "}", "<": ">"}

    @staticmethod
    def parse_navigation_subsystem(navigation_subsystem):
        expected_characters_list = []
        syntax_errors = []
        for line in navigation_subsystem:
            expected_characters = []
            syntax_error = None
            for character in line:
                if character in "([{<":
                    expected_characters.append(Day10.CHARACTER_MATCH[character])
                elif character in ")]}>":
                    if len(expected_characters) == 0 or expected_characters[-1] != character:
                        syntax_error = character
                        break
                    else:
                        expected_characters.pop()
                else:
                    raise Exception(f"Unexpected character: {character}")
            if syntax_error is None:
                expected_characters_list.append(list(reversed(expected_characters)))
            else:
                syntax_errors.append(syntax_error)
        return syntax_errors, expected_characters_list

    @staticmethod
    def compute_syntax_error_score(syntax_errors, _):
        character_points = {")": 3, "]": 57, "}": 1197, ">": 25137}
        return sum(character_points[character] for character in syntax_errors)

    @staticmethod
    def compute_middle_score(_, expected_characters_list):
        character_points = {x: 1 + i for i, x in enumerate(")]}>")}
        scores = []
        for expected_characters in expected_characters_list:
            score = 0
            for character in expected_characters:
                score = score * 5 + character_points[character]
            scores.append(score)
        return sorted(scores)[len(scores) // 2]

    @staticmethod
    def solve(navigation_subsystem, solve_function):
        syntax_errors, expected_characters_list = Day10.parse_navigation_subsystem(navigation_subsystem)
        return solve_function(syntax_errors, expected_characters_list)

    @staticmethod
    def solve_part1(input):
        return Day10.solve(input, Day10.compute_syntax_error_score)

    @staticmethod
    def solve_part2(input):
        return Day10.solve(input, Day10.compute_middle_score)


if __name__ == "__main__":
    Day10().solve_all()
