# https://adventofcode.com/2017/day/7
from solutions.challenge import Challenge


class Day07(Challenge):
    def read_file(self,filename):
        return {x.split()[0]:(int(x.split()[1][1:-1]),x.split(" -> ")[1].split(", ") if " -> " in x else []) for x in super().read_file(filename)}

    @staticmethod
    def solve_part1(tier_map):
        lower_tiers = [k for k,(_,v) in tier_map.items() if len(v) >= 0]
        middle_tiers = [x for _,v in tier_map.values() for x in v]
        return [p for p in lower_tiers if p not in middle_tiers][0]

    @staticmethod
    def solve_part2(tier_map,tiers=None):
        if tiers is None:
            bottom_tier = Day07.solve_part1(tier_map)
            return Day07.solve_part2(tier_map,tiers=tier_map[bottom_tier][1])[0]
        elif len(tiers) == 0:
            return 0, False
        else:
            tier_total_weights = []
            for tier in tiers:
                tier_weight, upper_tiers = tier_map[tier]
                upper_tiers_weight, solved = Day07.solve_part2(tier_map,tiers=upper_tiers)
                if solved:
                    return upper_tiers_weight, solved
                tier_total_weights.append(tier_weight + upper_tiers_weight)
            if len(tiers) > 1:
                idx_unbalanced = [i for i,x in enumerate(tier_total_weights) if x not in (tier_total_weights[:i] + tier_total_weights[i+1:])]
                if len(idx_unbalanced) > 0:
                    idx_unbalanced = idx_unbalanced[0]
                    weight_unbalanced = tier_map[tiers[idx_unbalanced]][0]
                    total_weight_unbalanced = tier_total_weights[idx_unbalanced]
                    total_weight_balanced = tier_total_weights[(idx_unbalanced+1)%len(tiers)]
                    weight_balanced = weight_unbalanced + (total_weight_balanced - total_weight_unbalanced)
                    return weight_balanced, True
            return sum(tier_total_weights), False


if __name__ == "__main__":
    Day07().solve_all()
