# https://adventofcode.com/2016/day/7
from solutions.challenge import Challenge


class Day07(Challenge):
    @staticmethod
    def contains_ABBA(str):
        for i in range(len(str)-3):
            if str[i] == str[i+3] and str[i+1] == str[i+2] and str[i] != str[i+1]:
                return True
        return False

    @staticmethod
    def get_ABAs(str):
        return [str[i:i+3] for i in range(len(str)-2) if str[i] == str[i+2] and str[i] != str[i+1]]

    @staticmethod
    def solve_part1(ips):
        num_valid = 0
        for ip in ips:
            supports_TLS = [False,False]
            while "[" in ip:
                part1,ip = tuple(ip.split("[",maxsplit=1))
                part2,ip = tuple(ip.split("]",maxsplit=1))
                supports_TLS[0] = supports_TLS[0] or Day07.contains_ABBA(part1)
                supports_TLS[1] = supports_TLS[1] or Day07.contains_ABBA(part2)
            supports_TLS[0] = supports_TLS[0] or Day07.contains_ABBA(ip)
            if supports_TLS[0] and not supports_TLS[1]:
                num_valid += 1
        return num_valid

    @staticmethod
    def solve_part2(ips):
        num_valid = 0
        for ip in ips:
            ABAs = set()
            BABs = set()
            while "[" in ip:
                part1,ip = tuple(ip.split("[",maxsplit=1))
                part2,ip = tuple(ip.split("]",maxsplit=1))
                [ABAs.add(x) for x in Day07.get_ABAs(part1)]
                [BABs.add(x) for x in Day07.get_ABAs(part2)]
            [ABAs.add(x) for x in Day07.get_ABAs(ip)]
            if any(x[1]+x[0]+x[1] in BABs for x in ABAs):
                num_valid += 1
        return num_valid


if __name__ == "__main__":
    Day07().solve_all()
