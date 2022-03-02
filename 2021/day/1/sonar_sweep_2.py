import sys
from typing import *


def read_data(f) -> List[int]:
    return [int(number) for number in f.readlines()]


def process(numbers: List[int]) -> int:
    inc = 0
    group_one = 0
    if 4 <= len(numbers):
        group_one = sum(numbers[0:3])

    for i in range(4, len(numbers)+1):  # len() + 1 because the sum below wouldn't include the last number
        group_two = sum(numbers[i - 3:i])
        if group_one < group_two:
            inc += 1
        group_one = group_two
    return inc


def show_results(result: int):
    print(f"The number of grouped increment measurements is {result}")


if __name__ == '__main__':
    numbers = read_data(sys.stdin)
    increments = process(numbers)
    show_results(increments)
