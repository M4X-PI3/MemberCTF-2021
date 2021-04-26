arr = [86, 126, 118, 121, 126, 105, 88, 79, 93, 96, 67, 43, 105, 68, 40, 104, 47, 98, 68, 77, 113, 107, 75, 105, 43, 68, 43, 99, 42, 41, 40, 102]
key = 27

result = []
for num in arr:
	result.append(chr(num^key))

print(''.join(result))