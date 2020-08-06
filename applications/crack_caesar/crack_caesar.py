# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.
def crackCaesar():
	mem = {}
	letterKey = {}
	totalLetters = 0
	frequencies = {
		'E': 11.53,
		'T': 9.75,
		'A': 8.46,
		'O': 8.08,
		'H': 7.71,
		'N': 6.73,
		'R': 6.29,
		'I': 5.84,
		'S': 5.56,
		'D': 4.74,
		'L': 3.92,
		'W': 3.08,
		'U': 2.59,
		'G': 2.48,
		'F': 2.42,
		'B': 2.19,
		'M': 2.18,
		'Y': 2.02,
		'C': 1.58,
		'P': 1.08,
		'K': 0.84,
		'V': 0.59,
		'Q': 0.17,
		'J': 0.07,
		'X': 0.07,
		'Z': 0.03
	}
	with open('ciphertext.txt', 'r') as f:
		fileString = f.read()
		for x in fileString:
			if x.isalpha():
				if x not in mem:
					mem[x] = 0
					letterKey[x] = x
				mem[x] += 1
				totalLetters += 1
	for key in mem:
		mem[key] = round((round((mem[key] / totalLetters), 4) * 100), 4)

	mem = {k:v for k,v in sorted(mem.items(), key=lambda item: item[1], reverse=True)}
	letterKey = {k:v for k,v in sorted(letterKey.items())}
	for key in mem:
		for key2 in frequencies:
			if mem[key] == frequencies[key2]:
				letterKey[key] = key2

	fileList = [c for c in fileString]
	for i in range(len(fileList) - 1):
		if fileList[i].isalpha():
			fileList[i] = letterKey[fileList[i]]
	fileString = ''.join(fileList)
	return fileString

print(crackCaesar())
