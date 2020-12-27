import sys
from typing import *


def read_file() -> List[str]:
    return [line for line in sys.stdin]


def find_trees(toboggan_map: List[str], down_move: int, right_move: int) -> int:
    pos = (0,0)
    tree_counter = 0
    while pos[0] < len(toboggan_map):
        if toboggan_map[pos[0]][pos[1]] == '#':
            tree_counter += 1
        pos = pos[0] + down_move, (pos[1] + right_move) % 31  # 31 is the len of a line
    return tree_counter


if __name__ == '__main__':
    toboggan_map = read_file()
    slope1 = find_trees(toboggan_map, 1,1)
    slope2 = find_trees(toboggan_map, 1,3)
    slope3 = find_trees(toboggan_map, 1,5)
    slope4 = find_trees(toboggan_map, 1,7)
    slope5 = find_trees(toboggan_map, 2,1)
    print(slope1)
    print(slope2)
    print(slope3)
    print(slope4)
    print(slope5)
    print(slope1*slope2*slope3*slope4*slope5)
