import sys
import time


def read_data(f):
    return f.readline()


def process(c: str):
    distinct_chars = 14
    if len(c) > distinct_chars:
        for i in range(len(c) - distinct_chars):
            fourchars = set(c[i:i + distinct_chars])
            if len(fourchars) == distinct_chars:
                return i + distinct_chars


def show_results(n: int):
    print(f"Found it at index {n}")


if __name__ == '__main__':
    start_time = time.time()
    c = read_data(sys.stdin)
    n = process(c)
    show_results(n)
    print(f"--- %.8s seconds ---" % (time.time() - start_time))
