# https://adventofcode.com/2016/day/20
from solutions.challenge import Challenge


class Day20(Challenge):
    def read_file(self,filename):
        return sorted(tuple(map(int,x.split("-"))) for x in super().read_file(filename))

    @staticmethod
    def solve_part1(blocked_ips):
        for i in range(len(blocked_ips)-1):
            if blocked_ips[i+1][0] - blocked_ips[i][1] > 1:
                return blocked_ips[i][1]+1

    @staticmethod
    def solve_part2(blocked_ips,num_ips=2**32):
        blocked_ips += [(num_ips,)]
        i = 0
        while i < len(blocked_ips)-1:
            if blocked_ips[i][0] <= blocked_ips[i+1][0] and blocked_ips[i+1][0] <= blocked_ips[i][1]:
                blocked_ips[i] = (blocked_ips[i][0],max(blocked_ips[i][1],blocked_ips[i+1][1]))
                blocked_ips.pop(i+1)
            else:
                i += 1
        return sum(blocked_ips[i+1][0]-blocked_ips[i][1]-1 for i in range(len(blocked_ips)-1))


if __name__ == "__main__":
    Day20().solve_all()
