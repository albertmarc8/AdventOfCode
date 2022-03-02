import sys
from typing import *


def read_data(f) -> List[int]:
    return [int(number) for number in f.readlines()]


def process(numbers: List[int]) -> int:
    prev_num: int = numbers[0]
    inc = 0
    for i in range(1, len(numbers)):
        if prev_num < numbers[i]:
            inc += 1
        prev_num = numbers[i]
    return inc


def show_results(result: int):
    print(f"The number of increment measurements is {result}")


if __name__ == '__main__':
    numbers = read_data(sys.stdin)
    increments = process(numbers)
    show_results(increments)
