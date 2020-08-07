"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

# q = set(range(1, 10))
# q = set(range(1, 200))
q = (1, 3, 4, 7, 12)


def f(x):
	return x * 4 + 6

mem = {}
mem2 = {}
for n in q:
	for n2 in q:
		mem[(n, n2)] = (n, n2)
# print(mem)
for key in mem:
	for key2 in mem:
		if (f(mem[key][0]) + f(mem[key][1])) == (f(mem[key2][0]) - f(mem[key2][1])):
			mem2[((key, key), (key2, key2))] = f'f({mem[key][0]}) + f({mem[key][1]}) = f({mem[key2][0]}) - f({mem[key2][1]})'
# print(mem2)

for key in mem2:
	print(mem2[key])
# print(len(mem))
#
# print('\n-----\n')
#
# # i = 1
# for key in mem:
# 	x = 1
# 	y = 1
# 	while x <= (len(q)):
# 		print(y)
# 		# if y == (len(q)):
# 		# 	x += 1
# 		# 	y = 1
# 		if (f(mem[key][0]) + f(mem[key][1])) == (f(mem[(x, y)][0]) - f(mem[(x, y)][1])):
# 			mem2[((key, key), (x, y))] = f'f({mem[key][0]}) + f({mem[key][1]}) = f({mem[(x, y)][0]}) - f({mem[(x, y)][1]})'
# 		if y == (len(q)):
# 			x += 1
# 			y = 1
# 		y += 1
#
# for key in mem2:
# 	print(mem2[key])
