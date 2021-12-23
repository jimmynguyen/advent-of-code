# https://adventofcode.com/2015/day/15
from challenge import Challenge
from itertools import combinations_with_replacement, permutations
from math import prod


class Day15(Challenge):
    @staticmethod
    def solve(ingredients,ignore_calories):
        _ingredients = dict()
        for ingredient in ingredients:
            ingredient,properties = tuple(ingredient.split(": "))
            properties = dict([(y,int(z)) for y,z in [tuple(x.split(" ")) for x in properties.split(", ")]])
            _ingredients[ingredient] = properties
        possible_amounts = []
        for x in combinations_with_replacement(list(range(101)),len(ingredients)):
            if sum(x) == 100:
                possible_amounts.append(x)
        max_score = float("-inf")
        for amounts_combination in possible_amounts:
            for amounts in permutations(amounts_combination):
                scores = dict([("capacity",0),("durability",0),("flavor",0),("texture",0),("calories",0)])
                for amount,(ingredient,properties) in zip(amounts,_ingredients.items()):
                    for property in scores.keys():
                        scores[property] += amount * properties[property]
                if not ignore_calories and scores["calories"] != 500:
                    continue
                scores.pop("calories")
                max_score = max(max_score,prod(0 if x < 0 else x for x in scores.values()))
        return max_score

    @staticmethod
    def solve_part1(input):
        return Day15.solve(input,True)

    @staticmethod
    def solve_part2(input):
        return Day15.solve(input,False)


if __name__ == "__main__":
    Day15().solve_all()
