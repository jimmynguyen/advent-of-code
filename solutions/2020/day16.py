# https://adventofcode.com/2020/day/16
from solutions.challenge import Challenge
import math


class Day16(Challenge):
    def read_file(self,filename,delimiter="\n\n"):
        ticket_fields,your_ticket,nearby_tickets = tuple(super().read_file(filename,delimiter))
        validation_map = Day16.parse_ticket_fields(ticket_fields)
        your_ticket = Day16.parse_tickets(your_ticket.split("\n")[1:])[0]
        nearby_tickets = Day16.parse_tickets(nearby_tickets.split("\n")[1:])
        return validation_map,your_ticket,nearby_tickets

    @staticmethod
    def parse_ticket_fields(fields):
        validation_map = dict()
        for field in fields.split("\n"):
            field,valid_ranges = tuple(field.split(": "))
            valid_ranges = [tuple(map(int,x.split("-"))) for x in valid_ranges.split(" or ")]
            validation_map[field] = valid_ranges
        return validation_map

    @staticmethod
    def parse_tickets(tickets):
        return [tuple(map(int,x.split(","))) for x in tickets]

    @staticmethod
    def validate_tickets(nearby_tickets,validation_map):
        valid_nearby_tickets = []
        invalid_values = []
        for nearby_ticket in nearby_tickets:
            any_invalid = False
            for value in nearby_ticket:
                is_valid = False
                for field,valid_ranges in validation_map.items():
                    for valid_range in valid_ranges:
                        if value >= valid_range[0] and value <= valid_range[1]:
                            is_valid = True
                            break
                    if is_valid:
                        break
                if not is_valid:
                    invalid_values.append(value)
                    any_invalid = True
            if not any_invalid:
                valid_nearby_tickets.append(nearby_ticket)
        return valid_nearby_tickets,sum(invalid_values)

    @staticmethod
    def update_possible_fields(possible_fields,i):
        update_list = [i]
        while len(update_list) > 0:
            i = update_list.pop()
            for j in range(len(possible_fields)):
                if i != j and possible_fields[i][0] in possible_fields[j]:
                    possible_fields[j].remove(possible_fields[i][0])
                    if len(possible_fields[j]) == 1:
                        update_list.append(j)
        return possible_fields

    @staticmethod
    def solve_part1(notes):
        validation_map,_,nearby_tickets = notes
        return Day16.validate_tickets(nearby_tickets,validation_map)[1]

    @staticmethod
    def solve_part2(notes):
        validation_map,your_ticket,nearby_tickets = notes
        nearby_tickets,_ = Day16.validate_tickets(nearby_tickets,validation_map)
        possible_fields = [[x for x in validation_map.keys()] for _ in range(len(your_ticket))]
        for nearby_ticket in nearby_tickets:
            for i,value in enumerate(nearby_ticket):
                for field,valid_ranges in validation_map.items():
                    is_valid = False
                    for valid_range in valid_ranges:
                        if value >= valid_range[0] and value <= valid_range[1]:
                            is_valid = True
                            break
                    if not is_valid:
                        possible_fields[i].remove(field)
                        if len(possible_fields[i]) == 1:
                            Day16.update_possible_fields(possible_fields,i)
        return math.prod([your_ticket[i] for i,x in enumerate(possible_fields) if x[0].startswith("departure")])


if __name__ == "__main__":
    Day16().solve_all()
