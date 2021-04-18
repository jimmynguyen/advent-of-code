import os


class Challenge:
    @staticmethod
    def solve_part1(input):
        raise NotImplementedError()

    @staticmethod
    def solve_part2(input):
        raise NotImplementedError()

    def read_file(self,filename,delimiter="\n"):
        with open(filename) as file:
            lines = [x.strip() for x in file.readlines()]
            if delimiter != "\n":
                lines = "\n".join(lines).split(delimiter)
            return lines if len(lines) > 1 else lines[0]

    def solve_all(self,input=None):
        classname = self.__class__.__name__.lower()
        year = os.path.basename(os.getcwd())
        print(f"\n{year} {classname} challenge")
        if input is None:
            filename = f"{classname}.txt"
            input = self.read_file(filename)
        print("part 1 answer:",self.solve_part1(input))
        print("part 2 answer:",self.solve_part2(input))
