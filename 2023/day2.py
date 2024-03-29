"""

https://adventofcode.com/2023/day/2

Determine which games would have been possible if the bag had been loaded with only 12 red cubes, 13 green cubes, and 14 blue cubes. What is the sum of the IDs of those games

SAMPLE DATA
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
"""

def possible_ids(_line):    
    game,rounds = _line.split(":")
    
    text,game_id = game.strip().split()
    
    rounds_list = rounds.strip().split(";")
    if is_possible(rounds_list):
        print("round " + str(game_id) + " is possible")
        return game_id
    
    print("round " + str(game_id) + " is not possible")
    return 0    


def is_possible(_rounds_list):   
    i = 0
    rounds_length = len(_rounds_list)
    while i < rounds_length:
        current_round = _rounds_list[i]
        cubes = current_round.strip().split(",")
                
        j = 0
        cubes_length = len(cubes)
        while j < cubes_length:
            if is_over_max(cubes[j]):
                return False
            j += 1
        
        i += 1
    
    return True


def is_over_max(_cubes):
    red_max = 12
    green_max = 13
    blue_max = 14
    
    number,color = _cubes.strip().split()
        
    if color.strip() == "red":
        if int(number) > int(red_max):
            return True
    elif color.strip() == "green":
        if int(number) > int(green_max):
            return True
    elif color.strip() == "blue":
        if int(number) > int(blue_max):
            return True

    return False;
    

def get_game_power(_line):
    game,rounds = _line.split(":")
    
    text,game_id = game.strip().split()
    
    rounds_list = rounds.strip().split(";")
    power = get_round_power(rounds_list)
    
    print("round " + str(game_id) + " has a power of " + str(power))
    return power    


def get_round_power(_rounds_list):
    #[red,green,blue]
    powers = [0,0,0]

    i = 0
    rounds_length = len(_rounds_list)
    while i < rounds_length:
        current_round = _rounds_list[i]
        cubes = current_round.strip().split(",")
                
        j = 0
        cubes_length = len(cubes)
        while j < cubes_length:
            powers = get_cube_powers(cubes[j], powers)
            j += 1
        
        i += 1
    
    return multiple_powers(powers)


def get_cube_powers(_cubes, _powers):
    number,color = _cubes.strip().split()
        
    if color.strip() == "red":
        current_power = _powers[0]
        if int(number) > int(current_power):
            _powers[0] = number
    elif color.strip() == "green":
        current_power = _powers[1]
        if int(number) > int(current_power):
            _powers[1] = number
    elif color.strip() == "blue":
        current_power = _powers[2]
        if int(number) > int(current_power):
            _powers[2] = number

    return _powers

def multiple_powers(_powers):
    power = int(_powers[0])
    
    i = 1
    power_length = len(_powers)
    while i < power_length:
        power *= int(_powers[i])
        i += 1
        
    return power


if __name__ == "__main__":
    id_sum = 0
    power_sum = 0
    inputFile = "C:\\github\\Advent-Of-Code\\2023\\day2.txt"
    
    with open(inputFile) as fp:
        for line in fp:
            id_sum += int(possible_ids(line))
            power_sum += int(get_game_power(line))

    print()
    print('Total calibration: ' + str(id_sum))
    print('Total power: ' + str(power_sum))
    