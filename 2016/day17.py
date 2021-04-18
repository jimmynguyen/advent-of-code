# https://adventofcode.com/2016/day/17
from challenge import Challenge
from hashlib import md5


class Day17(Challenge):
    @staticmethod
    def md5(x,hash_history):
        if x not in hash_history:
            hash_history[x] = md5(x.encode()).hexdigest()
        return hash_history[x]

    @staticmethod
    def is_open(x):
        return x in "bcdef"

    @staticmethod
    def solve(passcode,part2=False,N=4):
        hash_history = {}
        stack = [("",(0,0))]
        output_path = None
        while len(stack) > 0:
            path,coords = stack.pop()
            if coords == (N-1,N-1):
                if output_path is None or (not part2 and len(output_path) > len(path)) or (part2 and len(output_path) < len(path)):
                    output_path = path
                    if not part2:
                        stack = [x for x in stack if len(x) < len(output_path)]
                continue
            up,down,left,right = tuple(Day17.is_open(x) and any(Day17.is_open(z) for z in Day17.md5(passcode+path+y,hash_history)[:4]) for x,y in zip(Day17.md5(passcode+path,hash_history)[:4],"UDLR"))
            if part2 or output_path is None or len(path)+1 < len(output_path):
                if up and coords[0]-1 >= 0:
                    stack.append((path+"U",(coords[0]-1,coords[1])))
                if down and coords[0]+1 < N:
                    stack.append((path+"D",(coords[0]+1,coords[1])))
                if left and coords[1]-1 >= 0:
                    stack.append((path+"L",(coords[0],coords[1]-1)))
                if right and coords[1]+1 < N:
                    stack.append((path+"R",(coords[0],coords[1]+1)))
        return len(output_path) if part2 else output_path

    @staticmethod
    def solve_part1(passcode):
        return Day17.solve(passcode)

    @staticmethod
    def solve_part2(passcode):
        return Day17.solve(passcode,part2=True)


if __name__ == "__main__":
    Day17().solve_all("pgflpeqp")
