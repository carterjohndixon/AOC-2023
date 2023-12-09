import sys

D = open(sys.argv[1]).read().strip()

steps, _, *b = D.split('\n')

# PART ONE:
# path = {}

# for i in b:
#     pos, el = i.split(' = ')
#     path[pos] = el[1:-1].split(", ")

# path_count = 0
# current = 'AAA'
# target = 'ZZZ'

# while current != 'ZZZ':
# 	for step in steps:
# 	    if step == 'L':
# 	        current = path[current][0]
# 	    elif step == 'R':
# 	        current = path[current][1]

# 	    path_count += 1

# 	    if current == target:
# 	    	break

# print(path_count)

# PART TWO:
paths = {}

for i in b:
    pos, el = i.split(' = ')
    paths[pos] = el[1:-1].split(", ")

path_count = 0

def comm_div(a, b):
	while b:
		a, b = b, a % b
	return a

current_nodes = [node for node in paths.keys() if node.endswith('A')]
nodes = []

for node in current_nodes:
	new_node = []
	new_steps = steps
	step_count = 0
	z = None

	while True:
		while step_count == 0 or not node.endswith('Z'):
			if new_steps[0] == 'L':
				node = paths[node][0]
			elif new_steps[0] == 'R':
				node = paths[node][1]
			new_steps = new_steps[1:] + new_steps[0]
			step_count += 1

		new_node.append(step_count)

		if z is None:
			z = node
			step_count = 0
		elif node == z:
			break

	nodes.append(new_node)

node_count = [node[0] for node in nodes]

res = node_count.pop()

for i in node_count:
	res = res * i // comm_div(res, i)

print(res)