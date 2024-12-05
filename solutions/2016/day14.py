# https://adventofcode.com/2016/day/14
from solutions.challenge import Challenge
from hashlib import md5


class Day14(Challenge):
    @staticmethod
    def get_triplet(hash):
        triplet_idx = [i for i in range(len(hash)-2) if hash[i] == hash[i+1] and hash[i] == hash[i+2]]
        return None if len(triplet_idx) == 0 else hash[triplet_idx[0]]

    @staticmethod
    def get_quintet(hash):
        quintet_idx = [i for i in range(len(hash)-4) if hash[i] == hash[i+1] and hash[i] == hash[i+2] and hash[i] == hash[i+3] and hash[i] == hash[i+4]]
        return None if len(quintet_idx) == 0 else hash[quintet_idx[0]]

    @staticmethod
    def get_hash(x):
        return md5(x.encode()).hexdigest()

    @staticmethod
    def get_stretched_hash(x,num_stretches=2016):
        for _ in range(num_stretches+1):
            x = Day14.get_hash(x)
        return x

    @staticmethod
    def solve(salt,get_hash,num_keys=64,verbose=False):
        idx = 0
        triplets = {}
        keys = []
        while len(keys) < num_keys:
            hash = get_hash(salt+str(idx))
            quintet = Day14.get_quintet(hash)
            if quintet is not None and quintet in triplets:
                for _idx,_hash in triplets[quintet]:
                    if idx <= _idx + 1000:
                        if verbose: print(_idx,_hash,idx,hash)
                        keys.append(_idx)
                triplets.pop(quintet)
            triplet = Day14.get_triplet(hash)
            if triplet is not None:
                if triplet not in triplets:
                    triplets[triplet] = []
                triplets[triplet].append((idx,hash))
            idx += 1
        return keys[num_keys-1]

    @staticmethod
    def solve_part1(salt):
        return Day14.solve(salt,get_hash=Day14.get_hash)

    @staticmethod
    def solve_part2(salt):
        return Day14.solve(salt,get_hash=Day14.get_stretched_hash)


if __name__ == "__main__":
    Day14().solve_all("cuanljph")
