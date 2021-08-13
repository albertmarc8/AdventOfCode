import sys
from typing import *


def read_file() -> List[int]:
    arr = []
    for line in sys.stdin:
        arr.append(int(line.rstrip()))
    arr.sort()
    return arr


def find_joltage(arr, i):
    joltage_counter = 0
    one_joltage = 0
    three_joltage = 0

    while i < len(arr):
        if joltage_counter == arr[i] - 1:
            one_joltage += 1
            joltage_counter += 1
        elif joltage_counter == arr[i] - 3:
            three_joltage += 1
            joltage_counter += 3

        i += 1

    # my built in adapter adds 1 to three_joltage
    three_joltage += 1
    print("One joltage -> {}".format(one_joltage))
    print("Three joltage -> {}".format(three_joltage))
    print("What is the number of 1-jolt differences multiplied by the number of 3-jolt differences?")
    print(one_joltage * three_joltage)


def find_possible_combinations(arr, i):
    joltage_counter = 0
    one_joltage = 0
    three_joltage = 0

    while i < len(arr):
        if joltage_counter == arr[i] - 1:
            one_joltage += 1
        if joltage_counter == arr[i] - 3:
            three_joltage += 1
        joltage_counter = arr[i]
        i += 1
    # my built in adapter adds 1 to three_joltage
    three_joltage += 1
    print("One joltage -> {}".format(one_joltage))
    print("Three joltage -> {}".format(three_joltage))
    print("Possibilities: ")
    print(one_joltage + three_joltage)


def find_possible_combinations_recursive(arr, i) -> int:
    joltage_counter = 0
    one_joltage = 0
    three_joltage = 0
    counter = 0
    while i < len(arr):
        if joltage_counter == arr[i] - 1:
            one_joltage += 1
            counter += find_possible_combinations_recursive(arr, (i+1))

        if joltage_counter == arr[i] - 3:
            three_joltage += 1
            counter += find_possible_combinations_recursive(arr, (i+1))
        joltage_counter = arr[i]
        i += 1
    # my built in adapter adds 1 to three_joltage
    print(counter)
    three_joltage += 1
    print("One joltage -> {}".format(one_joltage))
    print("Three joltage -> {}".format(three_joltage))
    print("Possibilities: ")
    print(one_joltage + three_joltage)
    return counter

if __name__ == '__main__':
    arr = read_file()
    find_joltage(arr, 0)
    find_possible_combinations_recursive(arr, 0)