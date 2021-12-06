'''
The purpose of this script is to complete the day-2 Advent of Code challange
It will read from an input file and output the number of times a number is larger than the prior number
https://adventofcode.com/2021/day/2

Author: Travis Ottelien
'''	

if __name__ == "__main__":

	aim = 0
	horizontal = 0
	depth = 0
	inputFile = "C:\\dev\\GitHub\\Advent-Of-Code\\2021\\day2.txt"
	
	with open(inputFile) as fp:
		for line in fp:
			direction,amount = line.split(' ')
			match direction:
				case "down":
					aim = int(aim) + int(amount)
				case "forward":
					horizontal = int(horizontal) + int(amount)
					depth = int(depth) + (int(aim) * int(amount))
				case "up":
					aim = int(aim) - int(amount)
			
	print('Final Aim: ' + str(aim))
	print('Final Horizontal position: ' + str(horizontal))
	print('Final Depth: ' + str(depth))
	
	finalPosition = int(horizontal) * int(depth)
	print('Multipied final posistion: ' + str(finalPosition))