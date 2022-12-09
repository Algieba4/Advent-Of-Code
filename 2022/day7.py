'''
https://adventofcode.com/2022/day/7

OBJECTIVE
Find all of the directories with a 
total size of at most 100000. 
What is the sum of the total sizes 
of those directories?

TEST DATA
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k

It's lower than 17,545,234
'''



if __name__ == "__main__":
	
	inputFile = "day7.txt"
	directories = {}
	current_path = []
		
	with open(inputFile) as fp:
		for line in fp:
			line_info = line.split()
			
			# Change directory will manipulate the path array
			if 'cd' in line_info:
				if '..' in line_info:
					current_path.pop()
				else:
					list_path = list(line_info[2])
					for item in list_path:
						current_path.append(item)
						
			# These lines don't do anything
			elif 'ls' in line_info or 'dir' in line_info:
				continue
				
			# Whatever is left are the files
			else:
				bytes = line_info[0] # The size of the file
				path = current_path.copy() # Creates a temp path array without corrupting the original
				i = len(path) # Used to go backward down the file path (e.g. /egg --> /eg --> /e --> /)
				while i >= 1:
					path_index = ''.join(path) # Converts the temp path array into a string (index)
					if path_index in directories:
						directories[path_index] = int(bytes) + int(directories[path_index])
					else:
						directories[path_index] = bytes
					path.pop()
					i = len(path)
	
	answer = 0
	for key in directories:
		if int(directories[key]) < 100000:
			answer += int(directories[key])
	print("Total filesize in which a directory is less than 100,000 bytes : " + str(answer))
	
	total_used_disk = directories["/"]
	print("Total used disk: " + str(total_used_disk))
	target = 30000000
	answer = directories["/"]
	for key in directories:
		difference = int(total_used_disk) - int(directories[key])
		if int(difference) < target:
			temp_answer = directories[key]
			if int(temp_answer) < int(answer):
				answer = temp_answer
	
	print("Filesize required for deletion: " + str(answer))
























