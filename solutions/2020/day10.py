# https://adventofcode.com/2020/day/10
from solutions.challenge import Challenge


class Day10(Challenge):
    @staticmethod
    def diff(numbers):
        return [numbers[i+1] - numbers[i] for i in range(len(numbers)-1)]

    @staticmethod
    def solve_1(numbers):
        diffs = Day10.diff(numbers)
        num_diff1 = len([x for x in diffs if x == 1])
        num_diff3 = len([x for x in diffs if x == 3])
        return num_diff1 * num_diff3

    @staticmethod
    def solve_2(nodes):
        adjacency_matrix = dict()
        for node in nodes:
            if node not in adjacency_matrix:
                adjacency_matrix[node] = []
            for i in range(1,4):
                if node + i in nodes:
                    adjacency_matrix[node].append(node+i)
        count = 0
        stack = [[nodes[0]]]
        while len(stack) > 0:
            path = stack.pop()
            if path[-1] == nodes[-1]:
                count += 1
            else:
                for neighbor in adjacency_matrix[path[-1]]:
                    new_path = path.copy()
                    new_path.append(neighbor)
                    stack.append(new_path)
        return count

    @staticmethod
    def solve_2_cheat(adapters):
        # https://github.com/sijmn/aoc2020/blob/master/python/day10.py
        paths = [0] * len(adapters)
        paths[0] = 1
        for i, value in enumerate(adapters[:-1]):
            try:
                if adapters[i + 1] <= value + 3:
                    paths[i + 1] += paths[i]
                if adapters[i + 2] <= value + 3:
                    paths[i + 2] += paths[i]
                if adapters[i + 3] <= value + 3:
                    paths[i + 3] += paths[i]
            except IndexError:
                pass
        return paths[-1]

    @staticmethod
    def solve(numbers,solver):
        numbers = sorted(list(map(int,numbers)))
        numbers = [0] + numbers + [max(numbers) + 3]
        return solver(numbers)

    @staticmethod
    def solve_part1(input):
        return Day10.solve(input,Day10.solve_1)

    @staticmethod
    def solve_part2(input):
        return Day10.solve(input,Day10.solve_2_cheat)


if __name__ == "__main__":
    Day10().solve_all()
