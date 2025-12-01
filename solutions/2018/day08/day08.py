# https://adventofcode.com/2018/day/8
from solutions.challenge import Challenge
from typing import Self


class Node:
    num_children: int
    num_metadata_entries: int
    children: list[Self]
    metadata: list[int]

    def __init__(self, num_children: int, num_metadata_entries: int, children: list[Self], metadata: list[int]):
        self.num_children = num_children
        self.num_metadata_entries = num_metadata_entries
        self.children = children
        self.metadata = metadata


    def _to_str(self, indent_size: int = 0) -> str:
        base_indent = " " * indent_size
        child_indent = base_indent + "  "

        node_str = f"{base_indent}Node{{\n" \
            + f"{child_indent}metadata={self.metadata}\n" \
            + f"{child_indent}children={{\n"

        for child in self.children:
            node_str += child._to_str(indent_size + 4)

        node_str += f"{child_indent}}}\n" \
            + f"{base_indent}}} \n"

        return node_str


    def __str__(self) -> str:
        return self._to_str()


def parse_node(parsed_input: list[int]) -> Node:
    num_children = parsed_input.pop(0)
    num_metadata_entries = parsed_input.pop(0)

    children = []
    for _ in range(num_children):
        child, parsed_input = parse_node(parsed_input)
        children.append(child)

    metadata = parsed_input[:num_metadata_entries]
    parsed_input = parsed_input[num_metadata_entries:]

    return Node(num_children, num_metadata_entries, children, metadata), parsed_input


def compute_node_value(node: Node) -> int:
    if len(node.children) == 0:
        return sum(node.metadata)

    node_value = 0
    for metadatum in node.metadata:
        if metadatum > 0 and metadatum <= len(node.children):
            node_value += compute_node_value(node.children[metadatum - 1])
    return node_value


ParsedChallengeInput = Node


class Day08(Challenge):
    def read_file(self,filename) -> ParsedChallengeInput:
        parsed_input = list(map(int, super().read_file(filename, delimiter=" ")))
        tree_root_node, parsed_input = parse_node(parsed_input)
        assert len(parsed_input) == 0, "Expected processed parsed_input to be empty"
        return tree_root_node

    @staticmethod
    def solve_part1(
        tree_root_node: Node,
        verbose: bool = False,
    ):
        if verbose:
            print(tree_root_node)
        metadata_sum = 0
        queue = [tree_root_node]
        visited = set()
        while len(queue) > 0:
            node = queue.pop(0)
            if node not in visited:
                visited.add(node)
                queue.extend(node.children)
                metadata_sum += sum(node.metadata)
        return metadata_sum

    @staticmethod
    def solve_part2(
        tree_root_node: Node,
        verbose: bool = False,
    ):
        if verbose:
            print(tree_root_node)
        return compute_node_value(tree_root_node)


if __name__ == "__main__":
    Day08().solve_all()
