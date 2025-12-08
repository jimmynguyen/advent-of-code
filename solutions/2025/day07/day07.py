# https://adventofcode.com/2025/day/7
from solutions.challenge import Challenge
from collections import Counter, deque


ParsedChallengeInput = list[str]


class Day07(Challenge):
    def read_file(self,filename) -> ParsedChallengeInput:
        return super().read_file(filename, delimiter="\n", strip=False)


    @staticmethod
    def solve_part1(
        parsed_input: ParsedChallengeInput,
        debug: bool = False,
    ):
        lines = parsed_input
        beam_indices = {lines[0].index("S")}
        if debug:
            new_lines = [lines[0]]
        split_count = 0
        for line in lines[1:]:
            new_line = line
            if "^" in line: # has splitter
                splitter_indices = [idx for idx, character in enumerate(line) if character == "^"]
                for idx in beam_indices.difference(splitter_indices):
                    new_line = new_line[:idx] + "|" + new_line[idx+1:]
                for idx in beam_indices.intersection(splitter_indices):
                    new_line = new_line[:idx-1] + "|^|" + new_line[idx+2:]
                    split_count += 1
                    beam_indices.remove(idx)
                    beam_indices.add(idx-1)
                    beam_indices.add(idx+1)
                if debug:
                    new_lines.append(new_line)
            elif debug:
                for beam_idx in beam_indices:
                    new_line = new_line[:beam_idx] + "|" + new_line[beam_idx+1:]
                new_lines.append(new_line)
            if debug:
                [print(x) for x in new_lines]
                print()
        return split_count


    @staticmethod
    def solve_part2(
        parsed_input: ParsedChallengeInput,
        debug: bool = False,
        soln_version: str = "counter"
    ):
        lines = parsed_input

        if soln_version == "counter":
            paths = Counter()
            for line in lines:
                for idx, character in enumerate(line):
                    match character:
                        case "S":
                            paths[idx] = 1
                        case "^":
                            if idx in paths:
                                paths[idx-1] += paths[idx]
                                paths[idx+1] += paths[idx]
                                del paths[idx]
            return paths.total()
        elif soln_version != "dfs_brute_force":
            queue = deque([(lines[0].index("S"), 1, [lines[0].index("S")])])
            timeline_count = 0
            if debug:
                timelines = set()
            while queue:
                idx_beam, idx_line, beam_path = queue.pop()
                if debug:
                    for idx, line in enumerate(lines):
                        if idx == 0:
                            print(line)
                        elif idx >= len(beam_path):
                            break
                        else:
                            print(line[:beam_path[idx]] + "|" + line[beam_path[idx]+1:])
                while idx_line < len(lines) and "^" not in lines[idx_line]:
                    beam_path.append(beam_path[-1])
                    idx_line += 1
                if idx_line >= len(lines):
                    timeline_count += 1
                    if debug:
                        timelines.add(beam_path)
                    continue
                if lines[idx_line][idx_beam] == "^":
                    queue.append((idx_beam+1, idx_line+1, beam_path + [idx_beam+1]))
                    queue.append((idx_beam-1, idx_line+1, beam_path + [idx_beam-1]))
                else:
                    queue.append((idx_beam, idx_line+1, beam_path + [idx_beam]))
            if debug:
                assert len(timelines) == timeline_count, "Expected timeline count to match number of timelines"
                print("DEBUG\n-----")
                for beam_path in sorted(timelines):
                    for idx, line in enumerate(lines):
                        if idx == 0:
                            print(line)
                        elif idx >= len(beam_path):
                            break
                        else:
                            print(line[:beam_path[idx]] + "|" + line[beam_path[idx]+1:])
                    print("-----")
            return timeline_count
        else:
            raise RuntimeError(f"Unsupported solution version: {soln_version}")


if __name__ == "__main__":
    Day07().solve_all()
