def read_file(filename):
    with open(filename) as file:
        return [x.strip() for x in file.readlines()]


def unit_tests(test_input,inputs,test_outputs,solve):
    for i,test in enumerate([(test_input,x,y) for x,y in zip(inputs,test_outputs)]):
        actual = solve(*test[:-1])
        expected = test[-1]
        assert actual == expected,f"unit test {i+1} failed: expected={expected}, actual={actual}"


def solve(filename,inputs,test_input,test_outputs,solve,read_file=read_file):
    unit_tests(test_input,inputs,test_outputs,solve)
    for i,x in enumerate(inputs):
        print(f"part {i+1} answer:",solve(read_file(filename),x))