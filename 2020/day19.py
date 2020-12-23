# https://adventofcode.com/2020/day/19
import util


def read_file(filename):
    rules,messages = tuple(x.split("\n") for x in util.read_file(filename,"\n\n"))
    rules_map = dict()
    for rule in rules:
        rule_number,rule = tuple(rule.split(": "))
        rules_map[rule_number] = [x[1:-1] if x[0] == "\"" else x.split(" ") for x in rule.split(" | ")]
    return rules_map,messages


def validate_rule_option(message,rule_number,rule_option,rules_map):
    is_valid = False
    _message = message
    if not isinstance(rule_option,list):
        return _message[0] == rule_option,_message[1:]
    else:
        if rule_number in rule_option:
            idx = rule_option.index(rule_number)
            is_valid,_message = validate_rule_option(message,rule_number,rule_option[:idx],rules_map)
            if is_valid and len(rule_option[idx+1:]) > 0:
                is_valid,_message = validate_rule_option(_message[::-1],rule_number,rule_option[idx+1:][::-1],rules_map)
                _message = _message[::-1]
            if is_valid:
                is_valid,_message = validate_rule_option(_message,rule_number,[rule_option[idx]],rules_map)
        else:
            for rule_option_number in rule_option:
                is_valid,_message = validate_rule(rules_map,rule_option_number,_message)
                if not is_valid:
                    break
    if not is_valid:
        _message = message
    return is_valid,_message


def validate_rule(rules_map,rule_number,message):
    is_valid = False
    for rule_option in rules_map[rule_number]:
        is_valid,_message = validate_rule_option(message,rule_number,rule_option,rules_map)
        if is_valid:
            break
    return is_valid,_message


def solve(inputs,override_rules):
    rules_map,messages = inputs
    if override_rules is not None:
        for rule_number,rule_options in override_rules.items():
            rules_map[rule_number] = rule_options
    num_valid = 0
    for i,message in enumerate(messages):
        any_valid,_message = validate_rule(rules_map,"0",message)
        if any_valid and len(_message) == 0:
            num_valid += 1
    return num_valid


if __name__ == "__main__":
    day = 19
    inputs = [None,{"8":[["42"],["42","8"]],"11":[["42","31"],["42","11","31"]]}]
    test_outputs = [2,12]
    util.solve(day,inputs,test_outputs,solve,read_file=read_file)