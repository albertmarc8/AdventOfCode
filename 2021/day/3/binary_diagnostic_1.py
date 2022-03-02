import sys
from typing import *


def read_data(f) -> List[str]:
    return [line.rstrip() for line in f.readlines()]


def process(arr: List[str]) -> Tuple[int, int]:
    most_common_bits: List[int] = [0] * len(arr[0])
    for line in arr:
        for i in range(len(line)):
            if line[i] == '0':
                most_common_bits[i] -= 1
            elif line[i] == '1':
                most_common_bits[i] += 1

    # calculating gamma rate with the most common bits
    # if number is positive, most common bit is 1
    # if number is negative, most common bit is 0
    most_common_bit_sequence = ""
    least_common_bit_sequence = ""
    for num in most_common_bits:
        if num > 0:
            most_common_bit_sequence += "1"
            least_common_bit_sequence += "0"
        elif num < 0:
            most_common_bit_sequence += "0"
            least_common_bit_sequence += "1"

    g = int(most_common_bit_sequence, 2)
    e = int(least_common_bit_sequence, 2)
    return g, e


def show_results(g: int, e: int):
    print(f"The result of multiplying gamma = {g} and epsilon = {e} is {g * e}")


if __name__ == '__main__':
    directions = read_data(sys.stdin)
    gamma, epsilon = process(directions)
    show_results(gamma, epsilon)
