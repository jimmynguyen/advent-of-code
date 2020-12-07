# https://adventofcode.com/2020/day/7
import util


def can_contain(container_map,container,container_to_find):
    for _,subcontainer in container_map[container]:
        if subcontainer == container_to_find or can_contain(container_map,subcontainer,container_to_find):
            return True
    return False


def count_possible_containers(container_map,container_to_find):
    containers = []
    for container in container_map.keys():
        if can_contain(container_map,container,container_to_find):
            containers.append(container)
    return len(containers)


def _count_container_contents(container_map,container_to_find):
    count = 1
    for n,subcontainer in container_map[container_to_find]:
        count += n * _count_container_contents(container_map,subcontainer)
    return count


def count_container_contents(container_map,container_to_find):
    return _count_container_contents(container_map,container_to_find) - 1


def solve(rules,count,container_to_find="shiny gold"):
    container_map = dict()
    for rule in rules:
        container,contents = tuple([x.strip()[:-1] for x in rule.split("contain")])
        container = container.replace(" bag","")
        subcontainers = [x.strip() for x in contents.split(",")]
        container_map[container] = []
        for subcontainer in subcontainers:
            if subcontainer != "no other bags":
                subcontainer = subcontainer.split(" ")
                n = int(subcontainer[0])
                subcontainer = " ".join(subcontainer[1:])
                subcontainer = subcontainer.replace(" bags","").replace(" bag","")
                container_map[container].append((n,subcontainer))
    # sanity check
    for subcontainers in container_map.values():
        for n,subcontainer in subcontainers:
            assert subcontainer in container_map.keys(),f"Invalid subcontainer {subcontainer} found"
    return count(container_map,container_to_find)


if __name__ == "__main__":
    day = 7
    inputs = [count_possible_containers,count_container_contents]
    test_inputs2 = [count_possible_containers,count_container_contents,count_container_contents]
    test_outputs = [4,126,32]
    util.solve(day,inputs,test_outputs,solve,test_inputs2=test_inputs2)