'''
The purpose of this script is to complete the day-1 Advent of Code challange
It will read from an input file and output the number of times a number is larger than the prior number
https://adventofcode.com/2021/day/1

Author: Travis Ottelien
'''	

if __name__ == "__main__":

	arrayCount = 0
	count = 0
	depths = []
	firstLine = "True"
	inputFile = "C:\\dev\\GitHub\\Advent-Of-Code\\2021\\day1.txt"
		
	with open(inputFile) as fp:
	
		for line in fp:
			
			if len(depths) > int(0):
				currentLine = line
				if int(currentLine) > int(previousLine):
					count = count + 1
			else:
				currentLine = line
		
			if len(depths) < int(3):
				depths.append(line)
			else:
				previousArrayCount = int(depths[0]) + int(depths[1]) + int(depths[2])
				depths.pop(0)
				depths.append(line)
				currentArrayCount = int(depths[0]) + int(depths[1]) + int(depths[2])
				if int(currentArrayCount) > int(previousArrayCount):
					arrayCount = arrayCount + 1

			previousLine = currentLine
	
	print('There are ' + str(count) + ' measurements that are larger than the previous measurement.')
	print('There are ' + str(arrayCount) + ' sums that are larger than the previous sum')
						