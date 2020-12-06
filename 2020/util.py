import os


def read_file(filename,delimiter="\n"):
    with open(filename) as file:
        lines = [x.strip() for x in file.readlines()]
        if delimiter != "\n":
            lines = "\n".join(lines).split(delimiter)
        return lines


def run_tests(test_filename,inputs,test_outputs,solve,read_file):
    if os.path.isfile(test_filename):
        tests = zip([read_file(test_filename)]*len(inputs),inputs,test_outputs)
    else:
        test_filename = test_filename.replace(".","{}.")
        tests = zip([read_file(test_filename.format(i+1)) for i in range(len(inputs))],inputs,test_outputs)
    for i,test in enumerate(tests):
        actual = solve(*test[:-1])
        expected = test[-1]
        assert actual == expected,f"unit test {i+1} failed: expected={expected}, actual={actual}"


def solve(day,inputs,test_outputs,solve,read_file=read_file):
    day_padded = str(day).zfill(2)
    filename = f"day{day_padded}.txt"
    test_filename = f"day{day_padded}_test.txt"
    run_tests(test_filename,inputs,test_outputs,solve,read_file)
    for i,x in enumerate(inputs):
        print(f"part {i+1} answer:",solve(read_file(filename),x))