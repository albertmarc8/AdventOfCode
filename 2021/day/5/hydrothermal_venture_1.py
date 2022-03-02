import sys
from typing import *

Coordinate = Tuple[int, int]
Direction = Tuple[Coordinate, Coordinate]


def read_data(f: IO) -> Tuple[List[Direction], int, int]:
    arr: List[Direction] = []
    max_row, max_col = 0, 0
    for line in f.readlines():
        coordinates = line.rstrip().split(" -> ")
        x1, y1 = coordinates[0].split(",")
        x2, y2 = coordinates[1].split(",")
        x1 = int(x1)
        y1 = int(y1)
        x2 = int(x2)
        y2 = int(y2)
        if max_row < x1:
            max_row = x1
        if max_row < x2:
            max_row = x2
        if max_col < y1:
            max_col = y1
        if max_col < y2:
            max_col = y2
        arr.append(((x1, y1), (x2, y2)))

    return arr, max_row+1, max_col+1


def process(directions: List[Direction], rows: int, cols: int):

    def crossing_path(direction: Direction) -> List[Coordinate]:
        #print(f"Finding path from {direction[0]} to {direction[1]}")
        coord1, coord2 = direction
        path: List[Coordinate] = []
        if coord1[0] == coord2[0]:
            # Same column
            start, end = 0, 0
            if coord1[1] > coord2[1]:
                # Direction is up
                start = coord2[1]
                end = coord1[1] + 1
            else:
                # Direction is down or the same
                start = coord1[1]
                end = coord2[1] + 1
            for x in range(start, end):
                path.append((coord1[0], x))

        elif coord1[1] == coord2[1]:
            # Row is the same
            start, end = 0, 0
            if coord1[0] > coord2[0]:
                # Direction is right
                start = coord2[0]
                end = coord1[0] + 1
            else:
                # Direction is left
                start = coord1[0]
                end = coord2[0] + 1
            for x in range(start, end):
                path.append((x, coord1[1]))

        return path

    arr = []
    for _ in range(rows):
        arr.append([0] * cols)
    for direction in directions:
        path = crossing_path(direction)
        for x, y in path:
            arr[x][y] += 1
    counter = 0
    for x in range(len(arr)):
        for y in range(len(arr[x])):
            if arr[x][y] > 1:
                counter += 1
    return counter


def show_results(num_dangerous_points: int):
    print(f"The number of dangerous points is {num_dangerous_points}")


if __name__ == '__main__':
    directions, r, c = read_data(sys.stdin)
    num_dangerous_points = process(directions, r, c)
    show_results(num_dangerous_points)
