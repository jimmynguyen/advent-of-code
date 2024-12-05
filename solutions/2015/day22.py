# https://adventofcode.com/2015/day/22
from solutions.challenge import Challenge
from itertools import product
from math import inf


class Day22(Challenge):
    def read_file(self,filename):
        hit_points,damage = tuple(int(x.split(": ")[1]) for x in super().read_file(filename))
        return Stats(hit_points=hit_points,damage=damage)

    @staticmethod
    def apply_effects(stats):
        for x in stats.effects:
            stats.hit_points -= x.damage
            stats.mana += x.mana_regen
            x.duration -= 1
        stats.effects = [x for x in stats.effects if x.duration > 0]
        return stats

    @staticmethod
    def is_win(player,boss,spells,is_hard_difficulty):
        player = Stats(player)
        boss = Stats(boss)
        spells = [Spell(x) for x in spells]
        for i in range(2*len(spells)):
            if player.hit_points <= 0 or boss.hit_points <= 0:
                break
            elif i%2 == 0:
                # player turn
                spell = spells[i//2]

                # On the next run through the game, you increase the difficulty to hard.
                # At the start of each player turn (before any other effects apply), you lose 1 hit point. If this brings you to or below 0 hit points, you lose.
                if is_hard_difficulty:
                    player.hit_points -= 1
                if player.hit_points <= 0 or boss.hit_points <= 0:
                    break

                # apply mana cost
                if player.mana > spell.mana_cost:
                    player.mana -= spell.mana_cost
                else:
                    return False

                # apply effects
                boss = Day22.apply_effects(boss)
                player = Day22.apply_effects(player)
                if player.hit_points <= 0 or boss.hit_points <= 0:
                    break

                # perform player spell
                if spell.name == "Magic Missile":
                    boss.hit_points -= spell.damage
                elif spell.name == "Drain":
                    boss.hit_points -= spell.damage
                    player.hit_points += spell.healing
                elif spell.name in ["Shield","Recharge"]:
                    # You cannot cast a spell that would start an effect which is already active.
                    if spell.name not in [x.name for x in player.effects]:
                        player.effects.append(spell)
                    else:
                        return False
                elif spell.name == "Poison":
                    # You cannot cast a spell that would start an effect which is already active.
                    if spell.name not in [x.name for x in boss.effects]:
                        boss.effects.append(spell)
                    else:
                        return False
                else:
                    raise ValueError(f"Invalid spell: {spell}")
            else:
                # boss turn

                # apply effects
                player_armor = sum(x.armor for x in player.effects)
                boss = Day22.apply_effects(boss)
                player = Day22.apply_effects(player)
                if player.hit_points <= 0 or boss.hit_points <= 0:
                    break

                # perform boss attack
                player.hit_points -= max(boss.damage - player_armor,1)
        return player.hit_points > 0 and boss.hit_points <= 0

    @staticmethod
    def solve(boss_stats,is_hard_difficulty,hit_points=50,damage=0,mana=500,verbose=False):
        player_stats = Stats(hit_points=hit_points,damage=damage,mana=mana)
        if verbose: print(player_stats,boss_stats)
        spells = [
            Spell(name="Magic Missile",mana_cost=53,damage=4),
            Spell(name="Drain",mana_cost=73,damage=2,healing=2),
            Spell(name="Shield",mana_cost=113,armor=7,duration=6),
            Spell(name="Poison",mana_cost=173,damage=3,duration=6),
            Spell(name="Recharge",mana_cost=229,mana_regen=101,duration=5)
        ]
        combo_length = 1
        is_won = False
        mana_spent = inf
        while True:
            for spell_combo in product(spells,repeat=combo_length):
                if verbose: print(spell_combo)
                if Day22.is_win(player_stats,boss_stats,spell_combo,is_hard_difficulty):
                    is_won = True
                    if verbose: print(mana_spent,sum(x.mana_cost for x in spell_combo))
                    mana_spent = min(mana_spent,sum(x.mana_cost for x in spell_combo))
                    if verbose: print(f"WON: {mana_spent}")
            if is_won:
                break
            else:
                combo_length += 1
        return mana_spent

    @staticmethod
    def solve_part1(input,hit_points=50,damage=0,mana=500):
        return Day22.solve(input,False,hit_points=hit_points,damage=damage,mana=mana)

    @staticmethod
    def solve_part2(input):
        return Day22.solve(input,True)


class Stats:
    def __init__(self,that=None,hit_points=0,damage=0,mana=0):
        if that is None:
            self.hit_points = hit_points
            self.damage = damage
            self.mana = mana
            self.effects = []
        else:
            self.hit_points = that.hit_points
            self.damage = that.damage
            self.mana = that.mana
            self.effects = [Spell(x) for x in that.effects]

    def __str__(self):
        return f"Stats(hit_points={self.hit_points},damage={self.damage},mana={self.mana})"

    def __repr__(self):
        return f"Stats(hit_points={self.hit_points},damage={self.damage},mana={self.mana})"


class Spell:
    def __init__(self,that=None,name=None,mana_cost=0,damage=0,armor=0,healing=0,mana_regen=0,duration=0):
        if that is None:
            self.name = name
            self.mana_cost = mana_cost
            self.damage = damage
            self.armor = armor
            self.healing = healing
            self.mana_regen = mana_regen
            self.duration = duration
        else:
            self.name = that.name
            self.mana_cost = that.mana_cost
            self.damage = that.damage
            self.armor = that.armor
            self.healing = that.healing
            self.mana_regen = that.mana_regen
            self.duration = that.duration

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


if __name__ == "__main__":
    Day22().solve_all()
