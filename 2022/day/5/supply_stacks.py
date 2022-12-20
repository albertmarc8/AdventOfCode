import sys
import time
from typing import *


def read_data(f):
    cranes = []
    movements = []
    movs = False
    firstLine = True
    for line in f.readlines():
        line = line.rstrip()
        if movs:
            # adding to movement
            container, directions = line.split(" from ")
            container = container[5:]
            start, finish = directions.split(" to ")
            movements.append((int(container), int(start) - 1, int(finish) - 1))  # -1 to match index 0
        else:
            # adding to crane
            if len(line) == 0:
                movs = True
            elif not line.startswith(" 1"):
                if firstLine:
                    for i in range(1, len(line), 4):
                        if line[i] == ' ':
                            cranes.append([])
                        else:
                            cranes.append([line[i]])
                    firstLine = False
                else:
                    for i in range(1, len(line), 4):
                        if line[i] != ' ':
                            cranes[int(((i - 1) / 4))].insert(0, line[i])

    return cranes, movements


def process(c: List[List[str]], m: List[Tuple[int, int, int]], stack: bool):
    for mov in m:
        n_cont, c_source, c_dest = mov
        pop_location = len(c[c_source]) - n_cont
        for x in range(n_cont):
            if stack:
                c[c_dest].append(c[c_source].pop(pop_location))
            else:
                c[c_dest].append(c[c_source].pop())

    top_containers = []
    for i, cont in enumerate(c):
        top_containers.append(c[i][(len(c[i]) - 1)])

    return top_containers


def show_results(l: List[str]):
    print(f"The top containers are: ")
    for c in range(len(l)):
        print(f"{l[c]}", end="")
    print("")


if __name__ == '__main__':
    start_time = time.time()
    cr, mv = read_data(sys.stdin)
    # top_cont = process(cr, mv, False)
    top_cont = process(cr, mv, True)
    show_results(top_cont)
    print(f"--- %.8s seconds ---" % (time.time() - start_time))
