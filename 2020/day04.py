# https://adventofcode.com/2020/day/4
import re
import util


def read_file(filename):
    return [x.replace("\n"," ") for x in "\n".join(util.read_file(filename)).split("\n\n")]


def validate(passport):
    is_in_range = lambda x,a,b: x >= a and x <= b
    is_valid_year = lambda x,a,b: len(x) == 4 and is_in_range(int(x),a,b)
    return is_valid_year(passport["byr"],1920,2002)\
        and is_valid_year(passport["iyr"],2010,2020)\
        and is_valid_year(passport["eyr"],2020,2030)\
        and ((passport["hgt"].endswith("cm") and is_in_range(int(passport["hgt"][:-2]),150,193))\
            or (passport["hgt"].endswith("in") and is_in_range(int(passport["hgt"][:-2]),59,76)))\
        and re.search("^#[0-9a-z]{6}$",passport["hcl"]) is not None\
        and passport["ecl"] in ["amb","blu","brn","gry","grn","hzl","oth"]\
        and re.search("^[0-9]{9}$",passport["pid"]) is not None


def solve(passports,validate):
    required_fields = set(["byr","iyr","eyr","hgt","hcl","ecl","pid","cid"])
    num_valid = 0
    for passport in passports:
        passport = dict([tuple(x.split(":")) for x in passport.split(" ")])
        missing_fields = list(required_fields.difference(set(passport.keys())))
        if (len(missing_fields) == 0 or (len(missing_fields) == 1 and missing_fields[0] == "cid")) and validate(passport):
            num_valid += 1
    return num_valid


if __name__ == "__main__":
    day = 4
    inputs = [
        lambda x: True,
        validate
    ]
    test_outputs = [2,4]
    util.solve(day,inputs,test_outputs,solve,read_file)