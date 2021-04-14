# https://adventofcode.com/2016/day/4
from challenge import Challenge


class Day04(Challenge):
    def read_file(self,filename):
        return [(y,) + (int(x.split("[")[0]),x.split("[")[1].strip("]")) for x,y in [tuple(map(lambda x: x[::-1],x[::-1].split("-",maxsplit=1))) for x in super().read_file(filename)]]

    @staticmethod
    def verify_checksum(name,checksum):
        d = dict()
        for x in name.replace("-",""):
            if x not in d:
                d[x] = 0
            d[x] += 1
        return all(x == y for x,y in zip([x for x,_ in sorted(d.items(),key=lambda x: (-x[1],x[0]))],checksum))

    @staticmethod
    def solve_part1(rooms):
        return sum(sector_id for name,sector_id,checksum in rooms if Day04.verify_checksum(name,checksum))

    @staticmethod
    def solve_part2(rooms):
        for name,sector_id,checksum in rooms:
            if Day04.verify_checksum(name,checksum):
                decrypted_name = "".join(" " if x == "-" else chr(((ord(x)-ord('a')+sector_id)%26)+ord('a')) for x in name)
                if all(x in decrypted_name for x in ["north","pole","object"]):
                    return sector_id
        return None


if __name__ == "__main__":
    Day04().solve_all()
