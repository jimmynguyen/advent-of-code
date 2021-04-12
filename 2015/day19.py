# https://adventofcode.com/2015/day/19
from challenge import Challenge
import re


class Day19(Challenge):
    def read_file(self,filename,delimiter="\n\n"):
        return super().read_file(filename,delimiter)

    @staticmethod
    def count_distinct_molecules(rules,molecule):
        molecules = set()
        for src,dst in rules:
            i = 0
            while molecule.find(src,i) != -1:
                idx = molecule.find(src,i)
                i += 1
                molecules.add(molecule[:idx] + dst + molecule[idx+len(src):])
        return len(molecules)

    @staticmethod
    def count_steps_to_molecule(rules,target,molecules=["e"]):
        # inefficient brute force solution, takes too long to run
        new_molecules = set()
        for molecule in molecules:
            for src,dst in rules:
                i = 0
                while molecule.find(src,i) != -1:
                    idx = molecule.find(src,i)
                    i += 1
                    new_molecule = molecule[:idx] + dst + molecule[idx+len(src):]
                    if new_molecule == target:
                        return 1
                    new_molecules.add(new_molecule)
        return 1 + Day19.count_steps_to_molecule(rules,target,new_molecules)

    @staticmethod
    def count_steps_to_molecule_cheat(rules,molecule):
        # cheated: https://www.reddit.com/r/adventofcode/comments/3xflz8/day_19_solutions/cy4nsdd/
        molecule = molecule[::-1]
        rules = dict((y[::-1],x[::-1]) for x,y in rules)
        repl = lambda x: rules[x.group()]

        count = 0
        previous_molecule = None
        while molecule != 'e' and molecule != previous_molecule:
            previous_molecule = molecule
            molecule = re.sub('|'.join(rules.keys()), repl, molecule, 1)
            count += 1

        if molecule == previous_molecule:
            count -= 1

        return count

    @staticmethod
    def solve(*args):
        (rules,molecule),solver = args
        rules = [tuple(x.split(" => ")) for x in rules.split("\n")]
        return solver(rules,molecule)

    @staticmethod
    def solve_part1(input):
        return Day19.solve(input,Day19.count_distinct_molecules)

    @staticmethod
    def solve_part2(input):
        return Day19.solve(input,Day19.count_steps_to_molecule_cheat)


if __name__ == "__main__":
    Day19().solve_all()
