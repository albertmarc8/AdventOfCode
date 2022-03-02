import typing, sys


def read_file() -> list:
    array = []
    for line in sys.stdin:
        array.append(line.rstrip())
    return array


def read_instructions(instruction_array):
    accumulator = 0
    instruction_run_times = [0] * len(instruction_array)
    instruction_number = 0

    while instruction_number >= 0 & instruction_number < len(instruction_array):
        instruction, string_number = instruction_array[instruction_number].split()
        signed_number = int(string_number)

        instruction_run_times[instruction_number] += 1
        if instruction_run_times[instruction_number] == 2:
            return accumulator
        else:
            if instruction == "acc":
                accumulator += signed_number
                instruction_number += 1
            if instruction == "jmp":
                instruction_number += signed_number
            if instruction == "nop":
                instruction_number += 1

    return accumulator


if __name__ == '__main__':
    print("Handheld halting")
    instruction_list = read_file()
    acc = read_instructions(instruction_list)
    print("Accumulator value is {}".format(acc))
