# https://adventofcode.com/2016/day/22
from solutions.challenge import Challenge
from itertools import permutations


class Day22(Challenge):
    def read_file(self,filename):
        return {tuple(map(int,x.replace("/dev/grid/node-x","").split("-y"))):(s,u,a) for x,s,u,a,_ in [tuple(int(y[:-1]) if y.endswith("T") else y for y in x.split()) for x in super().read_file(filename)[2:]]}

    @staticmethod
    def print_map(src,tgt,mpt,ncols,nrows,invalid):
        visual = [["." for _ in range(ncols)] for _ in range(nrows)]
        visual[src[1]][src[0]] = "*"
        visual[tgt[1]][tgt[0]] = "G"
        visual[mpt[1]][mpt[0]] = "_"
        for x in invalid:
            visual[x[1]][x[0]] = "#"
        [print(x) for x in visual]
        print()

    @staticmethod
    def find_shortest_path(nodes,src,tgt,ncols,nrows,invalid):
        stack = [src+(0,None)]
        visited = {}
        while len(stack) > 0:
            node = stack.pop()
            visited[node[:2]] = node[2:] if node[:2] not in visited or visited[node[:2]][0] > node[2] else visited[node[:2]]
            if node[:2] == tgt:
                continue
            stack += [x for x in [(node[0]+i,node[1]+j,node[2]+1,node[:2]) for i,j in [(0,1),(0,-1),(1,0),(-1,0)] if node[0]+i >= 0 and node[1]+j >= 0 and node[0]+i < ncols and node[1]+j < nrows] if (x[:2] not in visited or visited[x[:2]][0] > x[2]) and x[:2] not in invalid and nodes[src][1] <= nodes[x[:2]][0]]
        path = []
        while tgt is not None:
            path.insert(0,tgt)
            tgt = visited[tgt][1]
        return path

    @staticmethod
    def solve_part1(nodes):
        return sum([1 if used > 0 and used <= avail else 0 for (_,used,_),(_,_,avail) in permutations(nodes.values(),2)])

    @staticmethod
    def solve_part2(nodes,verbose=False):
        ncols = max([x for x,_ in nodes.keys()])+1
        nrows = max([x for _,x in nodes.keys()])+1
        src = (0,0)
        tgt = (ncols-1,0)
        mpt = [x for x,(_,y,_) in nodes.items() if y == 0][0]
        invalid = [k for k,v in nodes.items() if v[1] > nodes[mpt][0]]
        path_tgt_src = Day22.find_shortest_path(nodes,tgt,src,ncols,nrows,[])
        nsteps = 0
        for nxt in path_tgt_src[1:]:
            if verbose: Day22.print_map(src,tgt,mpt,ncols,nrows,invalid)
            # mpt -> nxt
            path_mpt_nxt = Day22.find_shortest_path(nodes,mpt,nxt,ncols,nrows,invalid+[tgt])
            nsteps += len(path_mpt_nxt)-1
            # tgt -> mpt
            mpt = tgt
            tgt = nxt
            nsteps += 1
        if verbose: Day22.print_map(src,tgt,mpt,ncols,nrows,invalid)
        return nsteps


if __name__ == "__main__":
    Day22().solve_all()
