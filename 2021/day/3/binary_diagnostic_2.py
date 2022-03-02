import sys
from copy import copy
from typing import *


def read_data(f) -> List[str]:
    return [line.rstrip() for line in f.readlines()]


def process(arr: List[str]) -> Tuple[int, int]:
    oxygen_numbers = copy(arr)
    scrubber_rating = copy(arr)

    for i in range(len(arr)):
        most_common_bit = 0
        for j in range(len(arr[i])):
            most_common_bit += 1 if arr[i][j] == '1' else -1

        bit_to_keep = '0' if most_common_bit < 0 else '1'

        counter = len(oxygen_numbers) - 1
        while len(oxygen_numbers) > 1 and counter >= 0:
            if oxygen_numbers[counter][i] != bit_to_keep:
                oxygen_numbers.pop(counter)
            counter -= 1

        most_common_bit = 0
        for j in range(len(arr[i])):
            most_common_bit += 1 if arr[i][j] == '1' else -1

        bit_to_keep = '1' if most_common_bit < 0 else '0'

        counter = len(scrubber_rating) - 1
        while len(scrubber_rating) > 1 and counter >= 0:
            if scrubber_rating[counter][i] != bit_to_keep:
                scrubber_rating.pop(counter)
            counter -= 1

    oxygen_generator_rating = oxygen_numbers.pop()
    co2_scrubber_rating = scrubber_rating.pop()

    print(oxygen_generator_rating)
    print(co2_scrubber_rating)
    o_decimal = int(oxygen_generator_rating, 2)
    c_decimal = int(co2_scrubber_rating, 2)
    return o_decimal, c_decimal


def show_results(o: int, s: int):
    print(f"The result of multiplying oxygen rating = {o} and scrubber rating = {s} is {o * s}")


if __name__ == '__main__':
    directions = read_data(sys.stdin)
    oxygen_rate, scrubber_rate = process(directions)
    show_results(oxygen_rate, scrubber_rate)
