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
'''



if __name__ == "__main__":
	
	inputFile = "day7.txt"
	directories = {}
	current_path = []
		
	with open(inputFile) as fp:
		for line in fp:
			line_info = line.split()
			if 'cd' in line_info:
				if '..' in line_info:
					current_path.pop()
				else:
					current_path.append(line_info[2])
			elif 'ls' in line_info or 'dir' in line_info:
				continue
			else:
				path = ''.join(current_path)
				bytes = line_info[0]
				temp_path = current_path.copy()
				i = len(temp_path)
				while i >= 1:
					rolling_path = ''.join(temp_path)
					if rolling_path in directories:
						directories[rolling_path] = int(bytes) + int(directories[rolling_path])
					else:
						directories[rolling_path] = bytes
					temp_path.pop()
					i = len(temp_path)
	print(directories)
	
	answer = 0
	for key in directories:
		if int(directories[key]) < 100000:
			answer += int(directories[key])
	print("Answer: " + str(answer))
























