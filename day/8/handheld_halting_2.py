import sys


def read_file() -> list:
    array = []
    for line in sys.stdin:
        array.append(line.rstrip())
    return array


def read_instructions(instruction_array):
    accumulator = 0
    instruction_run_times = [0] * len(instruction_array)
    instruction_number = 0

    #while (instruction_number >= 0) & (instruction_number < len(instruction_array)):
    while (instruction_number >= 0 & instruction_number < len(instruction_array)):
        instruction, string_number = instruction_array[instruction_number].split()
        signed_number = int(string_number)
        instruction_run_times[instruction_number] += 1
        if instruction_run_times[instruction_number] == 2:
            return -1
        else:
            if instruction == "acc":
                accumulator += signed_number
                instruction_number += 1
            if instruction == "jmp":
                instruction_number += signed_number
            if instruction == "nop":
                instruction_number += 1
    print("Finished while with no repeated instructions.")
    return accumulator


if __name__ == '__main__':
    print("Handheld halting")
    instruction_list = read_file()
    for x in range(0, len(instruction_list)):
        instruction_list_copy = instruction_list.copy()
        if instruction_list[x].split()[0] == "jmp":
            instruction_list_copy[x] = instruction_list_copy[x].replace("jmp", "nop")

        if instruction_list[x].split()[0] == "nop":
            instruction_list_copy[x] = instruction_list_copy[x].replace("nop", "jmp")
        acc = read_instructions(instruction_list_copy)
        if acc != -1:
            print("Accumulator value is {}".format(acc))
