import sys

D = open(sys.argv[1]).read().strip()
lines = D.split('\n')

#PART ONE:
# res = 0
# for line in lines:
# 	cardl, cardr = line.split('|')
# 	id_, card = cardl.split(':')
# 	cardl_nums = [int(x) for x in card.split()]
# 	cardr_nums = [int(x) for x in cardr.split()]
# 	val = len(set(cardl_nums) & set(cardr_nums))
# 	if val > 0 :
# 		res += 2**(val-1)
# print(res)

# PART TWO
from collections import defaultdict
res = defaultdict(int)
for n, line in enumerate(lines):
	res[n] += 1
	cardl, cardr = line.split('|')
	id_, card = cardl.split(':')
	cardl_nums = [int(x) for x in card.split()]
	cardr_nums = [int(x) for x in cardr.split()]
	val = len(set(cardl_nums) & set(cardr_nums))
	for i in range(val):
		res[n+1+i] += res[n]

print(sum(res.values()))