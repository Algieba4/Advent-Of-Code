'''
https://adventofcode.com/2022/day/2

A = Rock
B = Paper
C = Scissors

X = Rock		= 1 point
Y = Paper		= 2 points
Z = Scissors	= 3 points

Loose 	= 0 points
Tie 	= 3 points
Win		= 6 points

'''

loses_to = {
	'X': 'C',
	'Y': 'A',
	'Z': 'B'
}

ties = {
	'X': 'A',
	'Y': 'B',
	'Z': 'C'
}

def get_score(them,me):

	score = 0
	
	if me == 'X':
		score = 1
	if me == 'Y':
		score = 2
	if me == 'Z':
		score = 3

	if them == loses_to[me]:
		score += 6
		print('Won with a total score of ' + str(score))
		return score
	elif them == ties[me]:
		score += 3
		print('Tied with a total score of ' + str(score))
		return score
	else:
		print('Lost with a total score of ' + str(score))
		return score
		
	return -1

if __name__ == "__main__":
	
	inputFile = "C:\\dev\\GitHub\\Advent-Of-Code\\2022\\day2.txt"
	total_score = 0
	
	with open(inputFile) as fp:
		for line in fp:
			them,me = line.split()
			score = get_score(them,me)
			total_score += int(score)
	
	print('Total Score: ' + str(total_score))