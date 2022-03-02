import sys


def read_file():
    number_array = []
    for line in sys.stdin:
        number_array.append(int(line.rstrip()))
    return number_array


def find_weak_point(arr, preamble):
    i = preamble
    while i < len(arr):
        min = i - preamble
        if min < 0:
            min = 0
        found = False
        for j in range(min, i):
            for k in range (min, i):
                if j != k:
                    suma = arr[j] + arr[k]
                    if suma == arr[i]:
                        found = True
                        #print("MATCH! La suma de {} y {} es {}".format(arr[j], arr[k], suma))
                    #print("La suma de {} y {} no es {}".format(arr[j], arr[k], suma))
        if not found:
            return arr[i]
        i += 1


def find_contiguous_sum(arr, number):
    i = 0
    while i < len(arr):
        j = i + 1
        sumatorio = arr[i]
        min = sys.maxsize
        max = 0
        while j < len(arr):
            sumatorio += arr[j]
            if min > arr[j]:
                min = arr[j]

            if max < arr[j]:
                max = arr[j]

            if sumatorio > number:
                break
            if sumatorio == number:
                print("Found match. From i = {} to j {} it sums {}".format(i, j, sumatorio))
                print("min's value is {} and max's value is {}".format(min, max))
                suma_min_max = min + max
                print("The sum of these previous numbers is {}".format(suma_min_max))
                return
            j += 1
        i += 1


if __name__ == '__main__':
    arr = read_file()
    print("Encoding error")
    weak_number = find_weak_point(arr, 25)
    find_contiguous_sum(arr, weak_number)
