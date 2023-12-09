import sys

D = open(sys.argv[1]).read().strip()

lines = [list(map(int, line.strip().split())) for line in D.split('\n')]

# PART ONE:
# def extrapolate(values):
# 	if all(i == 0 for i in values):
# 		return 0

# 	difference = [b - a for a, b in zip(values, values[1:])]
# 	return values[-1] + extrapolate(difference)

# extrapolate_vals = [extrapolate(value) for value in lines]
# res = sum(extrapolate_vals)

# print(res)

# PART TWO:
def extrapolate(values):
	if all(i == 0 for i in values):
		return 0

	difference = [b - a for a, b in zip(values, values[1:])]
	return values[0] - extrapolate(difference)

extrapolate_vals = [extrapolate(value) for value in lines]
res = sum(extrapolate_vals)

print(res)