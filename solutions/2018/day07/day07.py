# https://adventofcode.com/2018/day/7
from typing import Callable
from solutions.challenge import Challenge
import re
from collections import defaultdict


ParsedChallengeInput = tuple[set[str], dict[str,set[str]], dict[str,set[str]]]


class Day07(Challenge):
    def read_file(self,filename) -> ParsedChallengeInput:
        forward_dependency_map = defaultdict(set)
        backward_dependency_map = defaultdict(set)
        all_nodes = set()
        for line in super().read_file(filename):
            pattern = r"Step (.*?) must be finished before step (.*?) can begin\."
            match = re.search(pattern, line)
            parent = match.group(1)
            child = match.group(2)
            forward_dependency_map[parent].add(child)
            backward_dependency_map[child].add(parent)
            all_nodes.add(parent)
            all_nodes.add(child)
        return (all_nodes, forward_dependency_map, backward_dependency_map)

    @staticmethod
    def solve_part1(
        parsed_input: ParsedChallengeInput,
        verbose: bool = False,
    ):
        all_nodes, forward_map, backward_map = parsed_input

        if verbose:
            print("forward_map:", forward_map)
            print("backward_map:", backward_map)

        valid_start_nodes = sorted(all_nodes.difference(backward_map.keys()))

        if verbose:
            print("valid_start_nodes:", valid_start_nodes)

        priority_queue = valid_start_nodes
        visited = list()
        while len(priority_queue) > 0:
            curr_node = priority_queue.pop(0)
            if curr_node not in visited:
                visited.append(curr_node)
                for child in forward_map[curr_node]:
                    if child not in visited and backward_map[child].issubset(visited):
                        priority_queue.append(child)
            priority_queue = sorted(priority_queue)

        return "".join(visited)

    @staticmethod
    def solve_part2(
        parsed_input: ParsedChallengeInput,
        num_workers: int = 5,
        step_base_seconds: int = 60,
        verbose: bool = False,
    ):
        all_nodes, forward_map, backward_map = parsed_input

        if verbose:
            print("forward_map:", forward_map)
            print("backward_map:", backward_map)

        valid_start_nodes = sorted(all_nodes.difference(backward_map.keys()))

        if verbose:
            print("valid_start_nodes:", valid_start_nodes)

        compute_step_duration: Callable[[str],int] = lambda step: step_base_seconds + ord(step) - ord("A") + 1

        priority_queue = [
            (
                start_node,
                compute_step_duration(start_node)
            )
            for start_node
            in valid_start_nodes
        ]
        progress_queue = []
        visited = list()
        total_duration = 0
        while len(priority_queue) > 0 or len(progress_queue) > 0:
            while len(priority_queue) > 0 and len(progress_queue) < num_workers:
                progress_queue.append(priority_queue.pop(0))

            shortest_step, shortest_step_duration = min(progress_queue, key=lambda x: (x[1],x[0]))

            if shortest_step not in visited:
                visited.append(shortest_step)
                for child in forward_map[shortest_step]:
                    if child not in visited and backward_map[child].issubset(visited):
                        priority_queue.append((child, compute_step_duration(child)))
            priority_queue = sorted(priority_queue, key=lambda x: x[0])

            progress_queue = [(step, duration - shortest_step_duration) for step, duration in progress_queue if step != shortest_step]

            total_duration += shortest_step_duration

        return total_duration


if __name__ == "__main__":
    Day07().solve_all()
