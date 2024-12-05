# https://adventofcode.com/2021/day/12
from solutions.challenge import Challenge


class Day12(Challenge):
    def read_file(self, filename):
        graph = {}
        for src, dst in [tuple(x.split("-")) for x in super().read_file(filename)]:
            if src not in graph:
                graph[src] = []
            if dst not in graph:
                graph[dst] = []
            graph[src].append(dst)
            graph[dst].append(src)
        return graph

    @staticmethod
    def is_below_small_cave_visit_limit(path, small_cave_visit_limit):
        small_cave_counts = {}
        for small_cave in [x for x in path if x == x.lower()]:
            small_cave_counts[small_cave] = small_cave_counts.get(small_cave, 0) + 1
        return all(x < small_cave_visit_limit for x in small_cave_counts.values())

    @staticmethod
    def solve(graph, small_cave_visit_limit, src = "start", dst = "end"):
        paths = set()
        stack = [(src, [])]
        while len(stack) > 0:
            node, path = stack.pop()
            if node == dst:
                paths.add(tuple(path + [node]))
                continue
            for neighbor in graph[node]:
                new_path = path + [node]
                if neighbor != src \
                    and ( \
                        neighbor == neighbor.upper() \
                        or neighbor not in path \
                        or neighbor == dst \
                        or Day12.is_below_small_cave_visit_limit(new_path, small_cave_visit_limit)):
                    stack += [(neighbor, new_path)]
        return len(paths)

    @staticmethod
    def solve_part1(input):
        return Day12.solve(input, 1)

    @staticmethod
    def solve_part2(input):
        return Day12.solve(input, 2)


if __name__ == "__main__":
    Day12().solve_all()
