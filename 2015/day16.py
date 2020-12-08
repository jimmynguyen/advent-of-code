# https://adventofcode.com/2015/day/16
import util


def is_match(analysis,gift,amount,is_retroencabulator_outdated):
    if is_retroencabulator_outdated:
        if gift in ["cats","trees"]:
            return amount > analysis[gift]
        elif gift in ["pomeranians","goldfish"]:
            return amount < analysis[gift]
    return amount == analysis[gift]


def solve(aunts,is_retroencabulator_outdated):
    analysis = {"children": 3,"cats": 7,"samoyeds": 2,"pomeranians": 3,"akitas": 0,"vizslas": 0,"goldfish": 5,"trees": 3,"cars": 2,"perfumes": 1}
    for aunt in aunts:
        aunt,gifts = tuple(aunt.split(": ",1))
        aunt = int(aunt.split(" ")[1])
        gifts = dict((x,int(y)) for x,y in [tuple(x.split(": ")) for x in gifts.split(", ")])
        match = True
        for gift,amount in gifts.items():
            if not is_match(analysis,gift,amount,is_retroencabulator_outdated):
                match = False
                break
        if match:
            return aunt
    return None

if __name__ == "__main__":
    day = 16
    inputs = [False,True]
    test_outputs = []
    util.solve(day,inputs,test_outputs,solve)