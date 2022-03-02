import sys


def read_file():
    return [line for line in sys.stdin]


if __name__ == '__main__':
    toboggan_map = read_file()
    pos = (0,0)
    down_move = 1
    right_move = 3
    tree_counter = 0
    line_counter = 0

    while pos[0] < len(toboggan_map):
        if toboggan_map[pos[0]][pos[1]] == '#':
            tree_counter += 1
        pos = pos[0] + down_move, (pos[1] + right_move) % 31 # 31 is the len of a line

    print("Trees encountered: {}".format(tree_counter))
