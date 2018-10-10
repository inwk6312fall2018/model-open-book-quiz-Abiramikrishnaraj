import pyCardDeck
import random
class Card():
	def __init__(self,suit,val):
		self.suit=suit
		self.value=val
	def show(self):
		print("{} of {}".format(self.value,self.suit))
class Deck():
	def __init__(self):
		self.cards=[]
		self.build()
	def build(self):
		for s in ["spades","clubs","diamonds","hearts"]:
			for v in range(1,14):
				self.card.append(card(s,v))
				if v == 1:
					print("A")
	def show(self):
		for c in self.card:
			print(c.show())
	"""def shuffle(self):
		for i in range(len(self.cards)-1,0,-1):
			r=random.randint(0,i)
			self.card[i],self.card[r]=self.card[r],self.card[i]"""
#print()
#card=Card("clubs",6)
#print(Deck.shuffle())
#print(Deck.show())

