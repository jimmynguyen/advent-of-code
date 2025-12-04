# https://adventofcode.com/2017/day/23
from solutions.challenge import Challenge


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


class Day23(Challenge):
    def read_file(self, filename: str) -> list[str]:
        return super().read_file(filename)


    @staticmethod
    def solve(
        instructions: list[str],
        part2: bool = False,
        verbose: bool = False,
    ) -> int:
        registers = {register: 1 if part2 and register == "a" else 0 for register in "abcdefgh"}
        mul_count = 0
        idx = 0
        iteration = 0
        while idx < len(instructions):
            iteration += 1
            if iteration % 1000 == 0 and verbose:
                print(f"iteration {iteration}")
            instruction = instructions[idx]
            cmd, val1, val2 = instruction.split(" ")
            match cmd:
                case "set":
                    registers[val1] = registers[val2] if val2 in registers else int(val2)
                case "sub":
                    registers[val1] -= registers[val2] if val2 in registers else int(val2)
                case "mul":
                    registers[val1] *= registers[val2] if val2 in registers else int(val2)
                    mul_count += 1
                case "jnz":
                    if (registers[val1] if val1 in registers else int(val1)) != 0:
                        idx += int(val2)
                        continue
            idx += 1
        if not part2:
            return mul_count
        return registers["h"]


    @staticmethod
    def solve_part1(
        instructions: list[str],
    ) -> int:
        return Day23.solve(instructions)


    @staticmethod
    def solve_part2(
        instructions: list[str],
        soln_version: str = "optimized",
    ) -> int:
        match soln_version:
            case "naive":
                return Day23.solve(instructions, part2=True)
            case "disassembled":
                h = 0
                b = int(instructions[0].split()[2]) * 100 + 100000
                c = b + 17000
                while True:
                    f = 1
                    d = 2
                    while True:
                        e = 2
                        while True:
                            g = d * e - b
                            if g == 0:
                                f = 0
                            e += 1
                            g = e - b
                            if g == 0:
                                break
                        d += 1
                        g = d - b
                        if g == 0:
                            break
                    if f == 0:
                        h += 1
                    g = b - c
                    if g == 0:
                        return h
                    b += 17
            case "disassembled_and_optimized_inner_loop":
                h = 0
                b = int(instructions[0].split()[2]) * 100 + 100000
                c = b + 17000
                while True:
                    f = 1
                    d = 2
                    while True:
                        if b % d == 0:
                            f = 0
                            break
                        d += 1
                        g = d - b
                        if g == 0:
                            break
                    if f == 0:
                        h += 1
                    g = b - c
                    if g == 0:
                        return h
                    b += 17
            case "optimized":
                h = 0
                b = int(instructions[0].split()[2]) * 100 + 100000
                c = b + 17000
                for x in range(b, c + 1, 17):
                    if not is_prime(x):
                        h += 1
                return h
            case _:
                raise Exception(f"Unsupported soln_version={soln_version}")


if __name__ == "__main__":
    Day23().solve_all()
