# https://adventofcode.com/2015/day/6
import util


class Action:
    TURN_ON = "turn on"
    TOGGLE = "toggle"
    TURN_OFF = "turn off"

    @staticmethod
    def values():
        return [Action.TURN_ON,Action.TOGGLE,Action.TURN_OFF]

    @staticmethod
    def get_action(instruction):
        for action in Action.values():
            if instruction.startswith(action):
                return action,instruction.replace(action,"")
        raise Exception("Invalid action for instruction: {}".format(instruction))


def solve(instructions,adjust_light,n=1000):
    grid = [[0 for _ in range(n)] for _ in range(n)]
    for instruction in instructions:
        action,instruction = Action.get_action(instruction)
        coords = [tuple(int(y.strip()) for y in x.split(",")) for x in instruction.split("through")]
        for i in range(coords[0][0],coords[1][0]+1):
            for j in range(coords[0][1],coords[1][1]+1):
                grid[i][j] = adjust_light(action,grid[i][j])
    return sum([sum(grid[i]) for i in range(n)])


if __name__ == "__main__":
    day = 6
    inputs = [
        lambda x,y: 1 if x == Action.TURN_ON else 0 if x == Action.TURN_OFF else 1 if not y else 0,
        lambda x,y: y+1 if x == Action.TURN_ON else max(0,y-1) if x == Action.TURN_OFF else y+2
    ]
    test_outputs = [998996,2000000]
    util.solve(day,inputs,test_outputs,solve)