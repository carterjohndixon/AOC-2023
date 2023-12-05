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
# def find_numbers_and_symbols(line, line_number):
# 	num_coords = []
# 	symbol_coords = []
# 	num_start = None
# 	for i, char in enumerate(line):
# 		if char.isdigit():
# 			if num_start is None:
# 				num_start = i
# 		elif num_start is not None:
# 				num_coords.append((int(line[num_start:i]), (line_number, num_start)))
# 				num_coords.append((int(line[num_start:i]), (line_number, i - 1)))
# 				num_start = None
# 		if not char.isdigit() and char not in ('.', '\n'):
# 			symbol_coords.append([char, (line_number, i)])

# 	return num_coords, symbol_coords

# def get_adjacent_nums(coord, num_coords):
# 	adjacent_nums = []

# 	for c in num_coords:
# 		if (
# 			abs(c[1][0] - coord[1][0]) <= 1
# 			and abs(c[1][1] - coord[1][1]) <= 1
# 			and c[0] != coord[0]
# 		):
# 			adjacent_nums.append(c[0])

# 	return adjacent_nums

# def calc_gear_ratio(num_coords, symbol_coords):
# 	gear_ratios = set()

# 	for s in symbol_coords:
# 		if s[0] == '*':
# 			adjacent_nums = get_adjacent_nums(s, num_coords)
# 			print(adjacent_nums)

# 			if len(adjacent_nums) == 2:
# 				gear_ratios.add(tuple(sorted(adjacent_nums)))
# 				print(gear_ratios)

# 	return gear_ratios

# num_coords = []
# symbol_coords = []
# line_number = 0
# with open('test.txt') as file:
# 	for line in file:
# 		nums, symbols = find_numbers_and_symbols(line, line_number)
# 		num_coords.extend(nums)
# 		symbol_coords.extend(symbols)
# 		line_number += 1

# gear_ratios = calc_gear_ratio(num_coords, symbol_coords)

# res_part_two = sum(gear[0] * gear[1] for gear in gear_ratios)
# print(res_part_two)

# import re

# num_coords = []
# symbol_coords = []
# with open('input.txt') as file:
# 	for x, line in enumerate(file):
# 	    nums = re.finditer(r'\d+', line)
# 	    for n in nums:
# 	        coords = []
# 	        for i in range(len(n.group())):
# 	            coords.append((x, n.start() + i))
# 	        num_coords.append([int(n.group()), coords])
# 	    symbols = re.finditer(r'[*]', line)
# 	    for s in symbols:
# 	        symbol_coords.append([s.group(), (x, s.start()), []])
# 	for n in num_coords:
# 	    for c in n[1]:
# 	        for s in symbol_coords:
# 	            if abs(c[0] - s[1][0]) <= 1 and abs(c[1] - s[1][1]) <= 1:
# 	                s[2].append(n) if n not in s[2] else 0
# 	                break

# print('Day 03 Part 2:', sum([s[2][0][0] * s[2][1][0] for s in symbol_coords if len(s[2]) == 2]))

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