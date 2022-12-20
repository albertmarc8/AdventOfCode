import sys
import time
from typing import *

priority_values = {}
for i in range(1, 27):
    priority_values.update({chr(i + 96): i})
for j in range(27, 53):
    priority_values.update({chr(j + 38): j})


def read_data(f):
    return [line.rstrip() for line in f.readlines()]


def process_part1(c: List[str]):
    priority_sum = 0
    for line in c:
        rucksack_one = set(line[:len(line) // 2])
        rucksack_two = set(line[len(line) // 2:])

        common_item = rucksack_one.intersection(rucksack_two)
        priority_sum += priority_values.get(common_item.pop())
    return priority_sum


def process_part2(c: List[str]):
    n_group = 3
    i_group = 1
    group_common_item = set()
    priority_sum = 0
    for line in c:
        if i_group == 1:
            group_common_item = set(line)
            i_group += 1
        elif i_group == n_group:
            group_common_item = group_common_item.intersection(set(line))
            priority_sum += priority_values.get(group_common_item.pop())
            i_group = 1
        else:
            group_common_item = group_common_item.intersection(set(line))
            i_group += 1
    return priority_sum


def show_results(n: int):
    print(f"The sum of the priority items is {n}")


if __name__ == '__main__':
    start_time = time.time()
    c = read_data(sys.stdin)
    n = process_part2(c)
    show_results(n)
    print(f"--- %.8s seconds ---" % (time.time() - start_time))
