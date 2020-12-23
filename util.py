import os


def read_file(filename,delimiter="\n"):
    with open(filename) as file:
        lines = [x.strip() for x in file.readlines()]
        if delimiter != "\n":
            lines = "\n".join(lines).split(delimiter)
        return lines


def run_tests(filename_or_inputs,secondary_inputs,outputs,solve,read_file,verbose):
    if outputs is None or len(outputs) == 0:
        return
    if isinstance(filename_or_inputs,list):
        primary_inputs = filename_or_inputs
    elif os.path.isfile(filename_or_inputs):
        primary_inputs = [read_file(filename_or_inputs)]*len(secondary_inputs)
    else:
        test_filename = filename_or_inputs.replace(".","{}.")
        primary_inputs = [read_file(test_filename.format(i+1)) for i in range(len(secondary_inputs))]
    if secondary_inputs is None:
        tests = zip(primary_inputs,outputs)
    else:
        tests = zip(primary_inputs,secondary_inputs,outputs)
    for i,test in enumerate(tests):
        actual = solve(*test[:-1])
        expected = test[-1]
        assert actual == expected,f"unit test {i+1} failed: inputs={test[:-1]} expected={expected}, actual={actual}"
        if verbose:
            print(f"unit test {i+1} passed: inputs={test[:-1]} expected={expected}, actual={actual}")


def solve(day,inputs,test_outputs,solve,read_file=read_file,day_inputs=None,test_inputs1=None,test_inputs2=None,verbose=False,skip_tests=False):
    day_padded = str(day).zfill(2)
    filename = f"day{day_padded}.txt"
    test_filename = f"day{day_padded}_test.txt"
    year = os.path.basename(os.getcwd())
    print(f"\n{year} day {day_padded} challenge")
    if not skip_tests:
        run_tests(test_filename if test_inputs1 is None else test_inputs1,inputs if test_inputs2 is None else test_inputs2,test_outputs,solve,read_file,verbose=verbose)
    if inputs is None:
        if day_inputs is None:
            day_inputs = read_file(filename)
        print(f"answer:",solve(day_inputs))
    else:
        for i,x in enumerate(inputs):
            if day_inputs is None:
                day_inputs = read_file(filename)
            print(f"part {i+1} answer:",solve(day_inputs,x))