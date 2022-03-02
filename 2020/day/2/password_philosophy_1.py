import sys
from typing import *


def read_file():
    minimum, maximum, char, password = [], [], [], []

    for line in sys.stdin:
        minmax, character, passw = line.split(" ")
        minmax_split = minmax.split("-")
        minimum.append(int(minmax_split[0]))
        maximum.append(int(minmax_split[1]))
        char.append(character[:-1])
        password.append(passw)

    return minimum, maximum, char, password


if __name__ == '__main__':
    minimums, maximums, chars, passwords = read_file()
    ok_passwords = 0
    for i in range(len(passwords)):
        counter = 0
        for j in range(len(passwords[i])):
            if passwords[i][j] == chars[i]:
                counter += 1
        if minimums[i] <= counter <= maximums[i]:
            ok_passwords += 1

    print("Passwords that are OK = {}".format(ok_passwords))
