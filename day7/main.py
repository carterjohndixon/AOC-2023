import sys

D = open(sys.argv[1]).read().strip()
lines = D.split('\n')

# PART ONE:
# letters = {"T": "A", "J": "B", "Q": "C", "K": "D", "A": "E"}

# def find(hand):
# 	counts = [hand.count(card) for card in hand]

# 	if 5 in counts:
# 		return 6
# 	if 4 in counts:
# 		return 5
# 	if 3 in counts:
# 		if 2 in counts:
# 			return 4
# 		return 3
# 	if counts.count(2) == 4:
# 		return 2
# 	if 2 in counts:
# 		return 1
# 	return 0


# def get_strength(hand):
# 	hand_with_vals = ''.join(letters.get(card, card) for card in hand)
# 	return (find(hand_with_vals), hand_with_vals)

# def calc_winnings(hands):
# 	sorted_hands = sorted(hands, key=lambda x: (get_strength(x[0]), x[1]))

# 	total_winnings = sum(bid * rank for rank, (_,bid) in enumerate(sorted_hands, start=1))

# 	return total_winnings

# hands = []
# for line in lines:
# 	hand, bid = line.split()
# 	hands.append((hand, int(bid)))

# total_winnings = calc_winnings(hands)

# print(total_winnings)

# PART TWO:
letters = {"T": "A", "J": "0", "Q": "C", "K": "D", "A": "E"}

def find(hand):
	counts = [hand.count(card) for card in hand]

	if 5 in counts:
		return 6
	if 4 in counts:
		return 5
	if 3 in counts:
		if 2 in counts:
			return 4
		return 3
	if counts.count(2) == 4:
		return 2
	if 2 in counts:
		return 1
	return 0


def get_replacements_for_hand(hand):
	if not hand:
		return [""]

	if hand[0] == "J":
		return [x + y for x in "23456789TQKA" for y in get_replacements_for_hand(hand[1:])]

	return [hand[0] + y for y in get_replacements_for_hand(hand[1:])]

def max_score(hand):
	return max(map(find, get_replacements_for_hand(hand)))

def get_strength(hand):
	return (max_score(hand), [letters.get(card, card) for card in hand])

def calc_winnings(hands):
	sorted_hands = sorted(hands, key=lambda x: (get_strength(x[0]), x[1]))

	total_winnings = sum(bid * rank for rank, (_,bid) in enumerate(sorted_hands, start=1))

	return total_winnings

hands = []
for line in lines:
	hand, bid = line.split()
	hands.append((hand, int(bid)))

total_winnings = calc_winnings(hands)


print(total_winnings)