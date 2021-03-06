# https://adventofcode.com/2020/day/13
from challenge import Challenge
import math
import numpy as np


class Day13(Challenge):
    @staticmethod
    def solve_1(start_time,buses):
        return math.prod(sorted([(bus,bus - (start_time % bus)) for bus in buses if bus != "x"],key=lambda x: x[1])[0])

    @staticmethod
    def solve_2_bruteforce(start_time,buses):
        buses = [(idx,bus) for idx,bus in enumerate(buses) if bus != "x"]
        A,b = [],[]
        n = len(buses)
        for i,(idx,bus) in enumerate(buses):
            A.append(([0] * i + [bus] + ([0] * (n-i-1))))
            b.append(idx)
        A,b = np.array(A),np.array(b)
        i = 0
        while True:
            c = b + i
            x = np.linalg.solve(A,c)
            if all(map(float.is_integer,x)):
                break
            i += 1
        return i

    @staticmethod
    def extended_gcd(a,b):
        # https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm
        r1,r2 = a,b
        s1,s2 = 1,0
        t1,t2 = 0,1
        while r2 != 0:
            quotient,remainder = divmod(r1,r2)
            r1,r2 = r2,remainder
            s1,s2 = s2,s1 - quotient * s2
            t1,t2 = t2,t1 - quotient * t2
        return r1,s1,t1

    @staticmethod
    def combine(a_period, a_offset, b_period, b_offset):
        # https://github.com/sijmn/aoc2020/blob/master/python/day13.py
        gcd,s,_ = Day13.extended_gcd(a_period,b_period)
        diff = a_offset - b_offset
        diff_quot, dif_rem = divmod(diff, gcd)
        assert(dif_rem == 0)
        combined_period = a_period // gcd * b_period
        combined_offset = (a_offset - s * diff_quot * a_period) % combined_period
        return combined_period, combined_offset

    @staticmethod
    def solve_2_cheat(start_time,buses):
        # https://github.com/sijmn/aoc2020/blob/master/python/day13.py
        period = 1
        offset = 0
        for i,bus in enumerate(buses):
            if bus == "x":
                continue
            period,offset = Day13.combine(period,offset,bus,i)
        return -offset%period

    @staticmethod
    def solve(args,solver):
        start_time,buses = int(args[0]),[int(x) if x != "x" else x for x in args[1].split(",")]
        return solver(start_time,buses)

    @staticmethod
    def solve_part1(input):
        return Day13.solve(input,Day13.solve_1)

    @staticmethod
    def solve_part2(input):
        return Day13.solve(input,Day13.solve_2_cheat)


if __name__ == "__main__":
    Day13().solve_all()
