#https://leetcode.com/problems/minimum-consecutive-cards-to-pick-up/

def minimumCardPickup(self, cards: List[int]) -> int:
	dic = {}
	mini = 10000000
	for index, card in enumerate(cards):
		if not card in dic.keys():
			dic[card] = index
		else:
			sub = index-dic[card]+1
		if sub < mini:
			mini = sub
			dic[card] = index
	if mini == 10000000:
		return -1
	return mini
