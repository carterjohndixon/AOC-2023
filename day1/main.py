# PART ONE:

nums = []

with open('input.txt') as file:
	for line in file:
		digits = [char for char in line if char.isdigit()]
		nums.append(int(digits[0] + digits[-1]))

res = sum(nums)

print(res)

# PART TWO:
nums = []
with open('input.txt') as file:
	for line in file:
		digits = []
		for i,d in enumerate(line):
			if d.isdigit():
				digits.append(d)
			for d,c in enumerate(['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']):
				if line[i:].startswith(c):
					digits.append(str(d+1))
		if digits:
			nums.append(int(digits[0]+digits[-1]))

res = sum(nums)
print(res)