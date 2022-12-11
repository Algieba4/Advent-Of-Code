'''
RULES
- https://adventofcode.com/2022/day/10

OBJECTIVE
1. What is the sum of all signal strenghts
2. What eight capital letters appear on your CRT

TEST DATA
noop
addx 3
addx -5
'''

def get_signal_strength(x, cycle_count, signal_strengths):
	if cycle_count == 20 or (cycle_count - 20) % 40 == 0:
		signal_strength = int(cycle_count) * int(x)
		signal_strengths.append(signal_strength)
	return signal_strengths

def get_signal_strength_sum(signal_strengths):
	sum_signal_strength = 0
	for signal_strength in signal_strengths:
		sum_signal_strength += int(signal_strength)
	return sum_signal_strength

def move_sprite_position(value, sprite_position):
	sprite_position[0] = int(sprite_position[0]) + int(value)
	sprite_position[1] = int(sprite_position[1]) + int(value)
	sprite_position[2] = int(sprite_position[2]) + int(value)
	return sprite_position

def print_pixel_image(cycle_count, sprite_position, ctr_line):
	if cycle_count in sprite_position:
		ctr_line.append("#")
	else:
		ctr_line.append(".")
	return ctr_line

# Main method
if __name__ == "__main__":
	
	ctr_screen = []
	ctr_line = []
	inputFile = "day10.txt"
	signal_strengths = []
	sprite_position = [1,2,3]
	sum_signal_strength = 0
	x = 1
	cycle_count = 0
	
	with open(inputFile) as fp:
		for line in fp:
			cycle_count += 1
			ctr_line = print_pixel_image(cycle_count, sprite_position, ctr_line)
			if cycle_count % 40 == 0:
					ctr_screen.append(tuple(ctr_line))
					ctr_line = []
					cycle_count = 0
			if 'noop' in line:
				signal_strengths = get_signal_strength(x, cycle_count, signal_strengths)
			elif 'addx' in line:
				value = line.split()[1]
				signal_strengths = get_signal_strength(x, cycle_count, signal_strengths)
				cycle_count += 1
				ctr_line = print_pixel_image(cycle_count, sprite_position, ctr_line)
				if cycle_count % 40 == 0:
					ctr_screen.append(tuple(ctr_line))
					ctr_line = []
					cycle_count = 0
				signal_strengths = get_signal_strength(x, cycle_count, signal_strengths)
				x += int(value)
				sprite_position = move_sprite_position(value, sprite_position)
	
	print("Signal Strengths:" + str(signal_strengths))
	sum_signal_strength = get_signal_strength_sum(signal_strengths)
	print("Sum of Signal Strenths: " + str(sum_signal_strength))
	
	for line in ctr_screen:
		print(line)





