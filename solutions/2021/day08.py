# https://adventofcode.com/2021/day/8
from solutions.challenge import Challenge


class Day08(Challenge):
    DIGIT_TO_SEGMENTS = ["abcefg", "cf", "acdeg", "acdfg", "bcdf", "abdfg", "abdefg", "acf", "abcdefg", "abcdfg"]

    def read_file(self, filename):
        return [(y.split(), z.split()) for x in super().read_file(filename) for y, z in [tuple(x.split(" | "))]]

    @staticmethod
    def get_original_segments(digit):
        return set(Day08.DIGIT_TO_SEGMENTS[digit])

    @staticmethod
    def get_current_segments(segments_list, original_segments):
        return set([x for x in segments_list if len(x) == len(original_segments)][0])

    @staticmethod
    def get_segment_map(segments_list):
        segment_map = {x: set() for x in Day08.DIGIT_TO_SEGMENTS[8]}
        for digit, difference_digits in [(1, []), (7, [1]), (4, [1]), (8, [7, 4])]:
            original_segments = Day08.get_original_segments(digit)
            current_segments = Day08.get_current_segments(segments_list, original_segments)
            for difference_digit in difference_digits:
                difference_original_segments = Day08.get_original_segments(difference_digit)
                difference_current_segments = Day08.get_current_segments(segments_list, difference_original_segments)
                original_segments = original_segments.difference(difference_original_segments)
                current_segments = current_segments.difference(difference_current_segments)
            for x in original_segments:
                segment_map[x] = segment_map[x].union(current_segments)
        return segment_map

    @staticmethod
    def get_possible_segments_map(segments_list):
        segment_map = Day08.get_segment_map(segments_list)
        possible_segments_map = [set() for _ in range(len(Day08.DIGIT_TO_SEGMENTS))]
        for i, original_segment in enumerate(Day08.DIGIT_TO_SEGMENTS):
            possible_segments = []
            for x in original_segment:
                if len(possible_segments) == 0:
                    possible_segments += [y for y in segment_map[x]]
                else:
                    new_possible_segments = []
                    for possible_segment in possible_segments:
                        for y in segment_map[x]:
                            if y not in possible_segment:
                                new_possible_segments.append(''.join(sorted(possible_segment + y)))
                    possible_segments = new_possible_segments
            possible_segments_map[i].update(possible_segments)
        return possible_segments_map

    @staticmethod
    def solve(input, part1):
        output = 0
        for segments_list, digit_segments_list in input:
            if part1:
                digit_to_segments_length = [len(x) for x in Day08.DIGIT_TO_SEGMENTS]
                segments_list = [sorted(x) for x in segments_list]
                digit_segments_list = [sorted(x) for x in digit_segments_list]
                for segments in segments_list:
                    if digit_to_segments_length.count(len(segments)) == 1 and segments in digit_segments_list:
                        output += digit_segments_list.count(segments)
            else:
                possible_segments_map = Day08.get_possible_segments_map(segments_list)
                for digit_place, digit_segment in enumerate(reversed(digit_segments_list)):
                    digit_segment = ''.join(sorted(digit_segment))
                    digit = None
                    for i, possible_segments in enumerate(possible_segments_map):
                        for possible_segment in possible_segments:
                            if digit_segment == possible_segment:
                                digit = i
                                break
                        if digit is not None:
                            break
                    output += digit * 10**digit_place
        return output


    @staticmethod
    def solve_part1(input):
        return Day08.solve(input, True)

    @staticmethod
    def solve_part2(input):
        return Day08.solve(input, False)


if __name__ == "__main__":
    Day08().solve_all()
