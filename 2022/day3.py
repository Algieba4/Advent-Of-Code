'''
https://adventofcode.com/2022/day/3

- Rucksacks have two compartments of the same size
- Find the (1) letter existing in both compartments
- Find the priority of each letter
	- a-z = 1-26
	- A-Z = 27 = 52
Find the sum of of all common letters

TEST DATA
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
'''	

def get_badge_common_item(rucksack_group):
	rucksack_one = rucksack_group.pop()
	rucksack_two = rucksack_group.pop()
	rucksack_thre = rucksack_group.pop()
	
	for item in rucksack_one:
		if item in rucksack_two:
			if item in rucksack_thre:
				return item

def get_badge_priority(rucksack_group):

	item = get_badge_common_item(rucksack_group)
	priority = 0
	
	if(item.isupper()):
		priority = ((ord(item) - 64) + 26)
	else:
		priority = ord(item) - 96
	
	print("Common Group Item: " + str(item) + " ; Priority: " + str(priority))
	print()
	return priority

def get_rucksack_common_item(compartment_one, compartment_two):
	for item in compartment_one:
		if item in compartment_two:
			return item

def get_rucksack_priority(compartment_one, compartment_two):

	item = get_rucksack_common_item(compartment_one, compartment_two)
	priority = 0
	
	if(item.isupper()):
		priority = ((ord(item) - 64) + 26)
	else:
		priority = ord(item) - 96
	
	print("Common Item: " + str(item) + " ; Priority: " + str(priority))
	return priority

if __name__ == "__main__":
	
	inputFile = "C:\\dev\\GitHub\\Advent-Of-Code\\2022\\day3.txt"
	sum_group_priority = 0
	sum_priority = 0
	
	with open(inputFile) as fp:
		count = 0
		rucksack_group = []
		for line in fp:
			count += 1
			rucksack = list(line.strip())
			rucksack_size = len(rucksack)
			rucksack_first_half = rucksack_size / 2
			
			i = 0
			compartment_one = []
			while i < rucksack_first_half:
				compartment_one.append(rucksack[i])
				i = i + 1
			
			compartment_two = []
			while i < rucksack_size:
				compartment_two.append(rucksack[i])
				i = i + 1
			
			priority = get_rucksack_priority(compartment_one, compartment_two)
			sum_priority += int(priority)
			
			rucksack_group.append(rucksack)
			if(count == 3):
				group_priority = get_badge_priority(rucksack_group)
				sum_group_priority += int(group_priority)
				count = 0
				rucksack_group = []
	
	print("Sum of the rucksack priorities: " + str(sum_priority))
	print("Sum of the group priorities: " + str(sum_group_priority))
			