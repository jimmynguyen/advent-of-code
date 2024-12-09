# https://adventofcode.com/2023/day/8
import math
from typing import Dict, Tuple
from challenge import Challenge


ParsedChallengeInput = Tuple[str, Dict[str, Tuple[str, str]]]


def count_steps_from_src_to_dst(
    instructions: str,
    network: Dict[str, Tuple[str, str]],
    src_node: str,
    dst_node: str,
) -> int:
    idx = 0
    node = src_node
    num_steps = 0
    skip_first = src_node == dst_node
    while node != dst_node or skip_first:
        if skip_first:
            skip_first = False
        node = network[node]["LR".index(instructions[idx])]
        idx = (idx + 1) % len(instructions)
        num_steps += 1
    return num_steps


class Day08(Challenge):
    def read_file(self, filename: str) -> ParsedChallengeInput:
        instructions, network_lines = tuple(super().read_file(filename, delimiter="\n\n"))
        network = {}
        for line in network_lines.split("\n"):
            node, child_nodes = tuple(line.split(" = "))
            network[node] = tuple(child_nodes[1:-1].split(", "))
        return instructions, network

    @staticmethod
    def solve_part1(input: ParsedChallengeInput) -> int:
        instructions, network = input
        return count_steps_from_src_to_dst(instructions, network, "AAA", "ZZZ")

    @staticmethod
    def solve_part2(input: ParsedChallengeInput) -> int:
        instructions, network = input
        idx = 0
        z_nodes = set(node for node in network.keys() if node[-1] == "Z")
        counts = [count_steps_from_src_to_dst(instructions, network, node, node) for node in z_nodes]
        lcm = counts[0]
        for idx in range(1, len(counts)):
            lcm = math.lcm(lcm, counts[idx])
        return lcm

    @staticmethod
    def solve_part2_bruteforce(input: ParsedChallengeInput) -> int:
        instructions, network = input
        idx = 0
        nodes = set(node for node in network.keys() if node[-1] == "A")
        num_steps = 0
        while not all(node[-1] == "Z" for node in nodes):
            nodes = set(network[node]["LR".index(instructions[idx])] for node in nodes)
            idx = (idx + 1) % len(instructions)
            num_steps += 1
        return num_steps


if __name__ == "__main__":
    Day08().solve_all()
