'''
https://adventofcode.com/2022/day/10

RULES
- noop == no change
- addx $value == increments or decrements X by $value
- Actions take place AFTER a cycle has finished
- noop takes 1 cycle to complete
- addx takes 2 cycles to complete
- Cycle starts at 1
- signal_strength is calculated DURING cycle
- signal_strength is X * cycle_count
- signal_strength occurs on cycle 20 and then every 40th

OBJECTIVE
1. What is the sum of all signal strenghts

TEST DATA
noop
addx 3
addx -5
'''

def get_signal_strength(x, cycle_count, signal_strengths):
	if cycle_count == 20 or (cycle_count - 20) % 40 == 0:
		signal_strength = int(cycle_count) * int(x)
		print("Singal Strength: " + str(signal_strength))
		signal_strengths.append(signal_strength)
	return signal_strengths

def get_signal_strength_sum(signal_strengths):
	sum_signal_strength = 0
	for signal_strength in signal_strengths:
		sum_signal_strength += int(signal_strength)
	return sum_signal_strength

# Main method
if __name__ == "__main__":
	
	inputFile = "day10.txt"
	signal_strengths = []
	sum_signal_strength = 0
	x = 1
	cycle_count = 0
	
	with open(inputFile) as fp:
		for line in fp:
			cycle_count += 1
			print("Cycle Count: " + str(cycle_count))
			if 'noop' in line:
				signal_strengths = get_signal_strength(x, cycle_count, signal_strengths)
			elif 'addx' in line:
				value = line.split()[1]
				signal_strengths = get_signal_strength(x, cycle_count, signal_strengths)
				cycle_count += 1
				print("Cycle Count: " + str(cycle_count))
				signal_strengths = get_signal_strength(x, cycle_count, signal_strengths)
				x += int(value)
				print("x: " + str(x))
	
	print("Signal Strengths:" + str(signal_strengths))
	sum_signal_strength = get_signal_strength_sum(signal_strengths)
	print("Sum of Signal Strenths: " + str(sum_signal_strength))





