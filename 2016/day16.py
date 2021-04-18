# https://adventofcode.com/2016/day/16
from challenge import Challenge


class Day16(Challenge):
    @staticmethod
    def solve_part1(data,length=272):
        while len(data) < length:
            data += "0" + "".join(["1" if x == "0" else "0" for x in data[::-1]])
        data = data[:length]
        while True:
            data = "".join(["1" if data[i] == data[i+1] else "0" for i in range(0,len(data),2)])
            if len(data)%2 == 1: break
        return data

    @staticmethod
    def solve_part2(data,length=35651584):
        return Day16.solve_part1(data,length)


if __name__ == "__main__":
    Day16().solve_all("11110010111001001")
