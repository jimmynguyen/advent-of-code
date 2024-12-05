# https://adventofcode.com/2015/day/14
from solutions.challenge import Challenge


class Day14(Challenge):
    @staticmethod
    def compute_distances(reindeers,total_time):
        distances_list = []
        for speed,fly_duration,rest_duration in reindeers:
            distances = []
            for t in range(1,total_time+1):
                flying = True
                distance = 0
                time = 0
                while time < t:
                    if flying:
                        min_fly_duration = min(fly_duration,t - time)
                        time += min_fly_duration
                        distance += min_fly_duration * speed
                    else:
                        time += rest_duration
                    flying = not flying
                distances.append(distance)
            distances_list.append(distances)
        return distances_list

    @staticmethod
    def compute_max_score(distances,total_time):
        return max(z[total_time-2] for z in distances)

    @staticmethod
    def compute_max_score_2(distances,total_time):
        scores = [0] * len(distances)
        for i in range(total_time):
            _distances = [d[i] for d in distances]
            max_distance = max(_distances)
            for i,d in enumerate(_distances):
                scores[i] += 1 if d == max_distance else 0
        return max(scores)

    @staticmethod
    def solve(reindeers,args):
        compute_score,total_time = args
        _reindeers = []
        for reindeer in reindeers:
            reindeer = reindeer.split(" ")
            _reindeers.append(tuple(map(int,[reindeer[3],reindeer[6],reindeer[-2]])))
        distances = Day14.compute_distances(_reindeers,total_time)
        return compute_score(distances,total_time)

    @staticmethod
    def solve_part1(input):
        return Day14.solve(input,(Day14.compute_max_score,2503))

    @staticmethod
    def solve_part2(input):
        return Day14.solve(input,(Day14.compute_max_score_2,2503))


if __name__ == "__main__":
    Day14().solve_all()
