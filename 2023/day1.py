"""

https://adventofcode.com/2023/day/1

SAMPLE DATA
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
"""

numbers = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}


def get_calibration(_line):
    first_digit = 0
    last_digit = 0
    calibration = 0

    first_digit = get_digit(_line, True)
    last_digit = get_digit(_line, False)

    calibration = (int(first_digit) * 10) + int(last_digit)
    print('Line calibration: ' + str(calibration))

    return calibration


def get_digit(_line_array, is_first):
    array_three = []
    array_four = []
    array_five = []
    digit = 0

    calibration_array = list(_line_array.strip())
    calibration_size = len(calibration_array)

    i = 0
    while i < calibration_size:
        array_three, array_four, array_five = update_arrays(array_three, array_four, array_five, calibration_array[i])
        if calibration_array[i].isdigit():
            digit = calibration_array[i]
            if is_first:
                return digit
            else:
                i = i + 1
        elif list_to_string(array_three) in numbers:
            digit = numbers[list_to_string(array_three)]
            if is_first:
                return digit
            else:
                i = i + 1
        elif list_to_string(array_four) in numbers:
            digit = numbers[list_to_string(array_four)]
            if is_first:
                return digit
            else:
                i = i + 1
        elif list_to_string(array_five) in numbers:
            digit = numbers[list_to_string(array_five)]
            if is_first:
                return digit
            else:
                i = i + 1
        else:
            i = i + 1

    return digit


def update_arrays(_array_three, _array_four, _array_five, value):

    if len(_array_three) == 3:
        _array_three.pop(0)
    _array_three.append(value)

    if len(_array_four) == 4:
        _array_four.pop(0)
    _array_four.append(value)

    if len(_array_five) == 5:
        _array_five.pop(0)
    _array_five.append(value)

    return _array_three, _array_four, _array_five


def list_to_string(_array):
    list_string = ""
    for x in _array:
        list_string += x
    return list_string


if __name__ == "__main__":
    calibration_sum = 0
    inputFile = "C:\\github\\Advent-Of-Code\\2023\\day1.txt"

    with open(inputFile) as fp:
        for line in fp:
            calibration_sum += int(get_calibration(line))

    print('Total calibration: ' + str(calibration_sum))
