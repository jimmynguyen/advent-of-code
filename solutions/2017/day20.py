# https://adventofcode.com/2017/day/20
# https://www.reddit.com/r/adventofcode/comments/7kz6ik/comment/dric7uj/
from solutions.challenge import Challenge
from collections import namedtuple
from typing import List


Particle = namedtuple("Particle", ["position", "velocity", "acceleration"])


class Day20(Challenge):
    def read_file(self, filename: str) -> List[Particle]:
        return [Particle(position, velocity, acceleration) for position, velocity, acceleration in [tuple(map(lambda y: tuple(map(int, y[y.index("<")+1:y.index(">")].split(","))), x.split(", "))) for x in super().read_file(filename)]]

    @staticmethod
    def move_particle(particle: Particle) -> Particle:
        new_velocity = tuple(v + a for v, a in zip(particle.velocity, particle.acceleration))
        new_position = tuple(p + v for p, v in zip(particle.position, new_velocity))
        return Particle(new_position, new_velocity, particle.acceleration)

    @staticmethod
    def compute_manhattan_distance(particle: Particle) -> int:
        return sum(abs(p) for p in particle.position)

    @staticmethod
    def solve_part1(particles: List[Particle]) -> int:
        for _ in range(1000):
            particles = [Day20.move_particle(p) for p in particles]
        return particles.index(min(particles, key=Day20.compute_manhattan_distance))

    @staticmethod
    def solve_part2(particles: List[Particle]) -> int:
        for _ in range(1000):
            if len(set(p.position for p in particles)) < len(particles):
                positions = [p.position for p in particles]
                particles = [part for part, pos in zip(particles, positions) if positions.count(pos) == 1]
            particles = [Day20.move_particle(p) for p in particles]
        return len(particles)


if __name__ == "__main__":
    Day20().solve_all()
