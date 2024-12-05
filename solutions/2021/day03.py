# https://adventofcode.com/2021/day/3
from solutions.challenge import Challenge


class Day03(Challenge):
    @staticmethod
    def compute_product(a, b):
        return int(a, 2) * int(b, 2)

    @staticmethod
    def solve_part1(report_entries):
        dict_by_index = {}
        for entry in report_entries:
            for index, bit in enumerate(entry):
                if index not in dict_by_index:
                    dict_by_index[index] = {"0": 0, "1": 0}
                dict_by_index[index][bit] += 1
        gamma_rate, epsilon_rate = "", ""
        for index in dict_by_index.keys():
            max_bit_count = max(dict_by_index[index].values())
            gamma_rate += [bit for bit, count in dict_by_index[index].items() if count == max_bit_count][0]
            epsilon_rate += "1" if gamma_rate[-1] == "0" else "0"
        return Day03.compute_product(gamma_rate, epsilon_rate)

    @staticmethod
    def get_bit_count_map_by_index(report_entries, index):
        bit_count_map = {"0": 0, "1": 0}
        for entry in report_entries:
            bit_count_map[entry[index]] += 1
        return bit_count_map

    @staticmethod
    def get_common_bit_by_function(bit_count_map, filter_function, default_bit):
        bit_count = filter_function(bit_count_map.values())
        bits = [bit for bit, count in bit_count_map.items() if count == bit_count]
        if len(bits) > 1:
            return default_bit
        return bits[0]

    @staticmethod
    def get_rate(report_entries, filter_function, default_bit):
        index = 0
        while len(report_entries) > 1:
            bit_count_map = Day03.get_bit_count_map_by_index(report_entries, index)
            max_count_bit = Day03.get_common_bit_by_function(bit_count_map, filter_function, default_bit)
            report_entries = list(filter(lambda entry: entry[index] == max_count_bit, report_entries))
            index += 1
        return report_entries[0]

    @staticmethod
    def solve_part2(report_entries):
        oxygen_rate = Day03.get_rate([x for x in report_entries], max, "1")
        co2_rate = Day03.get_rate([x for x in report_entries], min, "0")
        return Day03.compute_product(oxygen_rate, co2_rate)


if __name__ == "__main__":
    Day03().solve_all()
