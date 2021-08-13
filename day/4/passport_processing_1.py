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
    # FIXME the last passport has no new line, therefore it is not added. Is there a better way to finish this?
    passports.append(passport)
    counter += 1
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
            print("req_fields: {} --> len: {} SKIPPED {}".format(len(required_fields), counter, passport))
    return valid_passports


def check_passports_dict(passports: List[dict]) -> int:
    valid_passports = 0
    proccessed_passports = 0
    eyes_possibility = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}
    for passport in passports:
        proccessed_passports += 1

        # Birth year validation
        byr = passport.get("byr")
        if byr is None:
            continue
        else:
            byr = int(byr)
            if (len(str(byr)) != 4) | ((byr < 1920) | (byr > 2002)):
                #print("SKIPPED byr: {}".format(byr))
                continue

        # Issue year validation
        iyr = passport.get("iyr")
        if iyr is None:
            continue
        else:
            iyr = int(iyr)
            if (len(str(iyr)) != 4) | ((iyr > 2020) | (iyr < 2010)):
                #print("SKIPPED iyr: {}".format(iyr))
                continue

        # Expiration date validation
        eyr = passport.get("eyr")
        if eyr is None:
            continue
        else:
            eyr = int(eyr)
            if (len(str(eyr)) != 4) | (eyr > 2030) | (eyr < 2020):
                #print("SKIPPED eyr: {}".format(eyr))
                continue

        # Height validation
        hgt = passport.get("hgt")
        if hgt is None:
            continue
        else:
            if len(hgt) < 4:
                #print("SKIPPED hgt: {}".format(hgt))
                continue
            else:
                height_type = hgt[-2:]
                height_value = int(hgt[:-2])
                if height_type == "cm":
                    if not (150 <= height_value <= 193):
                        #print("SKIPPED hgt cm: {}".format(hgt))
                        continue
                elif height_type == "in":
                    if not (59 <= height_value <= 76):
                        #print("SKIPPED hgt in: {}".format(hgt))
                        continue
                else:
                    #print("SKIPPED hgt other: {}".format(hgt))
                    continue

        # Hair color validation
        hcl = passport.get("hcl")
        if hcl is None:
            continue
        else:
            if len(hcl) != 7:
                #print("SKIPPED hcl: {}".format(hcl))
                continue
            else:
                hcl_ok = re.search("#[a-f0-9]{6}", hcl)
                if not hcl_ok:
                    #print("SKIPPED hcl: {}".format(hcl))
                    continue

        # Eyes color validation
        ecl = passport.get("ecl")
        if ecl is None:
            continue
        else:
            if ecl not in eyes_possibility:
                print("SKIPPED ecl: {}".format(ecl))
                continue

        pid = passport.get("pid")
        if pid is None:
            continue
        else:
            if len(pid) != 9:
                print("SKIPPED pid: {}".format(pid))
                continue
            else:
                pid_ok = re.search("[0-9]{9}", pid)
                if not pid_ok:
                    continue

        valid_passports += 1

    print("Processed passports -> {}".format(proccessed_passports))
    return valid_passports


if __name__ == '__main__':
    #ok_passports = check_passports_dict_simple(read_file_dict())
    print("Passport Processing")
    #print("Valid passports processed: {}".format(ok_passports))
    ok_passports = check_passports_dict(read_file_dict())
    # 158 too high
    # 154 too low
    print("Valid passports processed: {}".format(ok_passports))
