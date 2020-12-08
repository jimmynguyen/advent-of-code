# https://adventofcode.com/2015/day/14
import util


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


def compute_max_score(distances,total_time):
    scores = [0] * len(distances)
    for i in range(total_time):
        _distances = [d[i] for d in distances]
        max_distance = max(_distances)
        for i,d in enumerate(_distances):
            scores[i] += 1 if d == max_distance else 0
    return max(scores)


def solve(reindeers,args):
    compute_score,total_time = args
    _reindeers = []
    for reindeer in reindeers:
        reindeer = reindeer.split(" ")
        _reindeers.append(tuple(map(int,[reindeer[3],reindeer[6],reindeer[-2]])))
    distances = compute_distances(_reindeers,total_time)
    return compute_score(distances,total_time)


if __name__ == "__main__":
    day = 14
    inputs = [
        (lambda x,y: max(z[y-2] for z in x),2503),
        (compute_max_score,2503)
    ]
    test_inputs2 = [
        (lambda x,y: max(z[y-2] for z in x),1000),
        (compute_max_score,1000)
    ]
    test_outputs = [1120,689]
    util.solve(day,inputs,test_outputs,solve,test_inputs2=test_inputs2)