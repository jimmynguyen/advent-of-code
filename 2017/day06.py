# https://adventofcode.com/2017/day/6
from challenge import Challenge


class Day06(Challenge):
    def read_file(self,filename):
        return [int(x) for x in super().read_file(filename).split()]

    @staticmethod
    def solve(memory_state,get_output):
        history = []
        num_banks = len(memory_state)
        while memory_state not in history:
            history.append([x for x in memory_state])
            idx = memory_state.index(max(memory_state))
            num_blocks = memory_state[idx]
            memory_state[idx] = 0
            while True:
                idx = (idx+1)%num_banks
                memory_state[idx] += 1
                num_blocks -= 1
                if num_blocks == 0:
                    break
        return get_output(memory_state,history)

    @staticmethod
    def solve_part1(memory_state):
        return Day06.solve(memory_state,get_output=lambda x,y:len(y))

    @staticmethod
    def solve_part2(memory_state):
        return Day06.solve(memory_state,get_output=lambda x,y:len(y)-y.index(x))


if __name__ == "__main__":
    Day06().solve_all()
