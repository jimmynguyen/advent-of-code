# https://adventofcode.com/2015/day/13
from challenge import Challenge
from itertools import permutations


class Day13(Challenge):
    @staticmethod
    def solve(edges,include_stranger):
        adjacency_matrix = dict()
        for edge in edges:
            src,edge = tuple(edge.split(" would "))
            edge,dst = tuple(edge.split(" happiness units by sitting next to "))
            dst = dst[:-1]
            sign,weight = edge.split(" ")
            if src not in adjacency_matrix:
                adjacency_matrix[src] = dict()
            adjacency_matrix[src][dst] = int(weight) * (1 if sign == "gain" else -1)
        nodes = adjacency_matrix.keys()
        if include_stranger:
            stranger = "stranger"
            i = 0
            while stranger in nodes:
                stranger = "stranger" + str(i)
                i += 1
            adjacency_matrix[stranger] = dict([(x,0) for x in nodes])
            for node in nodes:
                if node != stranger:
                    adjacency_matrix[node][stranger] = 0
        num_nodes = len(nodes)
        dists = []
        for arrangement in permutations(nodes):
            dist = 0
            for i in range(len(arrangement)):
                src = arrangement[i]
                dst = arrangement[(i+1)%num_nodes]
                dist += adjacency_matrix[src][dst] + adjacency_matrix[dst][src]
            dists.append(dist)
        return max(dists)

    @staticmethod
    def solve_part1(input):
        return Day13.solve(input,False)

    @staticmethod
    def solve_part2(input):
        return Day13.solve(input,True)


if __name__ == "__main__":
    Day13().solve_all()
