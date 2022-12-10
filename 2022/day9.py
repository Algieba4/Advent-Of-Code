'''
https://adventofcode.com/2022/day/9

RULES
- There is a head (H) and tail (T)
- H and T start in the same location
- H moves as according to the test data
- H and T must always touch each other (diaganal counts)
- If H is touching T, T does not move
- If H stops touching T, T should move to touch H
- If H is two moves away, T can move diagonally, else not.

OBJECTIVE
1. How many positions does the tail of the rope visit at least once?
2. 

TEST DATA
R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2

It's lower than 8,070

Note for future: make the entire thing one array of arrays.
'''

# Checks to see if two knots are touching
# head = knot just ahead of the current knot
# tail = current knot 
def is_touching(head, tail):
	if is_touching_neighbors(head, tail):
		return True
	if is_touching_diagonally(head, tail):
		return True
	return False

# Checks to see if two knots are touching horizontally or vertially
# head = knot just ahead of the current knot
# tail = current knot
# Index 0 = X-axis
# Index 1 = Y-axis
def is_touching_neighbors(head, tail):
	if int(tail[0]) == int(head[0]) and int(tail[1]) == int(head[1]):
		return True
	if int(tail[0]) == int(head[0]) and ((int(tail[1]) + 1) == int(head[1]) or (int(tail[1]) - 1) == int(head[1])):
		return True
	if int(tail[1]) == int(head[1]) and ((int(tail[0]) + 1) == int(head[0]) or (int(tail[0]) - 1) == int(head[0])):
		return True
		
	return False

# Checks to see if two knots are touching diagonally
# head = knot just ahead of the current knot
# tail = current knot 
# Index 0 = X-axis
# Index 1 = Y-axis
def is_touching_diagonally(head, tail):
	# top-left diagonal
	if (int(tail[1]) + 1) == int(head[1]) and (int(tail[0]) - 1) == int(head[0]):
		return True
	
	# bottom-left diagonal
	if (int(tail[1]) - 1) == int(head[1]) and (int(tail[0]) - 1) == int(head[0]):
		return True
	
	# top-right diagonal
	if (int(tail[1]) + 1) == int(head[1]) and (int(tail[0]) + 1) == int(head[0]):
		return True
	
	# bottom-right diagonal
	if (int(tail[1]) - 1) == int(head[1]) and (int(tail[0]) + 1) == int(head[0]):
		return True
	
	return False

# Method to move the head knot
def move_head(head, direction):
	x = head[0]
	y = head[1]
	
	if direction == 'D':
		head[1] -= 1 
	if direction == 'L':
		head[0] -= 1
	if direction == 'R':
		head[0] += 1
	if direction == 'U':
		head[1] += 1
	
	return head

# Method to move a knot, if necessary
# head = knot just ahead of the current knot
# tail = current knot
# Index 0 = X-axis
# Index 1 = Y-axis
def move_tail(head, tail, direction):
	
	if is_touching(head,tail):
		return tail
	
	# Move tail up
	if int(tail[0]) == int(head[0]) and (int(tail[1]) + 2) == int(head[1]):
		tail[1] += 1
		return tail
	
	# Move tail down
	if int(tail[0]) == int(head[0]) and (int(tail[1]) - 2) == int(head[1]):
		tail[1] -= 1
		return tail
	
	# Move tail Right
	if int(tail[1]) == int(head[1]) and (int(tail[0]) + 2) == int(head[0]):
		tail[0] += 1
		return tail
	
	# Move tail Left
	if int(tail[1]) == int(head[1]) and (int(tail[0]) - 2) == int(head[0]):
		tail[0] -= 1
		return tail
	
	tail = move_tail_diaganally(head, tail, direction)
	
	return tail

# Method to move a knot diaganally 
# head = knot just ahead of the current knot
# tail = current knot
# Index 0 = X-axis
# Index 1 = Y-axis
def move_tail_diaganally(head, tail, direction):

	if direction == 'D':
		tail[1] -= 1 
		
		# bottom-left diagonal
		if (int(tail[1]) - 1) == int(head[1]) and (int(tail[0]) - 1) == int(head[0]):
			tail[0] -= 1
		else:
			tail[0] += 1
		
	if direction == 'L':
		tail[0] -= 1
		
		# top-left diagonal
		if (int(tail[1]) + 1) == int(head[1]) and (int(tail[0]) - 1) == int(head[0]):
			tail[1] += 1
		else:
			tail[1] -= 1
		
		
	if direction == 'R':
		tail[0] += 1
		
		# top-right diagonal
		if (int(tail[1]) + 1) == int(head[1]) and (int(tail[0]) + 1) == int(head[0]):
			tail[1] += 1
		else:
			tail[1] -= 1
		
		
	if direction == 'U':
		tail[1] += 1
		
		# top-left diagonal
		if (int(tail[1]) + 1) == int(head[1]) and (int(tail[0]) - 1) == int(head[0]):
			tail[0] -= 1
		else:
			tail[0] += 1
		
	return tail

# Main method
if __name__ == "__main__":
	
	inputFile = "day9.txt"
	unique_movements = set()
	knots = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
	unique_movements.add(tuple(knots[len(knots)-1])) # By default, tail will be in position [0,0]
	print("Movements: " + str(knots)) # Print initial body placement for debug
	
	with open(inputFile) as fp:
		for line in fp:
			direction,amount = line.split()
			range_amount = range(int(amount)) # range is 0 to amount - 1		
			for number in range_amount:
				knots[0] = move_head(knots[0], direction) # Move knot head
				i = 1 # Move rest of the knots
				while i < len(knots):
					knots[i] = move_tail(knots[int(i) - 1], knots[i], direction)
					if i == len(knots)-1: # Track unique locations of the knot tail
						unique_movements.add(tuple(knots[i]))	
					i += 1 # Progress through body knots
				print("Movements: " + str(knots)) # Print movements for debug
	print("Total unique movements: " + str(len(unique_movements))) # Print Solution answer
