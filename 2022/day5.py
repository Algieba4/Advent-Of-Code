'''
https://adventofcode.com/2022/day/5

OBJECTIVE
After the rearrangement procedure completes, 
what crate ends up on top of each stack

TEST DATA
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
'''

def get_container_info(line, queue_info):

	space_count = 0
	queue_count = 0
	line_info = list(line)
		
	for char_list in line_info:
		if char_list == ' ':
			space_count += int(1)
		if char_list.isupper():
			queue_info[queue_count-1].append(char_list)
		if char_list == '[':
			queue_count += 1
			while space_count >= int(4):
				queue_count += int(1)
				space_count -= int(4)			
			space_count = 0
			
	return queue_info

def move_containers(line, queue_info):
	container_movement = line.split()
	
	num_move = container_movement[1]
	from_container = container_movement[3]
	to_container = container_movement[5]
	
	print("move " + str(num_move) + " from " + str(from_container) + " to " + str(to_container))
	
	i = 0
	while i < int(num_move):
		char_move = queue_info[int(from_container)-1].pop(0)
		queue_info[int(to_container)-1].insert(0,str(char_move))
		i += 1
	
	return queue_info

if __name__ == "__main__":
	
	inputFile = "day5.txt"
	queue_info = [[],[],[],[],[],[],[],[],[]]
		
	with open(inputFile) as fp:
		for line in fp:
			if '[' in line:
				queue_info = get_container_info(line, queue_info)
				print(queue_info)
			elif 'move' in line:
				queue_info = move_containers(line, queue_info)
				print(queue_info)

	i = 0
	top_characters = ""
	while(i < len(queue_info)):
		top_characters += str(queue_info[i].pop(0))
		i += 1
	
	print("the top crate characters are " + str(top_characters))
