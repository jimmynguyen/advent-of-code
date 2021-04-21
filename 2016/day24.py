# https://adventofcode.com/2016/day/24
from challenge import Challenge
from itertools import permutations
from math import inf


class Day24(Challenge):
    def read_file(self,filename):
        return [list(x) for x in super().read_file(filename)]

    @staticmethod
    def get_adj_mat(graph,nodes):
        nrows = len(graph)
        ncols = len(graph[0])
        dist = {}
        for src in nodes.values():
            stack = [src+(0,)]
            visited = {}
            while len(stack) > 0:
                node = stack.pop()
                visited[node[:2]] = node[2] if node[:2] not in visited or visited[node[:2]] > node[2] else visited[node[:2]]
                stack += [x for x in [(node[0]+i,node[1]+j,node[2]+1) for i,j in [(0,-1),(0,1),(1,0),(-1,0)]]  if (x[0] >= 0 and x[1] >= 0 and x[0] < nrows and x[1] < ncols) and (x[:2] not in visited or visited[x[:2]] > x[2]) and graph[x[0]][x[1]] != "#"]
            dist[src] = visited
        adj_mat = {x:{y:dist[x][y] for y in dist[x].keys() if x in nodes.values() and y in nodes.values()} for x in dist.keys()}
        return adj_mat

    @staticmethod
    def get_shortest_path(graph,ret_to_src=False):
        nodes = {y:(i,j) for i,x in enumerate(graph) for j,y in enumerate(x) if y.isnumeric()}
        adj_mat = Day24.get_adj_mat(graph,nodes)
        src = nodes["0"]
        min_len_path = inf
        for path in [list(x) for x in permutations(x for x in nodes.values() if x != src)]:
            if ret_to_src:
                path.append(src)
            crr = src
            len_path = 0
            while len(path) > 0:
                nxt = path.pop(0)
                len_path += adj_mat[crr][nxt]
                crr = nxt
            min_len_path = min(min_len_path,len_path)
        return min_len_path

    @staticmethod
    def solve_part1(graph):
        return Day24.get_shortest_path(graph)

    @staticmethod
    def solve_part2(graph):
        return Day24.get_shortest_path(graph,ret_to_src=True)


if __name__ == "__main__":
    Day24().solve_all()
