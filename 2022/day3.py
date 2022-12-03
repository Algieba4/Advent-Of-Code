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

def get_priority(compartment_one, compartment_two):
	for item in compartment_one:
		if item in compartment_two:
			print("Common Item: " + str(item))
			if(item.isupper()):
				priority = ((ord(item) - 64) + 26)
			else:
				priority = ord(item) - 96
			return priority
			
	return -1

if __name__ == "__main__":
	
	inputFile = "C:\\dev\\GitHub\\Advent-Of-Code\\2022\\day3.txt"
	sum_priority = 0
	
	with open(inputFile) as fp:
		for line in fp:
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
			
			priority = get_priority(compartment_one, compartment_two)
			print("Priority: " + str(priority))
			sum_priority += int(priority)
	
	print("sum of the priorities: " + str(sum_priority))
			