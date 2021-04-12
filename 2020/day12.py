# https://adventofcode.com/2020/day/12
from challenge import Challenge
import math


class Day12(Challenge):
    @staticmethod
    def move(position,angle,value):
        position[0] += value * math.cos(angle)
        position[1] += value * math.sin(angle)
        return position

    @staticmethod
    def rotate(waypoint,angle):
        return [waypoint[0] * math.cos(angle) - waypoint[1] * math.sin(angle), waypoint[0] * math.sin(angle) + waypoint[1] * math.cos(angle)]

    @staticmethod
    def solve_part1(instructions):
        position = [0,0]
        angle = 0
        for instruction in instructions:
            instruction,value = instruction[0],int(instruction[1:])
            if instruction == Instruction.NORTH:
                position = Day12.move(position,math.pi/2,value)
            elif instruction == Instruction.SOUTH:
                position = Day12.move(position,-math.pi/2,value)
            elif instruction == Instruction.EAST:
                position = Day12.move(position,0,value)
            elif instruction == Instruction.WEST:
                position = Day12.move(position,math.pi,value)
            elif instruction == Instruction.FORWARD:
                position = Day12.move(position,angle,value)
            elif instruction == Instruction.RIGHT:
                angle -= value * math.pi / 180
            elif instruction == Instruction.LEFT:
                angle += value * math.pi / 180
        return round(sum(abs(x) for x in position))

    @staticmethod
    def solve_part2(instructions):
        position = [0,0]
        waypoint = [10,1]
        for instruction in instructions:
            instruction,value = instruction[0],int(instruction[1:])
            if instruction == Instruction.NORTH:
                waypoint = Day12.move(waypoint,math.pi/2,value)
            elif instruction == Instruction.SOUTH:
                waypoint = Day12.move(waypoint,-math.pi/2,value)
            elif instruction == Instruction.EAST:
                waypoint = Day12.move(waypoint,0,value)
            elif instruction == Instruction.WEST:
                waypoint = Day12.move(waypoint,math.pi,value)
            elif instruction == Instruction.FORWARD:
                for _ in range(value):
                    position[0] += waypoint[0]
                    position[1] += waypoint[1]
            elif instruction == Instruction.RIGHT:
                waypoint = Day12.rotate(waypoint,-value * math.pi / 180)
            elif instruction == Instruction.LEFT:
                waypoint = Day12.rotate(waypoint,value * math.pi / 180)
        return round(sum(abs(x) for x in position))


class Instruction:
    NORTH = "N"
    SOUTH = "S"
    EAST = "E"
    WEST = "W"
    FORWARD = "F"
    RIGHT = "R"
    LEFT = "L"


if __name__ == "__main__":
    Day12().solve_all()
