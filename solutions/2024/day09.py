# https://adventofcode.com/2024/day/9
from challenge import Challenge


ParsedChallengeInput = str


class Day09(Challenge):
    def read_file(self, filename: str) -> ParsedChallengeInput:
        return super().read_file(filename)

    @staticmethod
    def solve_part1(disk_map: ParsedChallengeInput) -> int:
        expanded_disk_map = []
        id = 0
        for idx in range(0, len(disk_map), 2):
            num_file_blocks = int(disk_map[idx])
            num_free_blocks = int(disk_map[idx+1]) if idx+1 < len(disk_map) else 0
            if num_file_blocks > 0:
                expanded_disk_map.append((id, num_file_blocks))
                id += 1
            if num_free_blocks > 0:
                expanded_disk_map.append((None, num_free_blocks))

        # remove all tailing free blocks
        while expanded_disk_map[-1][0] is None:
            expanded_disk_map.pop()

        idx_free = 0
        while any(id is None for id, _ in expanded_disk_map):
            id, num_file_blocks = expanded_disk_map.pop()
            while num_file_blocks > 0 and idx_free < len(expanded_disk_map):
                while idx_free < len(expanded_disk_map) and expanded_disk_map[idx_free][0] is not None:
                    idx_free += 1
                if idx_free >= len(expanded_disk_map):
                    break
                _, num_free_blocks = expanded_disk_map[idx_free]
                if num_free_blocks == num_file_blocks:
                    expanded_disk_map[idx_free] = (id, num_file_blocks)
                    num_file_blocks -= num_file_blocks
                elif num_free_blocks > num_file_blocks:
                    expanded_disk_map[idx_free] = (id, num_file_blocks)
                    expanded_disk_map = expanded_disk_map[:idx_free+1] + [(None, num_free_blocks - num_file_blocks)] + expanded_disk_map[idx_free+1:]
                    num_file_blocks -= num_file_blocks
                else:
                    expanded_disk_map[idx_free] = (id, num_free_blocks)
                    num_file_blocks -= num_free_blocks
            if idx_free >= len(expanded_disk_map):
                expanded_disk_map.append((id, num_file_blocks))

        checksum = 0
        idx = 0
        for id, count in expanded_disk_map:
            for _ in range(count):
                checksum += id * idx
                idx += 1
        return checksum


    @staticmethod
    def solve_part2(disk_map: ParsedChallengeInput) -> int:
        expanded_disk_map = []
        id = 0
        for idx in range(0, len(disk_map), 2):
            num_file_blocks = int(disk_map[idx])
            num_free_blocks = int(disk_map[idx+1]) if idx+1 < len(disk_map) else 0
            if num_file_blocks > 0:
                expanded_disk_map.append((id, num_file_blocks))
                id += 1
            if num_free_blocks > 0:
                expanded_disk_map.append((None, num_free_blocks))

        # remove all tailing free blocks
        while expanded_disk_map[-1][0] is None:
            expanded_disk_map.pop()

        idx_expanded_disk_map = len(expanded_disk_map) - 1
        while any(id is None for id, _ in expanded_disk_map) and idx_expanded_disk_map >= 0:
            while idx_expanded_disk_map >= len(expanded_disk_map):
                idx_expanded_disk_map -= 1
            id, num_file_blocks = expanded_disk_map[idx_expanded_disk_map]
            if id is not None:
                idx_free = 0
                while num_file_blocks > 0 and idx_free < len(expanded_disk_map):
                    while idx_free < len(expanded_disk_map) and (expanded_disk_map[idx_free][0] is not None or expanded_disk_map[idx_free][1] < num_file_blocks):
                        idx_free += 1
                    if idx_free >= len(expanded_disk_map) or idx_free > idx_expanded_disk_map:
                        break
                    _, num_free_blocks = expanded_disk_map[idx_free]
                    if num_free_blocks == num_file_blocks:
                        expanded_disk_map[idx_free] = (id, num_file_blocks)
                        expanded_disk_map[idx_expanded_disk_map] = (None, num_file_blocks)
                        break
                    elif num_free_blocks > num_file_blocks:
                        expanded_disk_map[idx_free] = (id, num_file_blocks)
                        expanded_disk_map = expanded_disk_map[:idx_free+1] + [(None, num_free_blocks - num_file_blocks)] + expanded_disk_map[idx_free+1:]
                        idx_expanded_disk_map += 1
                        expanded_disk_map[idx_expanded_disk_map] = (None, num_file_blocks)
                        break
                    else:
                        idx_free += 1

            # remove all tailing free blocks
            while expanded_disk_map[-1][0] is None:
                expanded_disk_map.pop()

            idx_expanded_disk_map -= 1

        checksum = 0
        idx = 0
        for id, count in expanded_disk_map:
            for _ in range(count):
                if id is not None:
                    checksum += id * idx
                idx += 1
        return checksum


if __name__ == "__main__":
    Day09().solve_all()
