# https://adventofcode.com/2020/day/16
import math
import util


def parse_ticket_fields(fields):
    validation_map = dict()
    for field in fields.split("\n"):
        field,valid_ranges = tuple(field.split(": "))
        valid_ranges = [tuple(map(int,x.split("-"))) for x in valid_ranges.split(" or ")]
        validation_map[field] = valid_ranges
    return validation_map


def parse_tickets(tickets):
    return [tuple(map(int,x.split(","))) for x in tickets]


def read_file(filename):
    ticket_fields,your_ticket,nearby_tickets = tuple(util.read_file(filename,"\n\n"))
    validation_map = parse_ticket_fields(ticket_fields)
    your_ticket = parse_tickets(your_ticket.split("\n")[1:])[0]
    nearby_tickets = parse_tickets(nearby_tickets.split("\n")[1:])
    return validation_map,your_ticket,nearby_tickets


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


def solve_1(notes):
    validation_map,_,nearby_tickets = notes
    return validate_tickets(nearby_tickets,validation_map)[1]


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


def solve_2(notes):
    validation_map,your_ticket,nearby_tickets = notes
    nearby_tickets,_ = validate_tickets(nearby_tickets,validation_map)
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
                        update_possible_fields(possible_fields,i)
    return math.prod([your_ticket[i] for i,x in enumerate(possible_fields) if x[0].startswith("departure")])


def solve(notes,solver):
    return solver(notes)


if __name__ == "__main__":
    day = 16
    inputs = [solve_1,solve_2]
    test_outputs = [71,1716]
    util.solve(day,inputs,test_outputs,solve,read_file=read_file)