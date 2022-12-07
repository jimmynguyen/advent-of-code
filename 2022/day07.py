# https://adventofcode.com/2022/day/7
from typing import List
from challenge import Challenge
from collections import defaultdict

class Day07(Challenge):
    def read_file(self, filename: str) -> List[str]:
        return super().read_file(filename)

    @staticmethod
    def solve(input: List[str], part2) -> int:
        dir_contents = defaultdict(list)
        idx = 0
        pwd = []
        while idx < len(input):
            line = input[idx]
            if line.startswith("$ cd "):
                cwd = line[len("$ cd "):]
                if cwd == "..":
                    pwd.pop()
                else:
                    pwd.append(cwd)
            elif line.startswith("dir "):
                dir_contents["/".join(pwd)].append(line[len("dir "):])
            elif not line.startswith("$ ls"):
                size, filename = line.split()
                dir_contents["/".join(pwd)].append((filename, int(size)))
            idx += 1

        dir_sizes = dict()
        while len(dir_contents) > 0:
            for dir, contents in dict(dir_contents).items():
                if all(isinstance(x, tuple) for x in contents):
                    dir_sizes[dir] = sum(x[1] for x in contents)
                    dir_contents.pop(dir)
                else:
                    for content in contents:
                        if not isinstance(content, tuple) and f"{dir}/{content}" in dir_sizes:
                            dir_contents[dir].remove(content)
                            dir_contents[dir].append((content, dir_sizes[f"{dir}/{content}"]))

        if not part2:
            return sum(x for x in dir_sizes.values() if x < 100000)

        return min(x for x in dir_sizes.values() if x > 30000000 - (70000000 - dir_sizes["/"]))

    @staticmethod
    def solve_part1(input: List[str]) -> int:
        return Day07.solve(input, False)

    @staticmethod
    def solve_part2(input: List[str]) -> int:
        return Day07.solve(input, True)


if __name__ == "__main__":
    Day07().solve_all()
