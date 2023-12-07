import sys

# PART ONE:

# D = open(sys.argv[1]).read().strip()
# lines = D.split('\n')

# times, distances = [list(map(int, line.split(':')[1].split())) for line in lines]

# t = 1
# for time,distance in zip(times, distances):
# 	m = 0
# 	for i in range(time):
# 		if i * (time - i) > distance:
# 			m += 1
# 	t *= m

# print(t)

# PART TWO:
D = open(sys.argv[1]).read().strip().replace(' ', '')
lines = D.split('\n')

times, distances = [list(map(int, line.split(':')[1].split())) for line in lines]

t = 1
for time,distance in zip(times, distances):
	m = 0
	for i in range(time):
		if i * (time - i) > distance:
			m += 1
	t *= m

print(t)