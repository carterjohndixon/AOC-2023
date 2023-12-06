import sys

D = open(sys.argv[1]).read().strip()
lines = D.split('\n')

# PART ONE:
# seeds, *conv_map = D.split('\n\n')
# seeds = list(map(int, seeds.split(':')[1].split()))

# for conv in conv_map:
# 	nums = []
# 	for line in conv.splitlines()[1:]:
# 		nums.append(list(map(int, line.split())))
# 	res = []
# 	for seed in seeds:
# 		for dest_start, source_start, range_len in nums:
# 			if seed >= source_start and seed < source_start + range_len:
# 				seeds = dest_start + (seed - source_start)
# 				res.append(seeds)
# 				break
# 		else:
# 			res.append(seed)

# 	seeds = res

# print(min(seeds))

# PART TWO:
t, *conv_map = D.split('\n\n')
t = list(map(int, t.split(':')[1].split()))

seeds = []

for i in range(0, len(t), 2):
	seeds.append((t[i], t[i] + t[i+1]))

for conv in conv_map:
	nums = []
	for line in conv.splitlines()[1:]:
		nums.append(list(map(int, line.split())))
	res = []

	while len(seeds) > 0:
		start, end = seeds.pop()
		for a, b, c in nums:
			ovs = max(start, b)
			ove = min(end, b +c)
			if ovs < ove:
				res.append((ovs - b + a, ove - b + a))
				if ovs > start:
					seeds.append((start, ovs))
				if end > ove:
					seeds.append((ove, end))
				break
		else:
			res.append((start, end))

	seeds = res

print(min(seeds)[0])