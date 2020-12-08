# https://adventofcode.com/2015/day/9
from itertools import permutations
import util


def solve(edges,aggregate):
    adjacency_matrix = dict()
    for edge in edges:
        edge,weight = tuple(edge.split(" = "))
        src,dst = tuple(edge.split(" to "))
        if src not in adjacency_matrix:
            adjacency_matrix[src] = dict()
        if dst not in adjacency_matrix:
            adjacency_matrix[dst] = dict()
        adjacency_matrix[src][dst] = int(weight)
        adjacency_matrix[dst][src] = int(weight)
    nodes = adjacency_matrix.keys()
    num_nodes = len(nodes)
    dists = []
    for path in permutations(nodes):
        dist = 0
        for i in range(num_nodes-1):
            u,v = path[i:i+2]
            dist += adjacency_matrix[u][v]
        dists.append(dist)
    return aggregate(dists)


if __name__ == "__main__":
    day = 9
    inputs = [min,max]
    test_outputs = [605,982]
    util.solve(day,inputs,test_outputs,solve)