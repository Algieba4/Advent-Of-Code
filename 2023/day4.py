"""
https://adventofcode.com/2023/day/4

left-side: winning numbers
right-side: "my" numbers

SAMPLE INPUT
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
"""


def get_winning_points(_line):
    points = 0

    card, lines = _line.strip().split(":")
    winning_numbers, my_numbers = lines.strip().split("|")

    my_list = my_numbers.strip().split()
    winning_list = winning_numbers.strip().split()

    for number in my_list:
        if number in winning_list:
            if points == 0:
                points += 1
            else:
                points *= 2

    return points


if __name__ == "__main__":
    inputFile = "C:\\github\\Advent-Of-Code\\2023\\day4.txt"
    points_sum = 0

    with(open(inputFile)) as input_file:
        for line in input_file:
            points_sum += int(get_winning_points(line))

    print("Total Points: " + str(points_sum))
