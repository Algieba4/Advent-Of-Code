'''
RULES
- https://adventofcode.com/2022/day/11

OBJECTIVE
1. What is the sum of all signal strenghts
2. What eight capital letters appear on your CRT

TEST DATA
noop
addx 3
addx -5
'''

class Monkey:
	index = 0
	items = []
	operation = ""
	operation_value = 0
	test_value = 0
	true_case = 0
	false_case = 0
	inspection_count = 0
	
	def __init__(self, index, items):
		 self.index = index
		 self.items = items
	
	def get_index(self):
		return self.index
	
	def get_items(self):
		return self.items
	
	def get_operation(self):
		return self.operation
		
	def get_operation_value(self):
		return self.operation_value
		
	def get_test_value(self):
		return self.test_value
		
	def get_true_case(self):
		return self.true_case
		
	def get_false_case(self):
		return self.false_case
		
	def get_inspection_count(self):
		return self.inspection_count
	
	def set_items(self, items):
		self.items = items
	
	def set_operation(self, operation):
		self.operation = operation
		
	def set_operation_value(self, operation_value):
		self.operation_value = operation_value
		
	def set_test_value(self, test_value):
		self.test_value = test_value
		
	def set_true_case(self, true_case):
		self.true_case = true_case
	
	def set_false_case(self, false_case):
		self.false_case = false_case
		
	def set_inspection_count(self, inspection_count):
		self.inspection_count = inspection_count

def get_new_value(item, operation, operation_value):
	tmp_value = 0
	value = 0
	
	match operation_value:
		case "old":
			value = int(item)
		case _:
			value = int(operation_value)
	
	match operation:
		case "*":
			tmp_value = int(item) * value
		case "+":
			tmp_value = int(item) + value
		case "-":
			tmp_value = int(item) - value
		case "/":
			tmp_value = int(item) / value
	
	new_value = int(tmp_value) // 3 # // performs division and skips the remainder
	
	return new_value

def initialize_monkeys(input_file):
	monkey_index = 0
	monkeys = []
	
	for line in fp:
		if 'Starting items' in line:
			items = []
			lines = line.split()
			i = 2
			while i < len(lines):
				items.append(lines[i].replace(",",""))
				i += 1
			monkey = Monkey(str(monkey_index),items)
			monkeys.append(monkey)
		elif 'Operation' in line:
			lines = line.split()
			monkey = monkeys[int(monkey_index)]
			monkey.set_operation(lines[4])
			monkey.set_operation_value(lines[5])
			monkeys[int(monkey_index)] = monkey
		elif 'Test' in line:
			lines = line.split()
			monkey = monkeys[int(monkey_index)]
			monkey.set_test_value(lines[3])
			monkeys[int(monkey_index)] = monkey
		elif 'true' in line:
			lines = line.split()
			monkey = monkeys[int(monkey_index)]
			monkey.set_true_case(lines[5])
			monkeys[int(monkey_index)] = monkey
		elif 'false' in line:
			lines = line.split()
			monkey = monkeys[int(monkey_index)]
			monkey.set_false_case(lines[5])
			monkeys[int(monkey_index)] = monkey
		elif 'Monkey' in line:
			lines = line.split()
			monkey_index = lines[1].replace(":","")
	
	return monkeys
	
def is_worried(new_value, worried_level):
	if int(new_value) % int(worried_level) == 0:
		return True
	return False

# Something is wrong with this function.
def move_items(monkeys, monkey, index):
	items = monkey.get_items()
	operation = monkey.get_operation()
	operation_value = monkey.get_operation_value()
	for item in items:
		inspection_count = monkeys[int(index)].get_inspection_count()
		inspection_count += 1
		monkeys[int(index)].set_inspection_count(inspection_count)
		new_value = get_new_value(item, operation, operation_value)
		if is_worried(new_value, monkey.get_test_value()):
			print("Monkey " + str(index) + " sends value " + str(new_value) + " to " + str(monkey.get_test_value()))
			new_monkey_items = monkeys[int(monkey.get_true_case())].get_items()
			new_monkey_items.append(new_value)
			monkeys[int(monkey.get_true_case())].set_items(new_monkey_items)
		else:
			print("Monkey " + str(index) + " sends value " + str(new_value) + " to " + str(monkey.get_false_case()))
			new_monkey_items = monkeys[int(monkey.get_false_case())].get_items()
			new_monkey_items.append(new_value)
			monkeys[int(monkey.get_false_case())].set_items(new_monkey_items)
	
	monkeys[int(index)].set_items([])
	return monkeys		

def print_monkey_details(monkeys):
	print()
	for monkey in monkeys:
		print("Monkey: " + str(monkey.get_index()))
		print("Items: " + str(monkey.get_items()))
		print("Operation: " + str(monkey.get_operation()))
		print("Operation Value: " + str(monkey.get_operation_value()))
		print("Test Value: " + str(monkey.get_test_value()))
		print("True Case: " + str(monkey.get_true_case()))
		print("False Case: " + str(monkey.get_false_case()))
		print()
	print()

def print_monkey_inspection_count(monkeys):
	print()
	for monkey in monkeys:
		print("Monkey " + str(monkey.get_index()) + ": " + str(monkey.get_inspection_count()))
	print()
	
def print_monkey_items(monkeys):
	print()
	for monkey in monkeys:
		print("Monkey " + str(monkey.get_index()) + ": " + str(monkey.get_items()))
	print()

# Main method
if __name__ == "__main__":
	
	input_file = "day11.txt"
	monkeys = []
	round = 0
	
	with open(input_file) as fp:
		monkeys = initialize_monkeys(input_file)
	
	print_monkey_details(monkeys)
	round += 1 # Start rounds
	while int(round) < 21:
		print("Starting round " + str(round))
		print_monkey_items(monkeys)
		for index,monkey in enumerate(monkeys):
			monkeys = move_items(monkeys, monkey, index)
			print_monkey_items(monkeys)
		round += 1 # Start next round
	
	print_monkey_inspection_count(monkeys)
	
	highest_count = 0
	second_highest_count = 0
	for monkey in monkeys:
		inspection_count = monkey.get_inspection_count()
		if int(inspection_count) > int(highest_count):
			second_highest_count = int(highest_count)
			highest_count = int(inspection_count)
		elif int(inspection_count) > int(second_highest_count):
			second_highest_count = int(inspection_count)
			
	monkey_business = int(highest_count) * int(second_highest_count)
	print("Monkey Business: " + str(monkey_business))