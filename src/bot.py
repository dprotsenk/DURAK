from basicplayer import BasicPlayer
import re

class Bot(BasicPlayer):
	def __init__(self):
		super().__init__()
		self.trump=0
		self.cards_on_table=[]
		self.pattern_card=re.compile(r'\[(\d+) ([a-zA-Z]+)\]')
		
	def send_msg(self, message):
		if message.startswith("Trump is"):
			self.trump=self.remember_trump(message)
		if message.startswith("Cards on table ["):
			self.cards_on_table=self.remember_cards_on_table()
#		if message.startswith("--------Attack--------"):
#			self.attack=
	
	def remember_trump(self, trump):
		cards = [[int(i[0]), i[1]] for i in self.pattern_card.findall(trump)]
		return cards[0]
		
	def remember_cards_on_table(self, cards_on_table):
		cards = [[int(i[0]), i[1]] for i in self.pattern_card.findall(cards_on_table)]
		return cards
		
#	def attack(self):
		
	def unique_values(self):
		a=[self.cards[0]]
		for i in range(len(self.cards)-1):
			if self.cards[i].value < self.cards[i+1].value:
				a.append(self.cards[i+1])
		return a
		
	def my_lowest_card():
		t=[]
		if len(self.cards_on_table) > 0:
			for i in self.cards_on_table:
				t.append(i.value)
		
		if len(self.cards_on_table) == 0:
			a=self.cards[0]
			for i in range(len(self.cards)-1):
				if a > self.cards[i+1].value and self.cards[i+1].suit != self.trump.suit and a.value in t:
					a = self.cards[i+1]
				elif a > self.cards[i+1].value
					a = self.cards[i+1]
				return a
				
				
			
			for j in self.cards_on_table
				for i in range(len(self.cards)-1):
					if a in j and a < self.cards[i+1].value:
						a.append(self.cards[i+1])
				return a
			
			
			
b=Bot()

b.send_msg("Cards on table [[6 Bubna], [7 Cherva], [8 Krest], [9 Krest], [9 Cherva], [12 Bubna]]")

		
