# https://adventofcode.com/2020/day/12
import math
import util


class Instruction:
    NORTH = "N"
    SOUTH = "S"
    EAST = "E"
    WEST = "W"
    FORWARD = "F"
    RIGHT = "R"
    LEFT = "L"


def move(position,angle,value):
    position[0] += value * math.cos(angle)
    position[1] += value * math.sin(angle)
    return position


def solve_1(instructions):
    position = [0,0]
    angle = 0
    for instruction in instructions:
        instruction,value = instruction[0],int(instruction[1:])
        if instruction == Instruction.NORTH:
            position = move(position,math.pi/2,value)
        elif instruction == Instruction.SOUTH:
            position = move(position,-math.pi/2,value)
        elif instruction == Instruction.EAST:
            position = move(position,0,value)
        elif instruction == Instruction.WEST:
            position = move(position,math.pi,value)
        elif instruction == Instruction.FORWARD:
            position = move(position,angle,value)
        elif instruction == Instruction.RIGHT:
            angle -= value * math.pi / 180
        elif instruction == Instruction.LEFT:
            angle += value * math.pi / 180
    return round(sum(abs(x) for x in position))


def rotate(waypoint,angle):
    return [waypoint[0] * math.cos(angle) - waypoint[1] * math.sin(angle), waypoint[0] * math.sin(angle) + waypoint[1] * math.cos(angle)]


def solve_2(instructions):
    position = [0,0]
    waypoint = [10,1]
    for instruction in instructions:
        instruction,value = instruction[0],int(instruction[1:])
        if instruction == Instruction.NORTH:
            waypoint = move(waypoint,math.pi/2,value)
        elif instruction == Instruction.SOUTH:
            waypoint = move(waypoint,-math.pi/2,value)
        elif instruction == Instruction.EAST:
            waypoint = move(waypoint,0,value)
        elif instruction == Instruction.WEST:
            waypoint = move(waypoint,math.pi,value)
        elif instruction == Instruction.FORWARD:
            for _ in range(value):
                position[0] += waypoint[0]
                position[1] += waypoint[1]
        elif instruction == Instruction.RIGHT:
            waypoint = rotate(waypoint,-value * math.pi / 180)
        elif instruction == Instruction.LEFT:
            waypoint = rotate(waypoint,value * math.pi / 180)
    return round(sum(abs(x) for x in position))


def solve(instructions,solve):
    return solve(instructions)


if __name__ == "__main__":
    day = 12
    inputs = [solve_1,solve_2]
    test_outputs = [25,286]
    util.solve(day,inputs,test_outputs,solve)