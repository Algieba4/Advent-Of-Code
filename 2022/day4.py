'''
https://adventofcode.com/2022/day/4


TEST DATA
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
'''

def is_overlapping(range_one,range_two):
	range_one_min,range_one_max = range_one.split("-")
	range_two_min,range_two_max = range_two.split("-")
	
	# First number is the staring point
	# Second number is the stopping point, not max, why is why +1 is added.
	_range_one = range(int(range_one_min), int(range_one_max)+1)
	_range_two = range(int(range_two_min), int(range_two_max)+1)
	
	for number in _range_one:
		print("range-1 number: " + str(number))
		if number in _range_two:
			return True
		
	return False

def is_fully_contained(range_one,range_two):
	range_one_min,range_one_max = range_one.split("-")
	range_two_min,range_two_max = range_two.split("-")
	
	if (int(range_one_min) >= int(range_two_min)) and (int(range_one_max) <= int(range_two_max)):
		return True
	
	if (int(range_two_min) >= int(range_one_min)) and (int(range_two_max) <= int(range_one_max)):
		return True
		
	return False

if __name__ == "__main__":
	
	inputFile = "day4.txt"
	count_contained = 0
	count_overlapped = 0
	
	with open(inputFile) as fp:
		count = 0
		rucksack_group = []
		for line in fp:
			range_one,range_two = line.split(",")
			if(is_fully_contained(range_one,range_two)):
				count_contained += 1
			if(is_overlapping(range_one,range_two)):
				count_overlapped += 1
	
	print(str(count_contained) + " assingment pairs have fully contained ranges.")
	print(str(count_overlapped) + " assingment pairs overlap.")