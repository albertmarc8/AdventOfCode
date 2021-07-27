import sys
import re
from typing import *


def read_file_dict() -> List[dict]:
    passports = []
    passport = {}
    counter = 0
    for line in sys.stdin:
        if len(line) == 1:
            passports.append(passport)
            counter += 1
            passport = {}
        else:
            fields = line.rstrip().split(" ")
            for field in fields:
                split_field = field.split(":")
                passport.update({split_field[0]: split_field[1]})
    print("Read passports -> {}".format(counter))
    return passports


def check_passports_dict_simple(passports: List[dict]) -> int:
    valid_passports = 0
    required_fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
    for passport in passports:
        counter = 0
        for field in passport.keys():
            if field in required_fields:
                counter += 1

        if counter == len(required_fields):
            valid_passports += 1
        else:
            print("len: {} SKIPPED {}".format(len(passport.keys()), passport))
    return valid_passports


def check_passports_dict(passports: List[dict]) -> int:
    valid_passports = 0
    proccessed_passports = 0
    eyes_possibility = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}
    for passport in passports:
        proccessed_passports += 1

        # Birth year validation
        byr = passport.get("byr")
        if byr is None or 1920 < int(byr) > 2002:
            print("SKIPPED byr: {}".format(passport))
            continue

        # Issue year validation
        iyr = passport.get("iyr")
        if iyr is None or 2010 < int(iyr) > 2020 or int(byr) > int(iyr):
            print("SKIPPED iyr: {}".format(passport))
            continue

        # Expiration date validation
        eyr = passport.get("eyr")
        if eyr is None or 2020 < int(eyr) > 2030 or int(iyr) > int(eyr):
            print("SKIPPED eyr: {}".format(passport))
            continue

        # Height validation
        hgt = passport.get("hgt")
        if hgt is None or len(hgt) < 3:
            continue
        else:
            height_type = hgt[-2:]
            height_value = int(hgt[:-2])
            if height_type == "cm":
                if 150 < height_value > 193:
                    continue
            if height_type == "in":
                if 59 < height_value > 76:
                    continue

        # Hair color validation
        hcl = passport.get("hcl")
        if hcl is None or len(hcl) != 7:
            continue
        else:
            hcl_ok = re.search("#[a-f0-9]{6}", hcl)
            if not hcl_ok:
                continue

        # Eyes color validation
        ecl = passport.get("ecl")
        if ecl is None or ecl not in eyes_possibility:
            continue

        pid = passport.get("pid")
        if pid is None or len(pid) != 9:
            continue

        valid_passports += 1

    print("Processed passports -> {}".format(proccessed_passports))
    return valid_passports


if __name__ == '__main__':
    ok_passports = check_passports_dict_simple(read_file_dict())
    print("Passport Processing")
    print("Valid passports processed: {}".format(ok_passports))
