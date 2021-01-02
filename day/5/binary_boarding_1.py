import sys
from typing import *


def read_file() -> List[str]:
    array = []
    for line in sys.stdin:
        array.append(line.rstrip().replace('B', r'1').replace('F', '0').replace('R', '1').replace('L', '0'))
    return array


def find_highest_seat(board_passes: List[str]) -> int:
    return int(max(board_passes), 2)  # , 2 is used to convert binary base to decimal base


if __name__ == '__main__':
    boarding_passes = read_file()
    print(find_highest_seat(boarding_passes))
