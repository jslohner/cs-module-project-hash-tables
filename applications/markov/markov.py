import random

# Read in all the words in one go
with open("input.txt") as f:
	words = f.read()
	words = words.strip().split(' ')
	temp_words = []
	for i in range(len(words) - 1):
		# if '\n' in words[i]:
		x = words[i].split('\n')
		for word in x:
			if word:
				temp_words.append(word.strip())
	words = temp_words

# TODO: analyze which words can follow other words
mem = {}
for i in range(len(words) - 1):
	# words[i].split('\n')
	if words[i] not in mem:
		# mem[words[i]] = words[i + 1]
		mem[words[i]] = []
	mem[words[i]].append(words[i + 1])

# TODO: construct 5 random sentences
def find_start():
	findingWord = True
	while findingWord:
		start = random.choice(list(mem.keys()))
		if (start[0].isalpha()) and (start[0] == start[0].upper()):
			findingWord = False
		elif (start[0] == ('"')) and (start[1] == start[1].upper()):
			findingWord = False
	return start

def print_sequence(num_sentences):
	for i in range(num_sentences):
		start = find_start()
		print(start, end=" ")
		findingWord = True
		end_matches = ['.', '?', '!']
		while findingWord:
			key = random.choice(list(mem.keys()))
			next = random.choice(mem[key])
			if any(c == key[-1] for c in end_matches):
				print(key, end=" ")
				findingWord = False
				break
			elif (len(key) >= 2) and (key[-1] == ('"')) and (any(c == key[-2] for c in end_matches)):
				print(key, end=" ")
				findingWord = False
				break
			else:
				print(key, end=" ")
			# ---
			if any(c == next[-1] for c in end_matches):
				print(next, end=" ")
				findingWord = False
				break
			elif (len(next) >= 2) and (next[-1] == ('"')) and (any(c == next[-2] for c in end_matches)):
				print(next, end=" ")
				findingWord = False
				break
			else:
				print(next, end=" ")
		print()

print_sequence(10)
