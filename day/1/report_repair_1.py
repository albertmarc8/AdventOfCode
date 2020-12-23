import sys
from typing import *


def read_file() -> List[int]:
    return [int(number) for number in sys.stdin]


if __name__ == '__main__':
    array = read_file()
    for x in array:
        for y in array:
            for z in array:
                if x+y == 2020:
                    print("The two entries that sum {} are x -> {} and y -> {}".format((x+y), x, y))
                    print("The product of these numbers is {}".format(x*y))
                    exit(0)
