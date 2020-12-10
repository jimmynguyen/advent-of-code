# https://adventofcode.com/2015/day/19
import re
import util


def count_distinct_molecules(rules,molecule):
    molecules = set()
    for src,dst in rules:
        i = 0
        while molecule.find(src,i) != -1:
            idx = molecule.find(src,i)
            i += 1
            molecules.add(molecule[:idx] + dst + molecule[idx+len(src):])
    return len(molecules)


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
    return 1 + count_steps_to_molecule(rules,target,new_molecules)


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


def solve(*args):
    (rules,molecule),solver = args
    rules = [tuple(x.split(" => ")) for x in rules.split("\n")]
    return solver(rules,molecule)


if __name__ == "__main__":
    day = 19
    inputs = [count_distinct_molecules,count_steps_to_molecule_cheat]
    test_inputs2 = [count_distinct_molecules] * 2 + [count_steps_to_molecule_cheat] * 2
    test_outputs = [4,7,3,6]
    util.solve(day,inputs,test_outputs,solve,read_file=lambda x: tuple(util.read_file(x,"\n\n")),test_inputs2=test_inputs2)