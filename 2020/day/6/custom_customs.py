import sys


def read_file3():
    # correct answer given: 3125
    return sum(len(set.intersection(*map(set, entry.split()))) for entry in open("input.txt").read().split("\n\n"))


def read_file() -> int:
    answers_sum = 0
    answers = dict()

    for line in sys.stdin:
        if line.isspace():
            print("newline appears")
            answers = {}
            different_answers = 0
        else:
            print(line.rstrip())
            different_answers = 0
            for character in line:
                if not character.isspace():
                    if character in answers:
                        print(f"{character} -> found it already")
                    else:
                        answers.setdefault(character)
                        print(f"\t{character} NEW")
                        different_answers += 1
            print(f"Adding {different_answers} to {answers_sum}")
            answers_sum += different_answers

    return answers_sum


def read_file2() -> int:
    # FIXME
    counter = 0
    my_set = set()

    for line in sys.stdin:
        line = line.rstrip()
        if len(line) < 1:
            # reset sets
            print(f"I add {len(my_set)} to {counter} ")
            counter += len(my_set)
            my_set = set()
        else:
            temp_set = set()
            for character in line:
                temp_set.add(character)
            if len(my_set) == 0:
                my_set = my_set.union(temp_set)
            else:
                my_set = my_set.intersection(temp_set)
    # 3125
    counter += len(my_set)
    print(f"I add {len(my_set)} to {counter} ")

    return counter


if __name__ == '__main__':
    print("Custom customs")
    print(read_file2())
