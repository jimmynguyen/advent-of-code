# https://adventofcode.com/2015/day/24
from solutions.challenge import Challenge
from itertools import combinations
from math import inf, prod


class Day24(Challenge):
    @staticmethod
    def solve(packages,num_grps=3,verbose=False):
        packages = [int(x) for x in packages]
        num_packages = len(packages)
        is_solved = False
        quantum_entanglement = inf
        for grp1_len in range(1,num_packages//num_grps+1):
            for grp1 in combinations(packages,grp1_len):
                remaining_packages = [x for x in packages if x not in grp1]
                if sum(grp1)*(num_grps-1) != sum(remaining_packages):
                    continue
                for grp2_len in range(grp1_len,num_packages//num_grps+1):
                    if is_solved:
                        continue
                    for grp2 in combinations(remaining_packages,grp2_len):
                        if is_solved:
                            continue
                        if sum(grp1) == sum(grp2):
                            if num_grps == 3:
                                grp3 = [x for x in remaining_packages if x not in grp2]
                                if sum(grp1) == sum(grp3):
                                    if verbose: print(grp1,grp2,grp3)
                                    is_solved = True
                                    quantum_entanglement = min(quantum_entanglement,prod(grp1))
                                    if verbose: print(f"SOLVED: {quantum_entanglement}")
                            elif num_grps == 4:
                                remaining_packages = [x for x in packages if x not in grp1 and x not in grp2]
                                for grp3_len in range(grp1_len,num_packages//num_grps+1):
                                    if is_solved:
                                        continue
                                    for grp3 in combinations(remaining_packages,grp3_len):
                                        if is_solved:
                                            continue
                                        if sum(grp1) == sum(grp3):
                                            grp4 = [x for x in remaining_packages if x not in grp3]
                                            if sum(grp1) == sum(grp4):
                                                if verbose: print(grp1,grp2,grp3,grp4)
                                                is_solved = True
                                                quantum_entanglement = min(quantum_entanglement,prod(grp1))
                                                if verbose: print(f"SOLVED: {quantum_entanglement}")
                            else:
                                raise ValueError(f"Invalid num_grps: {num_grps}")

            if is_solved:
                break
        return quantum_entanglement

    @staticmethod
    def solve_part1(input):
        return Day24.solve(input,num_grps=3)

    @staticmethod
    def solve_part2(input):
        return Day24.solve(input,num_grps=4)


if __name__ == "__main__":
    Day24().solve_all()
