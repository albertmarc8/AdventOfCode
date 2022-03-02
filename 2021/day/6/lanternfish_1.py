import sys
from copy import copy
from typing import *


def read_data(f: IO):
    return [int(line) for line in f.readline().split(",")]


def process(fish_days: List[int]) -> int:
    # We will init an array of size 9 (max days a fish can live)
    # We will store each fish to its corresponding day
    days = [0] * 9
    for f in fish_days:
        days[f] += 1

    # After each day, the fish will transfer to its corresponding day, for example: day #6 fish will go to day #5
    remaining_days = 18
    counter = 0
    while remaining_days > 0:
        remaining_days -= 1
        new_fish = days[0]

        for n in range(len(days)-1):
            days[n] = days[n+1]
        days[5] += new_fish
        days[8] = new_fish
        counter += 1
        print(f"After {counter} days -> {days}")

    print(days[0:8])
    return sum(days[0:8])


def show_results(num_fish: int):
    print(f"The total amount of fish is {num_fish}")


if __name__ == '__main__':
    fish_days = read_data(sys.stdin)
    num_fish = process(fish_days)
    show_results(num_fish)