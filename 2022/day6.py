'''
https://adventofcode.com/2022/day/6

OBJECTIVE
For each line, find the point in which
four consecutive characters are different.
Count the total characters up to that point

E.G
mjqjpqmgbljsphdztnvjfqwrcgsmlb
First instance of four unique characters: jpqm
Completed after (comparing) 7 characters: mjqjpqm

How many characters need to be processed before 
the first start-of-packet marker is detected?

TEST DATA
mjqjpqmgbljsphdztnvjfqwrcgsmlb
bvwbjplbgvbhsrlpgdmjqwftvncz
nppdvjthqldpwncqszvftbrmjlhg
nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg
zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw

EDIT: learned something new about set() today
'''

def get_packet_marker(datastream, unique_count):
	
	packet_marker = set()
	for count, value in enumerate(datastream):
		counter = 0
		index = int(count)
		while counter < unique_count:
			index += 1
			packet_marker.add(datastream[int(index)])
			counter += 1
		counter = 0
		if(len(packet_marker)) == unique_count:
			return str(index + 1)
		packet_marker.clear()
	

if __name__ == "__main__":
	
	inputFile = "day6.txt"
		
	with open(inputFile) as fp:
		for line in fp:
			marker = get_packet_marker(list(line.strip()), 4)
			messages = get_packet_marker(list(line.strip()), 14)
			
			print(str(marker) + " characters were processed to find marker")
			print(str(messages) + " characters were processed to find messages")
			print()

