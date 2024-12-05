# https://adventofcode.com/2016/day/21
from solutions.challenge import Challenge
from enum import Enum


class Day21(Challenge):
    @staticmethod
    def solve(instructions,msg,reverse=False,verbose=False):
        for ins in (instructions[::-1] if reverse else instructions):
            if verbose: print(msg,ins)
            op = Operation.get_op(ins)
            params = op.get_params(ins)
            msg = op.perform_op(params,msg,reverse)
        if verbose: print(msg)
        return msg

    @staticmethod
    def solve_part1(instructions,msg="abcdefgh"):
        return Day21.solve(instructions,msg)

    @staticmethod
    def solve_part2(instructions,msg="fbgdceah"):
        return Day21.solve(instructions,msg,reverse=True)


class Operation(Enum):
    SWP_POS = "swap position "," with position ",[],lambda x:tuple(sorted(map(int,x)))
    SWP_LET = "swap letter "," with letter ",[],tuple
    ROT_LEF = "rotate left ",None,[" step","s"],int
    ROT_RIT = "rotate right ",None,[" step","s"],lambda x:-int(x)
    ROT_POS = "rotate based on position of letter ",None,[],lambda x:x
    REV_POS = "reverse positions "," through ",[],lambda x:tuple(map(int,x))
    MOV_POS = "move position "," to position ",[],lambda x:tuple(map(int,x))

    def __new__(cls,*args,**kwds):
        obj = object.__new__(cls)
        obj._value_ = args[0]
        return obj

    def __init__(self,id,split_token,replace_tokens,format_params):
        self.id = id
        self.split_token = split_token
        self.replace_tokens = replace_tokens
        self.format_params = format_params

    @staticmethod
    def get_op(ins):
        for x in Operation:
            if ins.startswith(x.id):
                return x
        raise Exception(f"invalid instruction: {ins}")

    def get_params(self,ins):
        params = ins.replace(self.id,"")
        params = params if self.split_token is None else params.split(self.split_token)
        for x in self.replace_tokens:
            params = params.replace(x,"")
        return self.format_params(params)

    @staticmethod
    def rotate(msg,x):
        return msg[x%len(msg):] + msg[:x%len(msg)]

    def perform_op(self,params,msg,reverse=False):
        if self == Operation.SWP_POS:
            x,y = params
            msg = msg[:x] + msg[y] + msg[x+1:y] + msg[x] + msg[y+1:]
        elif self == Operation.SWP_LET:
            x,y = params[::-1] if reverse else params
            msg = "".join(y if c == x else x if c == y else c for c in msg)
        elif self == Operation.ROT_LEF or self == Operation.ROT_RIT:
            msg = Operation.rotate(msg[::-1],params)[::-1] if reverse else Operation.rotate(msg,params)
        elif self == Operation.ROT_POS:
            idx = msg.index(params)
            if reverse:
                rev_pos_map = {(1+2*i+(1 if i >= 4 else 0))%len(msg):i for i in range(len(msg))}
                n = idx - rev_pos_map[idx]
            else:
                n = -1-idx-(1 if idx >= 4 else 0)
            msg = Operation.rotate(msg,n)
        elif self == Operation.REV_POS:
            x,y = params
            msg = msg[:x] + (msg[y::-1] if x-1 < 0 else msg[y:x-1:-1]) + msg[y+1:]
        elif self == Operation.MOV_POS:
            x,y = params[::-1] if reverse else params
            msg = msg[:min(x,y)] + (msg[x+1:y+1] + msg[x] if x < y else msg[x] + msg[y:x]) + msg[max(x,y)+1:]
        return msg


if __name__ == "__main__":
    Day21().solve_all()
