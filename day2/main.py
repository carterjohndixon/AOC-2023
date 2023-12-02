#PART ONE:
games = []
with open('input.txt') as file:
	for line in file:
		go = True
		line = line.strip()
		id,line = line.split(':')
		for game in line.split(';'):
			for cube in game.split(','):
				num,color = cube.split()
				if int(num) > {'red': 12, 'green': 13, 'blue': 14}.get(color):
					go = False
		if go:
			games.append(int(id.split()[-1]))
res = sum(games)
print(res)

#PART TWO:
games = []
with open('input.txt') as file:
	for line in file:
		go = True
		line = line.strip()
		id,line = line.split(':')
		d = {}
		for game in line.split(';'):
			for cube in game.split(','):
				num,color = cube.split()
				num = int(num)
				if color not in d:
					d[color] = num
				else:
					d[color] = max(d[color], num)
				if int(num) > {'red': 12, 'green': 13, 'blue': 14}.get(color,0):
					go = False
		p = 1
		for d in d.values():
			p *= d
		games.append(p)
res = sum(games)
print(res)