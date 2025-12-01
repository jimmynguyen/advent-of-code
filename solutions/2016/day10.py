# https://adventofcode.com/2016/day/10
from solutions.challenge import Challenge
from math import prod
import re


class Day10(Challenge):
    @staticmethod
    def get_bot(bots,id):
        if id not in bots:
            bots[id] = Bot(id)
        return bots[id]

    @staticmethod
    def solve(instructions,chips=None):
        bots = dict()
        for ins in instructions:
            if re.match(r"^value \d+ goes to bot \d+$",ins):
                val,id = tuple(map(lambda x:int(x) if x.isnumeric() else x,map(lambda x:x.strip("value "),ins.split(" goes to "))))
                Day10.get_bot(bots,id).chips.add(val)
            else:
                id,lo_id,hi_id = tuple(re.split(" gives low to | and high to ",ins))
                bot = Day10.get_bot(bots,id)
                bot.lo_id = lo_id
                bot.hi_id = hi_id
        while True:
            ids = [k for k,v in bots.items() if len(v.chips) == 2]
            if len(ids) == 0:
                break
            bot = Day10.get_bot(bots,ids[0])
            if bot.chips == chips:
                return int(bot.id.strip("bot "))
            Day10.get_bot(bots,bot.lo_id).chips.add(min(bot.chips))
            Day10.get_bot(bots,bot.hi_id).chips.add(max(bot.chips))
            bots.pop(bot.id)
        return prod(list(v.chips)[0] for k,v in bots.items() if re.match("^output [012]$",k))

    @staticmethod
    def solve_part1(instructions,chips={17,61}):
        return Day10.solve(instructions,chips)

    @staticmethod
    def solve_part2(instructions):
        return Day10.solve(instructions)


class Bot:
    def __init__(self,id):
        self.id = id
        self.chips = set()
        self.lo_id = None
        self.hi_id = None

    def __str__(self):
        return f"<Bot id='{self.id}' chips={self.chips} lo_id='{self.lo_id}' hi_id='{self.hi_id}'>"

    def __repr__(self):
        return self.__str__()


if __name__ == "__main__":
    Day10().solve_all()
