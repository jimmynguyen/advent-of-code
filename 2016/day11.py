# https://adventofcode.com/2016/day/11
from challenge import Challenge
from itertools import combinations
import re


class Day11(Challenge):
    ELEVATOR_CAPACITY = 2

    @staticmethod
    def init_floors(input,floors=None):
        new_floors = {i:list(filter(lambda x:x != "nothing relevant",map(lambda x:x.strip("."),re.split(", and | and |, ",x.split("contains ")[1])))) for i,x in enumerate(input)}
        if floors is not None:
            for x in floors.keys():
                new_floors[x].extend(floors[x])
        return new_floors

    @staticmethod
    def get_item_map(floors):
        items = []
        [items.extend(x) for x in floors.values()]
        item_map = dict()
        for item in items:
            item_map[item] = list(filter(lambda x:x != item and item.replace("a ","").replace("an ","").replace(" generator","").replace("-compatible microchip","") in x,items))[0]
        return item_map

    @staticmethod
    def is_item_type(item,item_type):
        return item.endswith(item_type)

    @staticmethod
    def get_items_by_type(floor,item_type):
        return list(filter(lambda x:Day11.is_item_type(x,item_type),floor))

    @staticmethod
    def get_items_by_types(floor,item_types):
        items = []
        for item_type in item_types:
            items += Day11.get_items_by_type(floor,item_type)
        return items

    @staticmethod
    def is_valid(items,item_map,items_to_add=None,items_to_remove=None):
        new_items = [x for x in items]
        if items_to_add is not None:
            for x in items_to_add:
                new_items.append(x)
        if items_to_remove is not None:
            for x in items_to_remove:
                new_items.remove(x)
        new_generators = Day11.get_items_by_type(new_items,ItemType.GENERATOR)
        new_microchips = Day11.get_items_by_type(new_items,ItemType.MICROCHIP)
        if len(new_generators) == 0 or len(new_microchips) == 0:
            return True
        return all(item_map[x] in new_generators for x in new_microchips)

    @staticmethod
    def sort_items(items,item_map):
        sorted_items = []
        for item in Day11.get_items_by_types(items,[ItemType.GENERATOR,ItemType.MICROCHIP]):
            if item not in sorted_items:
                if item_map[item] not in items and Day11.is_item_type(item,ItemType.GENERATOR):
                    sorted_items.insert(0,item)
                else:
                    sorted_items.append(item)
            if item_map[item] in items and item_map[item] not in sorted_items:
                sorted_items.append(item_map[item])
        return sorted_items

    @staticmethod
    def move_items(floors,item_map,src_idx,dst_idx):
        src_items = floors[src_idx]
        dst_items = floors[dst_idx]
        best_combo = None
        combo_sizes = range(Day11.ELEVATOR_CAPACITY,0,-1)
        if src_idx > dst_idx:
            combo_sizes = reversed(combo_sizes)
        for combo in [x for n in combo_sizes for x in combinations(Day11.sort_items(src_items,item_map),n)]:
            combo = list(combo)
            if Day11.is_valid(dst_items,item_map,items_to_add=combo) and Day11.is_valid(src_items,item_map,items_to_remove=combo):
                best_combo = combo
                break
        if best_combo is not None:
            dst_items.extend(best_combo)
            [src_items.remove(x) for x in best_combo]

    @staticmethod
    def has_perfect_pairs(src_items,item_map):
        filtered_src_items = [x for x in src_items]
        for x in Day11.get_items_by_type(filtered_src_items,ItemType.MICROCHIP):
            if item_map[x] in filtered_src_items:
                filtered_src_items.remove(x)
                filtered_src_items.remove(item_map[x])
        return len(src_items)//2 if len(src_items) > 0 and len(filtered_src_items) == 0 else False

    @staticmethod
    def print_floors(floors):
        for k,v in floors.items():
            print("  ",k,v)

    @staticmethod
    def solve(input,floors=None,verbose=False):
        floors = Day11.init_floors(input,floors)
        item_map = Day11.get_item_map(floors)
        num_floors = len(floors.keys())
        num_steps,prev_floor_idx,curr_floor_idx,next_floor_idx = 0,-1,0,1
        while True:
            if verbose: print(num_steps,prev_floor_idx,curr_floor_idx,next_floor_idx)
            if verbose: Day11.print_floors(floors)
            Day11.move_items(floors,item_map,curr_floor_idx,next_floor_idx)
            num_steps += abs(next_floor_idx - curr_floor_idx)
            if not any([len(v) > 0 for k,v in floors.items() if k < max(floors.keys())]):
                break
            prev_floor_idx = curr_floor_idx
            curr_floor_idx = next_floor_idx
            if Day11.has_perfect_pairs(floors[curr_floor_idx],item_map) and (next_floor_idx+1 < num_floors) and (len(floors[next_floor_idx+1]) == 1) and Day11.is_item_type(floors[next_floor_idx+1][0],ItemType.MICROCHIP):
                next_floor_idx -= 1
            elif next_floor_idx+1 >= num_floors or ((next_floor_idx+1 == num_floors-1) and Day11.has_perfect_pairs(floors[num_floors-1],item_map) and (Day11.has_perfect_pairs(floors[curr_floor_idx],item_map) == 1) and any([len(v) > 0 for k,v in floors.items() if k < next_floor_idx])):
                while True:
                    next_floor_idx -= 1
                    if len(floors[next_floor_idx]) > 0:
                        break
            else:
                next_floor_idx += 1
        if verbose: Day11.print_floors(floors)
        return num_steps

    @staticmethod
    def solve_part1(input):
        return Day11.solve(input)

    @staticmethod
    def solve_part2(input):
        return Day11.solve(input,floors={0:["an elerium generator","an elerium-compatible microchip","a dilithium generator","a dilithium-compatible microchip"]})


class ItemType:
    GENERATOR = "generator"
    MICROCHIP = "microchip"


if __name__ == "__main__":
    Day11().solve_all()
