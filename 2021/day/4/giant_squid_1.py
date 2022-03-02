import sys
from typing import *

Board = List[List[int]]
Score = int


def read_data(f) -> Tuple[List[int], List[Board]]:
    bingo_nums: List[int] = []
    for number in f.readline().split(','):
        bingo_nums.append(int(number))

    b_boards: List[Board] = []
    board_local: Board = []
    for line in f.readlines():
        if len(line.rstrip()) > 0:
            board_local_internal: List[int] = []
            for number in line.rstrip().split():
                board_local_internal.append(int(number))
            board_local.append(board_local_internal)
        else:
            if len(board_local) > 0:
                b_boards.append(board_local)
                board_local = []
    if len(board_local) > 0:
        b_boards.append(board_local)

    return bingo_nums, b_boards


def process(numbers: List[int], bingo_boards: List[Board]) -> Score:
    def mark_number(x: int) -> Tuple[bool, int]:
        for n_b in range(len(bingo_boards)):
            for n_r in range(len(bingo_boards[n_b])):
                for n_c in range(len(bingo_boards[n_b][n_r])):
                    if bingo_boards[n_b][n_r][n_c] == x:
                        bingo_boards[n_b][n_r][n_c] = -1
                        # We also check if the board is a winner
                        winner = True
                        for n in bingo_boards[n_b][n_r]:
                            if n != -1:
                                winner = False
                                break

                        if winner:
                            print(f"BINGO! Board {n_b} found winner on row {n_r}")
                            return winner, n_b

                        winner = True
                        for m in range(len(bingo_boards[n_b][n_r])):
                            if bingo_boards[n_b][m][n_c] != -1:
                                winner = False
                                break
                        if winner:
                            print(f"BINGO! Board {n_b} found winner on col {n_c}")
                            return winner, n_b

        return False, len(bingo_boards)-1

    def sum_unmarked_numbers(winning_board: int) -> Score:
        suma = 0
        for r in range(len(bingo_boards[winning_board])):
            for c in range(len(bingo_boards[winning_board][r])):
                if bingo_boards[winning_board][r][c] != -1:
                    suma += bingo_boards[winning_board][r][c]
        return suma

    for number in numbers:
        print(f"Number {number} is out!")
        bingo, winner_bingo = mark_number(number)
        if bingo:
            print(f"Board {winner_bingo} won")
            unmarked_sum = sum_unmarked_numbers(winner_bingo)
            print(f"Unmarked sum: {unmarked_sum} and number {number}")
            return unmarked_sum * number
    return 0


def show_results(score: Score):
    print(f"Final score: {score}")


if __name__ == '__main__':
    numbers, bingo_boards = read_data(sys.stdin)
    score = process(numbers, bingo_boards)
    show_results(score)
