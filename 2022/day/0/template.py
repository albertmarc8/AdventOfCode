import sys
import time
from typing import *


def read_data(f: IO):
    pass


def process(c: List[List[int]]):
    pass


def show_results(n_elf: List[int], calories_carrying: List[int]):
    pass


if __name__ == '__main__':
    start_time = time.time()
    c = read_data(sys.stdin)
    n, n_cal = process(c)
    show_results(n, n_cal)
    print(f"--- %.8s seconds ---" % (time.time() - start_time))
