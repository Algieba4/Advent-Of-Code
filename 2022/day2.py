'''
https://adventofcode.com/2022/day/2

A = Rock
B = Paper
C = Scissors

Rock 		= 1 point
Paper 		= 2 points
Scissors 	= 3 points

X = Loose 	= 0 points
Y = Tie 	= 3 points
Z = Win		= 6 points

'''

wins = {
	'A': '2',
	'B': '3',
	'C': '1'
}

ties = {
	'A': '1',
	'B': '2',
	'C': '3'
}

loses = {
	'A': '3',
	'B': '1',
	'C': '2'
}

def get_score(them,me):

	score = 0
	
	if me == 'X':
		score = int(loses[them])
		print('Lost with a total score of ' + str(score))
		return score
	if me == 'Y':
		score = 3 + int(ties[them])
		print('Tied with a total score of ' + str(score))
		return score
	if me == 'Z':
		score = 6 + int(wins[them])
		print('Won with a total score of ' + str(score))
		return score

if __name__ == "__main__":
	
	inputFile = "day2.txt"
	total_score = 0
	
	with open(inputFile) as fp:
		for line in fp:
			them,me = line.split()
			score = get_score(them,me)
			total_score += int(score)
	
	print('Total Score: ' + str(total_score))