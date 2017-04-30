

class Card(object):
	def __init__(self,suit,value):
		self.suit = suit
		self.value = value


class Deck(object):
	def __init__(self):
		#build the deck
		self.deck = []

		suits = ['Clubs','Spades','Diamonds','Hearts']

		for suit in suits:
			for i in range(2,15):
				value = i
				if i == 11:
					value = "Jack"
				elif i == 12:
					value = "Quees"
				elif i == 13:
					value = "King"
				elif i == 14:
					value='Ace'
				self.deck.append(Card(suit,card))

card = Card('Spades','Aces')
print Deck.deck
