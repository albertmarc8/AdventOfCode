import sys
import time
from typing import *


def read_data(f):
    cleaning_areas = []
    pair = (2, 5)
    for line in f.readlines():
        area_one, area_two = line.split(",")
        area_one_start, area_one_end = area_one.split("-")
        area_two_start, area_two_end = area_two.split("-")
        cleaning_areas.append(((int(area_one_start), int(area_one_end)), (int(area_two_start), int(area_two_end))))
    return cleaning_areas


def process_part1(c: List[Tuple[Tuple[int, int], Tuple[int, int]]]):
    fully_contained = 0
    for i, line in enumerate(c):
        a1s = line[0][0]
        a1e = line[0][1]
        a2s = line[1][0]
        a2e = line[1][1]

        if (a1e == a2e) or (a1s == a2s):
            fully_contained += 1
            continue

        if a1s < a2s:
            # el primero empieza antes que el segundo
            # a2s y a2e tiene que ser <= a1e
            if a2e <= a1e:
                fully_contained += 1
                continue

        elif a2s < a1s:
            # el segundo empieza antes que el primero
            # a1e y a2s tiene que ser <= a2e
            if a1e <= a2e:
                fully_contained += 1
                continue

    return fully_contained


# 911 too high
def process_part2(c: List[Tuple[Tuple[int, int], Tuple[int, int]]]):
    overlap = 0
    for i, line in enumerate(c):
        a1s = line[0][0]
        a1e = line[0][1]
        a2s = line[1][0]
        a2e = line[1][1]

        if (a1e == a2e) or (a1s == a2s):
            overlap += 1
            continue
        elif (a1e >= a2s) and (a2e >= a1s):
            overlap += 1
            continue

    return overlap


def show_results_part1(n: int):
    print(f"A total of {n} pairs fully contain the other.")


def show_results_part2(n: int):
    print(f"A total of {n} pairs overlap each other.")


if __name__ == '__main__':
    start_time = time.time()
    c = read_data(sys.stdin)
    n_part1 = process_part1(c)
    n_part2 = process_part2(c)
    show_results_part1(n_part1)
    show_results_part2(n_part2)
    print(f"--- %.8s seconds ---" % (time.time() - start_time))

