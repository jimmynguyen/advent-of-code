# https://adventofcode.com/2024/day/8
from typing import Dict, List, Tuple
from solutions.challenge import Challenge
from itertools import combinations


ParsedChallengeInput = Tuple[List[str], int, int, Dict[str, List[Tuple[int, int]]]]


class Day08(Challenge):
    def read_file(self, filename: str) -> ParsedChallengeInput:
        grid = super().read_file(filename)
        M, N = len(grid), len(grid[0])
        frequency_to_nodes = {}
        for i, row in enumerate(grid):
            for j, frequency in enumerate(row):
                if frequency != ".":
                    if frequency not in frequency_to_nodes:
                        frequency_to_nodes[frequency] = []
                    frequency_to_nodes[frequency].append((i, j))
        return grid, M, N, frequency_to_nodes

    @staticmethod
    def solve_part1(input: ParsedChallengeInput) -> int:
        _, M, N, frequency_to_nodes = input
        antinodes = set()
        for _, nodes in frequency_to_nodes.items():
            possible_node_pairs = [sorted(node_pairs) for node_pairs in combinations(nodes, 2)]
            for node1, node2 in possible_node_pairs:
                x, y = node1[0] - node2[0], node1[1] - node2[1]
                if node1[0] + x >= 0 and node1[0] + x < M and node1[1] + y >= 0 and node1[1] + y < N:
                    antinodes.add((node1[0] + x, node1[1] + y))
                if node2[0] - x >= 0 and node2[0] - x < M and node2[1] - y >= 0 and node2[1] - y < N:
                    antinodes.add((node2[0] - x, node2[1] - y))
        return len(antinodes)


    @staticmethod
    def solve_part2(input: ParsedChallengeInput) -> int:
        _, M, N, frequency_to_nodes = input
        antinodes = set()
        for _, nodes in frequency_to_nodes.items():
            possible_node_pairs = [sorted(node_pairs) for node_pairs in combinations(nodes, 2)]
            for node1, node2 in possible_node_pairs:
                antinodes.add(node1)
                antinodes.add(node2)
                x, y = node1[0] - node2[0], node1[1] - node2[1]
                node = node1
                while node[0] + x >= 0 and node[0] + x < M and node[1] + y >= 0 and node[1] + y < N:
                    antinodes.add((node[0] + x, node[1] + y))
                    node = (node[0] + x, node[1] + y)
                node = node1
                while node[0] - x >= 0 and node[0] - x < M and node[1] - y >= 0 and node[1] - y < N:
                    antinodes.add((node[0] - x, node[1] - y))
                    node = (node[0] - x, node[1] - y)
                node = node2
                while node[0] + x >= 0 and node[0] + x < M and node[1] + y >= 0 and node[1] + y < N:
                    antinodes.add((node[0] + x, node[1] + y))
                    node = (node[0] + x, node[1] + y)
                node = node2
                while node[0] - x >= 0 and node[0] - x < M and node[1] - y >= 0 and node[1] - y < N:
                    antinodes.add((node[0] - x, node[1] - y))
                    node = (node[0] - x, node[1] - y)
        return len(antinodes)


if __name__ == "__main__":
    Day08().solve_all()
