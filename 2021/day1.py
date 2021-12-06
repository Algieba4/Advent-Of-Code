'''
The purpose of this script is to complete the day-1 Advent of Code challange
It will read from an input file and output the number of times a number is larger than the prior number
https://adventofcode.com/2021/day/1

Author: Travis Ottelien
'''	

if __name__ == "__main__":

	count = 0
	firstLine = "True"
	inputFile = "C:\\dev\\GitHub\\Advent-Of-Code\\2021\\day1.txt"
		
	with open(inputFile) as fp:
		for line in fp:
			if(bool(firstLine)):
				currentLine = line
				firstLine = ""
			else:
				currentLine = line
				if(int(currentLine) > int(previousLine)):
					count = count + 1
			previousLine = currentLine
	
	print('There are ' + str(count) + ' measurements that are larger than the previous measurement.')
						