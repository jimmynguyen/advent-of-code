# https://adventofcode.com/2015/day/11
import util


def is_valid(password):
    ascii = [ord(x) for x in password]
    found = False
    for i in range(len(ascii)-2):
        seq = ascii[i:i+3]
        if all(seq[j+1] - seq[j] == 1 for j in range(len(seq)-1)):
            found = True
            break
    if not found:
        return False
    for c in ["i","o","l"]:
        if c in password:
            return False
    i,count = 0,0
    while i < len(password)-1:
        if password[i] == password[i+1]:
            count += 1
            i += 2
        else:
            i += 1
    return count >= 2


def increment_password(password):
    next_password = ""
    inc = 1
    for c in password[::-1]:
        if inc == 0:
            next_password += c
        elif c != "z":
            next_password += chr(ord(c) + inc)
            inc = 0
        else:
            next_password += "a"
    return next_password[::-1]


def solve(password,num_passes):
    first_pass = True
    for _ in range(num_passes):
        if first_pass:
            first_pass = False
        else:
            password = increment_password(password)
        while not is_valid(password):
            idx = None
            for i,c in enumerate(password):
                if c in ["i","o","l"]:
                    idx = i
                    break
            if idx is not None:
                password = password[:idx] + chr(ord(password[idx])+1) + "a" * len(password[idx+1:])
            password = increment_password(password)
    return password


if __name__ == "__main__":
    day = 11
    day_inputs = "hxbxwxba"
    inputs = [1,2]
    test_inputs1 = ["abcdefgh","ghijklmn"]
    test_inputs2 = [1,1]
    test_outputs = ["abcdffaa","ghjaabcc"]
    util.solve(day,inputs,test_outputs,solve,day_inputs=day_inputs,test_inputs1=test_inputs1,test_inputs2=test_inputs2)