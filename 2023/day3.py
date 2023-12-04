"""
https://adventofcode.com/2023/day/3

SAMPLE INPUT
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..

Expected Sum: 4361
"""


def get_line_array(_line):
    _array = []
    for ch in _line:
        _array.append(ch)
    return _array


def get_part_number_sum(_input_array, _row_count):
    _row_number = 0
    _column_number = 0
    _part_number = ""
    _part_number_sum = 0
    _valid_part_number = False

    for row in _input_array:
        row_length = len(row)
        for column in row:

            if column.isdigit():
                _part_number = _part_number + column
                if not _valid_part_number:
                    _valid_part_number = is_valid_part_number(_input_array, _row_number, _row_count, _column_number,
                                                              row_length)
            else:
                if _part_number and _valid_part_number:
                    _part_number_sum += int(_part_number)
                _part_number = ""
                _valid_part_number = False

            # added to ensure we are adding the previous digit if the row ends with a number.
            if int(_column_number) == (int(row_length) - 1):
                if _part_number and _valid_part_number:
                    _part_number_sum += int(_part_number)
                _part_number = ""
                _valid_part_number = False

            _column_number += 1

        _row_number += 1
        _column_number = 0
        _valid_part_number = False

    return _part_number_sum


def is_valid_part_number(_input_array, _row_number, _row_count, _column_number, _row_length):
    _character = ""

    # Checking the previous row
    if _row_number != 0:
        if _column_number != 0:
            _character = _input_array[_row_number - 1][_column_number - 1]
            if not _character.isdigit() and _character != ".":
                return True

        _character = _input_array[_row_number - 1][_column_number]
        if not _character.isdigit() and _character != ".":
            return True

        if _column_number != (_row_length - 1):
            _character = _input_array[_row_number - 1][_column_number + 1]
            if not _character.isdigit() and _character != ".":
                return True

    # Checking current row
    if _column_number != 0:
        _character = _input_array[_row_number][_column_number - 1]
        if not _character.isdigit() and _character != ".":
            return True

    if _column_number != (_row_length - 1):
        _character = _input_array[_row_number][_column_number + 1]
        if not _character.isdigit() and _character != ".":
            return True

    # Checking the next row
    if _row_number != (_row_count - 1):
        if _column_number != 0:
            _character = _input_array[_row_number + 1][_column_number - 1]
            if not _character.isdigit() and _character != ".":
                return True

        _character = _input_array[_row_number + 1][_column_number]
        if not _character.isdigit() and _character != ".":
            return True

        if _column_number != (_row_length - 1):
            _character = _input_array[_row_number + 1][_column_number + 1]
            if not _character.isdigit() and _character != ".":
                return True

    return False


if __name__ == "__main__":
    line_count = 0
    part_number_sum = 0
    input_array = []
    inputFile = "C:\\github\\Advent-Of-Code\\2023\\day3.txt"

    with open(inputFile) as fp:
        for line in fp:
            input_array.append(get_line_array(line.strip()))
            line_count += 1

    part_number_sum = get_part_number_sum(input_array, line_count)

    print('The sum of all part numbers in the engine schematic is: ' + str(part_number_sum))
