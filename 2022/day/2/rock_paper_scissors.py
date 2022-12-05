import sys
from typing import *


#           P1  P2
# ROCK:     A   X
# PAPER     B   Y
# SCISSORS  C   Z

rock_shape = 1
paper_shape = 2
scissor_shape = 3

lose_score = 0
draw_score = 3
win_score = 6


def read_data(f: IO):
    return [line.rstrip().split(" ") for line in f.readlines()]


def process_part1(c: List[List[chr]]):
    score = 0
    for play in c:
        if play[0] == 'A':  # rock first
            if play[1] == 'X':
                score += draw_score + rock_shape  # rock v rock
            if play[1] == 'Y':
                score += win_score + paper_shape  # rock v paper
            if play[1] == 'Z':
                score += lose_score + scissor_shape  # rock v scissors

        elif play[0] == 'B':  # paper first
            if play[1] == 'X':
                score += lose_score + rock_shape  # paper v rock
            if play[1] == 'Y':
                score += draw_score + paper_shape  # paper v paper
            if play[1] == 'Z':
                score += win_score + scissor_shape  # paper v scissor

        elif play[0] == 'C':  # scisssor first
            if play[1] == 'X':
                score += win_score + rock_shape  # scisssor v rock
            if play[1] == 'Y':
                score += lose_score + paper_shape  # scissor v paper
            if play[1] == 'Z':
                score += draw_score + scissor_shape  # scissor v scissor

    return score

def process_part2(c: List[List[chr]]):
    score = 0
    for play in c:
        if play[0] == 'A':  # rock first
            if play[1] == 'X':
                score += lose_score + scissor_shape  # need to lose -> scissor
            if play[1] == 'Y':
                score += draw_score + rock_shape  # need to draw -> rock
            if play[1] == 'Z':
                score += win_score + paper_shape  # need to win -> paper

        elif play[0] == 'B':  # paper first
            if play[1] == 'X':
                score += lose_score + rock_shape  # need to lose -> rock
            if play[1] == 'Y':
                score += draw_score + paper_shape  # need to draw -> paper
            if play[1] == 'Z':
                score += win_score + scissor_shape  # need to win -> scissor

        elif play[0] == 'C':  # scissor first
            if play[1] == 'X':
                score += lose_score + paper_shape  # need to lose -> paper
            if play[1] == 'Y':
                score += draw_score + scissor_shape  # need to draw -> scissor
            if play[1] == 'Z':
                score += win_score + rock_shape  # need to win -> rock

    return score


def show_results(score: int):
    print(f"Score following the guide: {score} points")


if __name__ == '__main__':
    c = read_data(sys.stdin)
    n = process_part2(c)
    show_results(n)
