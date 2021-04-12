# https://adventofcode.com/2020/day/7
from challenge import Challenge


class Day07(Challenge):
    @staticmethod
    def can_contain(container_map,container,container_to_find):
        for _,subcontainer in container_map[container]:
            if subcontainer == container_to_find or Day07.can_contain(container_map,subcontainer,container_to_find):
                return True
        return False

    @staticmethod
    def count_possible_containers(container_map,container_to_find):
        containers = []
        for container in container_map.keys():
            if Day07.can_contain(container_map,container,container_to_find):
                containers.append(container)
        return len(containers)

    @staticmethod
    def _count_container_contents(container_map,container_to_find):
        count = 1
        for n,subcontainer in container_map[container_to_find]:
            count += n * Day07._count_container_contents(container_map,subcontainer)
        return count

    @staticmethod
    def count_container_contents(container_map,container_to_find):
        return Day07._count_container_contents(container_map,container_to_find) - 1

    @staticmethod
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

    @staticmethod
    def solve_part1(input):
        return Day07.solve(input,Day07.count_possible_containers)

    @staticmethod
    def solve_part2(input):
        return Day07.solve(input,Day07.count_container_contents)


if __name__ == "__main__":
    Day07().solve_all()
