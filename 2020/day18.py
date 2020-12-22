# https://adventofcode.com/2020/day/18
import re
import util


def evaluate_1(expression):
    a,expression = tuple(expression.split(" ",1))
    a = int(a)
    while len(expression) > 0:
        op,expression = tuple(expression.split(" ",1))
        b = expression.split(" ",1)
        if len(b) > 1:
            expression = b[1]
        else:
            expression = ""
        b = int(b[0])
        if op == "+":
            a += b
        elif op == "*":
            a *= b
    return a


def evaluate_2(expression):
    for op in "+*":
        pattern = r"[0-9]+ [" + op + "] [0-9]+"
        match = re.search(pattern,expression)
        while match:
            expression = expression[:match.span()[0]] + str(evaluate_1(match.group())) + expression[match.span()[1]:]
            match = re.search(pattern,expression)
    return int(expression)


def solve(expressions,evaluate):
    results = []
    for expression in expressions:
        matches = re.findall(r"\([0-9*+ ]+\)",expression)
        while len(matches) > 0:
            for match in matches:
                expression = expression.replace(match,str(evaluate(match[1:-1])),1)
            matches = re.findall(r"\([0-9*+ ]+\)",expression)
        results.append(evaluate(expression))
    return sum(results)


if __name__ == "__main__":
    day = 18
    inputs = [evaluate_1,evaluate_2]
    test_outputs = [26335,693942]
    util.solve(day,inputs,test_outputs,solve)