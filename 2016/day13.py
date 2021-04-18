# https://adventofcode.com/2016/day/13
from challenge import Challenge


class Day13(Challenge):
    def read_file(self,filename):
        return int(super().read_file(filename))

    @staticmethod
    def is_wall(src,n):
        x,y = tuple(src)
        return bin(x*x + 3*x + 2*x*y + y + y*y + n).count("1")%2 == 1

    @staticmethod
    def get_neighbors(src,n):
        return [x for x in set((max(src[0]+i,0),max(src[1]+j,0)) for i,j in [(0,1),(0,-1),(1,0),(-1,0)]) if not Day13.is_wall(x,n)]

    @staticmethod
    def explore(src,dst,n,path,prv):
        if src not in path or path[src][0] > path[prv][0]+1:
            path[src] = (0 if prv not in path else path[prv][0]+1,prv)
        if src == dst:
            return
        for neighbor in Day13.get_neighbors(src,n):
            if neighbor not in path or path[neighbor][0] > path[src][0]:
                Day13.explore(neighbor,dst,n,path,src)

    @staticmethod
    def print_map(map):
        for x in map:
            print("".join(x))
        print()

    @staticmethod
    def get_path(n,dst,verbose=False):
        prv = src = (1,1)
        path = dict()
        Day13.explore(src,dst,n,path,prv)
        if verbose:
            dim = max(dst)+1
            map = [["." for _ in range(dim)] for _ in range(dim)]
            for i in range(dim):
                for j in range(dim):
                    if Day13.is_wall((j,i),n):
                        map[i][j] = "#"
            _path = []
            node = dst
            while node != path[node][1]:
                _path.append(node)
                node = path[node][1]
            _path.append(node)
            Day13.print_map(map)
            for node in reversed(_path):
                map[node[1]][node[0]] = 'O'
                Day13.print_map(map)
        return path

    @staticmethod
    def solve_part1(n,dst=(31,39)):
        return Day13.get_path(n,dst)[dst][0]

    @staticmethod
    def solve_part2(n,dst=(31,39)):
        return len([k for k,v in Day13.get_path(n,dst).items() if v[0] <= 50])


if __name__ == "__main__":
    Day13().solve_all()
