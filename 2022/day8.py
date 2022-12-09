'''
https://adventofcode.com/2022/day/8

OBJECTIVE
how many trees are visible from outside the grid?

TEST DATA
30373
25512
65332
33549
35390

'''

def count_visible_trees(tree_grove):
	
	# count outter trees
	rows = len(tree_grove)
	collumns = len(tree_grove[0])
	count = (int(collumns) * 2) + ((int(rows) - 2) * 2)
	print("perimeter count: " + str(count))
	
	print("rows:" + str(rows))
	print("collumns:" + str(collumns))
	row = 1
	collumn = 1
	
	# count inner visible trees
	while row < rows - 1:
		while collumn < collumns -1:
			if is_visible_down(tree_grove, row, collumn, range(int(row) + 1, rows)):
				# print("row " + str(row) + " collumn " + str(collumn) + " is visible from below")
				count += 1
			elif is_visible_left(tree_grove, row, collumn, range(0, collumn)):
				# print("row " + str(row) + " collumn " + str(collumn) + " is visible from left")
				count += 1
			elif is_visible_right(tree_grove, row, collumn, range(int(collumn) + 1, collumns)):
				# print("row " + str(row) + " collumn " + str(collumn) + " is visible from right")
				count += 1
			elif is_visible_up(tree_grove, row, collumn, range(0, row)):
				# print("row " + str(row) + " collumn " + str(collumn) + " is visible from up")
				count += 1
			collumn += 1
		row += 1
		collumn = 1
		
	return count

def print_tree_grove(tree_grove):
	for tree_row in tree_grove:
		for tree in tree_row:
			print(tree,end = " ")
		print()
		
def is_visible_down(tree_grove, row, collumn, range):
	for number in range:
		if tree_grove[row][collumn] <= tree_grove[number][collumn]:
			return False
	return True
	
def is_visible_left(tree_grove, row, collumn, range):
	for number in range:
		if tree_grove[row][collumn] <= tree_grove[row][number]:
			return False
	return True

def is_visible_right(tree_grove, row, collumn, range):
	for number in range:
		if tree_grove[row][collumn] <= tree_grove[row][number]:
			return False
	return True

def is_visible_up(tree_grove, row, collumn, range):
	for number in range:
		if tree_grove[row][collumn] <= tree_grove[number][collumn]:
			return False
	return True

if __name__ == "__main__":
	
	inputFile = "day8.txt"
	tree_grove = []
		
	with open(inputFile) as fp:
		index = 0
		for line in fp:
			tree_grove.insert(index, list(line.strip()))
			index += 1
		
	print_tree_grove(tree_grove)
	count = count_visible_trees(tree_grove)
	
	print("count of visible trees: " + str(count))
