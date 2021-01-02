import sys


def read_file() -> dict:
    passes = {}
    for line in sys.stdin:
        line = line.rstrip().replace('B', r'1').replace('F', '0').replace('R', '1').replace('L', '0')
        passes.setdefault(line)
    return passes


def find_highest_seat(board_passes: dict) -> int:
    return int(max(board_passes), 2)  # , 2 is used to convert binary base to decimal base


def find_empty_seat(board_passes: dict) -> int:
    seat_ids = {}
    for seat in board_passes.keys():
        seat_ids.setdefault(int(seat, 2), int(seat, 2))

    for s in seat_ids.keys():
        seat_before = seat_ids.get(s-1)
        seat_after = seat_ids.get(s+1)
        if seat_before is None:
            seat_before_before = seat_ids.get(s-2)
            if seat_before_before is not None:
                return s-1
        if seat_after is None:
            seat_after_after = seat_ids.get(s+2)
            if seat_after_after is not None:
                return s+1


if __name__ == '__main__':
    boarding_passes = read_file()
    print("The highest seat ID is: {}".format(find_highest_seat(boarding_passes)))
    print("My seat is: {}".format(find_empty_seat(boarding_passes)))
