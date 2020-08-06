import re

def printWordHistogram(filename):
	mem = {}
	longestStr = 0
	with open(filename, 'r') as f:
		# print(f.readlines())
		for line in f:
			wordList = list(filter(None, (re.split('[\\\\\-\[\]\":;,.+=/|{}()*^&\s]', line.lower()))))
			for word in wordList:
				word = re.sub(r'[^\w\s]', '', word)
				if len(word) > longestStr:
					longestStr = len(word)
				if word not in mem:
					mem[word] = ''
				mem[word] += '#'
	mem = {k:v for k,v in sorted(mem.items(), key=lambda item: (-len(item[1]), item[0]))}
	for key in mem:
		print(f'{key:<{longestStr + 2}}{mem[key]}')

printWordHistogram('robin.txt')
