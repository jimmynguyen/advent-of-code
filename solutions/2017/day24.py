# https://adventofcode.com/2017/day/24
from solutions.challenge import Challenge
from collections import deque


ParsedChallengeInput = set[tuple[int,int]]


class Day24(Challenge):
    def read_file(self, filename: str) -> ParsedChallengeInput:
        return {tuple(map(int, line.split("/"))) for line in super().read_file(filename)}


    @staticmethod
    def solve_part1(
        parsed_input: ParsedChallengeInput,
        find_longest: bool = False,
    ) -> int:
        components = parsed_input
        compute_strength = lambda bridge: sum(sum(component) for component in bridge)
        queue = deque(((component,), {component}) for component in components if component[0] == 0)
        best_bridge = None
        while len(queue) > 0:
            bridge, visited = queue.pop()
            remaining_components = components.difference(visited)
            if best_bridge is None \
                or find_longest and len(best_bridge) < len(bridge) \
                or (not find_longest or len(best_bridge) == len(bridge)) and compute_strength(best_bridge) < compute_strength(bridge):
                best_bridge = bridge
            for component in remaining_components:
                available_port = bridge[-1][1] if len(bridge) == 1 else bridge[-1][0] if bridge[-1][0] == bridge[-1][1] else [port for port in bridge[-1] if port not in bridge[-2]][0]
                if any(x == available_port for x in component):
                    queue.append((bridge + (component,), visited.union({component})))
        return compute_strength(best_bridge)


    @staticmethod
    def solve_part2(
        parsed_input: ParsedChallengeInput,
    ) -> int:
        return Day24.solve_part1(parsed_input, find_longest=True)


if __name__ == "__main__":
    Day24().solve_all()
