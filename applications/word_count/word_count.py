import re

def word_count(s):
	mem = {}
	word_list = list(filter(None, (re.split('[\\\\\-\[\]\":;,.+=/|{}()*^&\s]', s.lower()))))
	for word in word_list:
		if word not in mem:
			mem[word] = 0
		mem[word] += 1
	return mem

if __name__ == "__main__":
	print(word_count(""))
	print(word_count("Hello"))
	print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
	print(word_count('This is a test of the emergency broadcast network. This is only a test.'))
