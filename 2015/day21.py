# https://adventofcode.com/2015/day/21
from challenge import Challenge
from itertools import combinations
from math import inf


class Day21(Challenge):
    def read_file(self,filename):
        hit_points,damage,armor = tuple(int(x.split(": ")[1]) for x in super().read_file(filename))
        return Stats(hit_points,damage,armor)

    @staticmethod
    def is_win(hit_points,items,boss_stats):
        player_stats = Stats(hit_points,sum(x.damage for x in items),sum(x.armor for x in items))
        return (player_stats.hit_points / max(boss_stats.damage - player_stats.armor,1)) > (boss_stats.hit_points / max(player_stats.damage - boss_stats.armor,1))

    @staticmethod
    def update_gold_spent(gold_spent,hit_points,items,boss_stats,is_betrayed):
        if not is_betrayed and Day21.is_win(hit_points,items,boss_stats):
            gold_spent = min(sum(x.cost for x in items),gold_spent)
        if is_betrayed and not Day21.is_win(hit_points,items,boss_stats):
            gold_spent = max(sum(x.cost for x in items),gold_spent)
        return gold_spent

    @staticmethod
    def solve(boss_stats,is_betrayed):
        hit_points = 100
        weapons = [Item("Dagger",8,4,0),Item("Shortsword",10,5,0),Item("Warhammer",25,6,0),Item("Longsword",40,7,0),Item("Greataxe",74,8,0)]
        armors = [Item("None",0,0,0),Item("Leather",13,0,1),Item("Chainmail",31,0,2),Item("Splintmail",53,0,3),Item("Bandedmail",75,0,4),Item("Platemail",102,0,5)]
        rings = [Item("Damage +1",25,1,0),Item("Damage +2",50,2,0),Item("Damage +3",100,3,0),Item("Defense +1",20,0,1),Item("Defense +2",40,0,2),Item("Defense +3",80,0,3)]
        gold_spent = -inf if is_betrayed else inf
        for weapon in weapons:
            items = [weapon]
            gold_spent = Day21.update_gold_spent(gold_spent,hit_points,items,boss_stats,is_betrayed)
            for armor in armors:
                items.append(armor)
                gold_spent = Day21.update_gold_spent(gold_spent,hit_points,items,boss_stats,is_betrayed)
                for ring in rings:
                    items.append(ring)
                    gold_spent = Day21.update_gold_spent(gold_spent,hit_points,items,boss_stats,is_betrayed)
                    items.remove(ring)
                for (ring1,ring2) in combinations(rings,2):
                    items.append(ring1)
                    items.append(ring2)
                    gold_spent = Day21.update_gold_spent(gold_spent,hit_points,items,boss_stats,is_betrayed)
                    items.remove(ring1)
                    items.remove(ring2)
                items.remove(armor)
        return gold_spent

    @staticmethod
    def solve_part1(input):
        return Day21.solve(input,False)

    @staticmethod
    def solve_part2(input):
        return Day21.solve(input,True)


class Stats:
    def __init__(self,hit_points,damage,armor):
        self.hit_points = hit_points
        self.damage = damage
        self.armor = armor


class Item:
    def __init__(self,name,cost,damage,armor):
        self.name = name
        self.cost = cost
        self.damage = damage
        self.armor = armor

    def __str__(self):
        return f"Item(name={self.name},cost={self.cost},damage={self.damage},armor={self.armor})"


if __name__ == "__main__":
    Day21().solve_all()
