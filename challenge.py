import os

from typing import Any, Optional


class Challenge:
    @staticmethod
    def solve_part1(input: Any):
        raise NotImplementedError()

    @staticmethod
    def solve_part2(input: Any):
        raise NotImplementedError()

    def read_file(self, filename: str, delimiter: str="\n", strip: bool=True):
        with open(filename) as file:
            lines = [x.strip() if strip else x[:-1] for x in file.readlines()]
            if delimiter != "\n":
                lines = "\n".join(lines).split(delimiter)
            return lines if len(lines) > 1 else lines[0]

    def solve_all(self, input: Optional[Any]=None):
        classname = self.__class__.__name__.lower()
        year = os.path.basename(os.getcwd())
        print(f"\n{year} {classname} challenge")
        filename = f"{classname}.txt"
        print("part 1 answer:",self.solve_part1(self.read_file(filename) if input is None else input))
        print("part 2 answer:",self.solve_part2(self.read_file(filename) if input is None else input))
