# https://adventofcode.com/2015/day/13
from itertools import permutations
import util


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


if __name__ == "__main__":
    day = 13
    inputs = [False,True]
    test_outputs = [330]
    util.solve(day,inputs,test_outputs,solve)