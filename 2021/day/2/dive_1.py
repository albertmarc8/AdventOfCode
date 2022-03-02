import sys
from typing import *


def read_data(f) -> List[Tuple[str, int]]:
    arr: List[Tuple[str, int]] = []
    for line in f.readlines():
        line = line.split()
        arr.append((line[0], int(line[1])))
    return arr


def process(dirs: List[Tuple[str, int]]) -> Tuple[int, int]:
    h_pos = 0
    depth = 0
    for dir, value in dirs:
        if dir == "forward":
            h_pos += value
        elif dir == "down":
            depth += value
        elif dir == "up":
            depth -= value

    return h_pos, depth


def show_results(h: int, d: int):
    print(f"The result of multiplying horizontal pos = {h} and depth = {d} is {h*d}")


if __name__ == '__main__':
    directions = read_data(sys.stdin)
    horizontal_position, depth_position = process(directions)
    show_results(horizontal_position, depth_position)