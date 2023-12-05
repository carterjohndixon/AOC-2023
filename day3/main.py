# PART ONE:
# def find_numbers_and_symbols(line, line_number):
# 	num_coords = []
# 	symbol_coords = []
# 	num_start = None
# 	for i, char in enumerate(line):
# 		if char.isdigit():
# 			if num_start is None:
# 				num_start = i
# 		elif num_start is not None:
# 			num_coords.append((line[num_start:i], [(line_number, j) for j in range(num_start, i)]))
# 			num_start = None
# 		if not char.isdigit() and char not in ('.', '\n'):
# 			symbol_coords.append([char, (line_number, i)])

# 	return num_coords, symbol_coords

# num_coords = []
# symbol_coords = []
# line_number = 0
# with open('input.txt') as file:
# 	for line in file:
# 		nums, symbols = find_numbers_and_symbols(line, line_number)
# 		num_coords.extend(nums)
# 		symbol_coords.extend(symbols)
# 		line_number += 1

# adj_nums = []
# for n in num_coords:
# 	for c in n[1]:
# 		for s in symbol_coords:
# 			if abs(c[0] - s[1][0]) <= 1 and abs(c[1] - s[1][1]) <= 1:
# 				adj_nums.append(n) if n not in adj_nums else 0
# 				break

# res = sum([int(n[0]) for n in adj_nums])
# print(res)

# PART TWO:
num_coords = []
symbol_coords = []

with open('input.txt') as file:
    for x, line in enumerate(file):
        # Find numbers
        num_start = None
        for i, char in enumerate(line):
            if char.isdigit():
                if num_start is None:
                    num_start = i
            elif num_start is not None:
                num = int(line[num_start:i])
                coords = [(x, j) for j in range(num_start, i)]
                num_coords.append([num, coords])
                num_start = None

        for i, char in enumerate(line):
            if char == '*':
                symbol_coords.append([char, (x, i), []])
    for n in num_coords:
	    for c in n[1]:
	        for s in symbol_coords:
	            if abs(c[0] - s[1][0]) <= 1 and abs(c[1] - s[1][1]) <= 1:
	                s[2].append(n) if n not in s[2] else 0
	                break

print(sum([s[2][0][0] * s[2][1][0] for s in symbol_coords if len(s[2]) == 2]))