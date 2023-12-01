"""

https://adventofcode.com/2023/day/1

SAMPLE DATA
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
"""


def get_calibration(_line):
    first_digit = 0
    last_digit = 0
    calibration = 0

    first_digit = get_digit(_line)

    _line_reverse = _line[::-1]
    last_digit = get_digit(_line_reverse)

    calibration = (int(first_digit) * 10) + int(last_digit)
    print('Line calibration: ' + str(calibration))

    return calibration


def get_digit(_line_array):
    calibration_array = list(_line_array.strip())
    calibration_size = len(calibration_array)

    i = 0
    while i < calibration_size:
        if calibration_array[i].isdigit():
            return calibration_array[i]
        else:
            i = i + 1

    return 0


if __name__ == "__main__":
    calibration_sum = 0
    inputFile = "C:\\github\\Advent-Of-Code\\2023\\day1.txt"

    with open(inputFile) as fp:
        for line in fp:
            calibration_sum += int(get_calibration(line))

    print('Total calibration: ' + str(calibration_sum))
