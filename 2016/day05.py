# https://adventofcode.com/2016/day/5
from challenge import Challenge
from hashlib import md5


class Day05(Challenge):
    @staticmethod
    def solve(door_id,part2=False):
        password = [None,None,None,None,None,None,None,None]
        idx = 0
        while any(x is None for x in password):
            hash = md5((door_id+str(idx)).encode()).hexdigest()
            if hash.startswith("0"*5):
                if part2 and hash[5].isnumeric() and int(hash[5]) < len(password) and password[int(hash[5])] is None:
                        password[int(hash[5])] = hash[6]
                elif not part2:
                    password[password.index(None)] = hash[5]
            idx += 1
        return "".join(password)

    @staticmethod
    def solve_part1(input):
        return Day05.solve(input)

    @staticmethod
    def solve_part2(input):
        return Day05.solve(input,part2=True)


if __name__ == "__main__":
    Day05().solve_all()
