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