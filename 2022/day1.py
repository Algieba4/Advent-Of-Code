'''


https://adventofcode.com/2022/day/1
'''

def compare_calories(_highest_calories, _elf_calories):
	_temp_array = []

	for _max_calories in _highest_calories:
		if int(_elf_calories) > int(_max_calories):
			_temp_array.append(_elf_calories)
			_elf_calories = int(_max_calories)
		else:
			_temp_array.append(_max_calories)
		
	return _temp_array
	
def get_calories(_highest_calories):
	_sum_calories = 0
	
	for _calories in _highest_calories:
		_sum_calories += int(_calories)
		
	return _sum_calories

if __name__ == "__main__":
	
	highest_calories = [0,0,0]
	elf_calories = 0;
	inputFile = "day1.txt"
	
	with open(inputFile) as fp:
		for line in fp:
			if line.strip():
				elf_calories += int(line)
			else:
				highest_calories = compare_calories(highest_calories, elf_calories)
				elf_calories = int(0)
	
	highest_calories = compare_calories(highest_calories, elf_calories)
	
	sum_calories = get_calories(highest_calories)
	
	print('The total calories between the highest three caloric elves are ' + str(sum_calories) + '.')
			