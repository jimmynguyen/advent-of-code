# https://adventofcode.com/2025/day/8
from solutions.challenge import Challenge
import numpy as np


ParsedChallengeInput = list[tuple[int,int,int]]


class Day08(Challenge):
    def read_file(self,filename) -> ParsedChallengeInput:
        return [np.array(list(map(int, line.split(",")))) for line in super().read_file(filename, delimiter="\n")]


    @staticmethod
    def solve_part1(
        parsed_input: ParsedChallengeInput,
        num_connections_threshold: int = 1000,
        part2: bool = False,
        debug: bool = False,
    ):
        junction_boxes = parsed_input
        num_junction_boxes = len(junction_boxes)
        D = np.ones(shape=(num_junction_boxes, num_junction_boxes)) * float("inf")
        for idx in range(num_junction_boxes):
            for jdx in range(idx + 1, num_junction_boxes):
                D[idx, jdx] = np.linalg.norm(junction_boxes[idx] - junction_boxes[jdx])
        circuits = []
        num_connections = 0
        while part2 or num_connections < num_connections_threshold:
            idx, jdx = np.unravel_index(D.argmin(), D.shape)
            if debug:
                print(f"min connection: {junction_boxes[idx]} - {junction_boxes[jdx]}")
            D[idx, jdx] = float("inf") # set to inf to exclude from next D.argmin()
            existing_circuit_indices = []
            for idx_circuit, circuit in enumerate(circuits):
                if idx in circuit or jdx in circuit:
                    existing_circuit_indices.append(idx_circuit)
            if not existing_circuit_indices:
                circuits.append({idx, jdx})
            else:
                circuit = set()
                for idx_circuit in existing_circuit_indices[::-1]:
                    circuit |= circuits.pop(idx_circuit)
                circuit.add(idx)
                circuit.add(jdx)
                circuits.append(circuit)
            if part2 and len(circuits) == 1 and len(circuits[0]) == num_junction_boxes:
                return junction_boxes[idx][0] * junction_boxes[jdx][0]
            num_connections += 1
        return np.prod(sorted(len(circuit) for circuit in circuits)[-3:])


    @staticmethod
    def solve_part2(
        parsed_input: ParsedChallengeInput,
        debug: bool = False,
    ):
        return Day08.solve_part1(parsed_input, part2=True, debug=debug)


if __name__ == "__main__":
    Day08().solve_all()
