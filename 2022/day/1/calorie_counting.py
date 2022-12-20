import sys
import time
from typing import *


def read_data(f: IO):
    calories = []
    arr = []
    for line in f.readlines():
        if not line == '\n':
            arr.append(int(line))
        else:
            calories.append(arr)
            arr = []
    return calories


def process(c: List[List[int]]):
    n_top = 3
    max_calories = [0 for _ in range(n_top)]
    i_max = [0 for _ in range(n_top)]

    for i, arr in enumerate(c):
        elf_sum = sum(arr)

        for n in range(n_top):
            if elf_sum > max_calories[n]:
                max_calories.insert(n, elf_sum)
                i_max.insert(n, i)
                max_calories.pop(3)
                i_max.pop(3)
                break


    return i_max, max_calories


def show_results(n_elf: List[int], calories_carrying: List[int]):
    for n in range(len(n_elf)):
        print(f"The #{n+1} elf with most calories is {n_elf[n]} and carrying {calories_carrying[n]} calories.")
    print(f"Those elves are carrying {sum(calories_carrying)} calories.")


if __name__ == '__main__':
    start_time = time.time()
    c = read_data(sys.stdin)
    n, n_cal = process(c)
    show_results(n, n_cal)
    print("--- %s seconds ---" % (time.time() - start_time))

