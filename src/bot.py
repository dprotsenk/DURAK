from basicplayer import BasicPlayer
import re

class Bot(BasicPlayer):
	def __init__(self):
		super().__init__()
		self.trump=[]
		self.cards_on_table=[]
		self.pattern_card=re.compile(r'\[(\d+) ([a-zA-Z]+)\]')
		
	def send_msg(self, message):
		if message.startswith("Trump is"):
			self.trump=self.remember_trump(message)
		if message.startswith("Cards on table ["):
			self.cards_on_table=self.remember_cards_on_table()
	
	def remember_trump(self, trump):
		cards = [[int(i[0]), i[1]] for i in self.pattern_card.findall(trump)]
		return cards[0]
		
	def emember_cards_on_table(self, cards_on_table):
		cards = [[int(i[0]), i[1]] for i in self.pattern_card.findall(cards_on_table)]
		return cards
