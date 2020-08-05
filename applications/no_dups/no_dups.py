def no_dups(s):
	mem = {}
	word_list = s.strip().split(' ')
	rtn_str = ''
	for i in range(len(word_list)):
		if word_list[i] not in mem:
			mem[word_list[i]] = word_list[i]
			rtn_str += f' {word_list[i]}' if i != 0 else f'{word_list[i]}'
	return rtn_str

if __name__ == "__main__":
	print(no_dups(""))
	print(no_dups("hello"))
	print(no_dups("hello hello"))
	print(no_dups("cats dogs fish cats dogs"))
	print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
