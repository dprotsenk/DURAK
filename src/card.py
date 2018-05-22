import random

class Card:
	def __init__(self, suit, value):
		self.suit=suit
		self.value=value
		
	def __str__(self):
		print_card="[{} {}]".format(self.value, self.suit)	
		return print_card
		
	def __repr__(self):
		print_card="[{} {}]".format(self.value, self.suit)	
		return print_card

class Card_deck:
	def __init__(self):
		self.total=36
		self.set_cards()
		self.set_trump()
	
	def set_tacke(self):
		self.total = self.total-1
		
	def set_cards(self):
		self.cards=[]
		suit=['Bubna', 'Krest', 'Cherva', 'Pika']
		value=list(range(6,15)) #value=list(range(6,15))
		for i in suit:
			for j in value:
				self.cards.append(Card(i,j))
		random.shuffle(self.cards)
				
	def get_card(self):
		self.total-=1
		return self.cards.pop()

	
	def set_trump(self):
		self.trump=self.cards[0]
		
	def get_trump(self):
		return self.trump
		
	def get_total_card_deck(self):
		return len(self.cards)
	
				
			
	
	
		