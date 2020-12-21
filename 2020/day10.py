# https://adventofcode.com/2020/day/10
import util


def diff(numbers):
    return [numbers[i+1] - numbers[i] for i in range(len(numbers)-1)]


def solve_1(numbers):
    diffs = diff(numbers)
    num_diff1 = len([x for x in diffs if x == 1])
    num_diff3 = len([x for x in diffs if x == 3])
    return num_diff1 * num_diff3


def solve_2(nodes):
    adjacency_matrix = dict()
    for node in nodes:
        if node not in adjacency_matrix:
            adjacency_matrix[node] = []
        for i in range(1,4):
            if node + i in nodes:
                adjacency_matrix[node].append(node+i)
    count = 0
    stack = [[nodes[0]]]
    while len(stack) > 0:
        path = stack.pop()
        if path[-1] == nodes[-1]:
            count += 1
        else:
            for neighbor in adjacency_matrix[path[-1]]:
                new_path = path.copy()
                new_path.append(neighbor)
                stack.append(new_path)
    return count


def solve(numbers,solver):
    numbers = sorted(list(map(int,numbers)))
    numbers = [0] + numbers + [max(numbers) + 3]
    return solver(numbers)


if __name__ == "__main__":
    day = 10
    inputs = [solve_1,solve_2]
    test_inputs2 = [solve_1,solve_1,solve_2,solve_2]
    test_outputs = [35,220,8,19208]
    util.solve(day,inputs,test_outputs,solve,test_inputs2=test_inputs2)