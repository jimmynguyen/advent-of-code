# https://adventofcode.com/2018/day/10
from solutions.challenge import Challenge
import re
from PIL import Image
import tempfile
import pytesseract
import matplotlib.pyplot as plt
from datetime import datetime


ParsedChallengeInput = list[tuple[int,int,int,int]]


def run_ocr(
    particles: list[tuple[int,int,int,int]],
    figsize: tuple[int,int],
    debug: bool = False,
) -> str:
    x = [particle[0] for particle in particles]
    y = [particle[1] for particle in particles]
    fig = plt.figure(figsize=figsize)
    plt.scatter(x, y, c="black", marker="s", s=150)
    plt.gca().invert_yaxis()
    plt.axis("off")
    filename = f"/Users/jimmynguyen/Desktop/tmp.{int(datetime.now().timestamp())}.png" if debug else f"{tempfile.gettempdir()}/tmp.png"
    plt.savefig(filename, dpi=300, bbox_inches="tight", pad_inches=1)
    plt.show(block=False)
    if debug:
        plt.pause(0.5)
    plt.close(fig)

    # psm 8 = treat the image as a single word
    text = pytesseract.image_to_string(Image.open(filename), config="--psm 8")

    return re.sub(r"[^a-zA-Z0-9]", "", text)


class Day10(Challenge):
    @staticmethod
    def parse_file(lines: list[str]) -> ParsedChallengeInput:
        particles = []
        for line in lines:
            pattern = r"position=<\s*(.*?),\s*(.*?)> velocity=<\s*(.*?),\s*(.*?)>"
            match = re.search(pattern, line)
            x, y, vx, vy = int(match.group(1)), int(match.group(2)), int(match.group(3)), int(match.group(4))
            particles.append((x, y, vx, vy))
        return particles

    def read_file(self,filename) -> ParsedChallengeInput:
        return self.parse_file(super().read_file(filename))

    @staticmethod
    def solve_part1(
        particles: ParsedChallengeInput,
        figsize: tuple[int,int] = (10,1.2),
        part2: bool = False,
    ):
        # find best iteration by minimizing bounding box area
        best_iter = 0
        min_width_height = float("inf")
        for iter in range(20000):
            px = [x + iter * vx for x, _, vx, _ in particles]
            py = [y + iter * vy for _, y, _, vy in particles]
            xmin = min(px)
            xmax = max(px)
            ymin = min(py)
            ymax = max(py)
            area = (xmax - xmin) + (ymax - ymin)
            if area < min_width_height:
                min_width_height = area
                best_iter = iter

        # update particles to best iteration
        particles = [(x + best_iter * vx, y + best_iter * vy, vx, vy) for x, y, vx, vy in particles]

        return best_iter if part2 else run_ocr(particles, figsize)

    @staticmethod
    def solve_part2(
        particles: ParsedChallengeInput,
        figsize: tuple[int,int] = (10,1.2),
    ):
        return Day10.solve_part1(particles, figsize, part2=True)


if __name__ == "__main__":
    Day10().solve_all()
