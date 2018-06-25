from basicplayer import BasicPlayer
import re
from card import Card_deck

class Bot(BasicPlayer):
	def __init__(self):
		super().__init__()
		self.trump=0
		self.cards_on_table=[]
		self.pattern_card=re.compile(r'\[(\d+) ([a-zA-Z]+)\]')
		self.deck=Card_deck()
		self.cards=[]
		self.command=[]
		self.action_type=0
		
	def get_command(self):
		return self.command.pop()
		
	def send_msg(self, message):
		print("MESSSAAAAGEEE", message)
		if message.startswith("Trump is"):
			self.trump=self.remember_trump(message)
		if message.startswith("Cards on table"):
			self.cards_on_table=self.remember_cards_on_table(message)
		if message.startswith("--------Attack--------"):
			self.attack()
		if message.startswith("--------Defend--------"):
			self.defend()
		if message.startswith("--------Podbros--------"):
			self.attack()
		
	# def send_msg(self, message):
		# if message.startswith("Trump is"):
			# self.trump=self.remember_trump(message)
		# if message.startswith("Cards on table"):
			# self.cards_on_table=self.remember_cards_on_table(message)
			# if self.action_type==self.attack or self.action_type==self.defend:
				# self.action_type()
		# if message.startswith("--------Attack--------"):
			# self.action_type=self.attack
		# if message.startswith("--------Defend--------"):
			# self.action_type=self.defend
		# if message.startswith("--------Podbros--------"):
			# self.action_type=self.attack

			
	def remember_trump(self, trump):
		cards = [[int(i[0]), i[1]] for i in self.pattern_card.findall(trump)]
		return cards[0]
		
	def remember_cards_on_table(self, cards_on_table):
		cards = [[int(i[0]), i[1]] for i in self.pattern_card.findall(cards_on_table)]
		return cards

		
	def unique_values(self):
		a=[self.cards[0]]
		for i in range(len(self.cards)-1):
			if self.cards[i].value < self.cards[i+1].value:
				a.append(self.cards[i+1])
		return a
		
	def my_lowest_card_to_pohodit(self):
		b=0
		trumps=0
		for l in self.cards:
			if l.suit != self.trump:
				trumps=trumps+1
		if trumps == len(self.cards):	
			a = self.cards[0]
			for i in self.cards:
				if a.value>i.value:
					a=i
		else:
			while True:
				if self.cards[b].suit != self.trump[1]:
					a=self.cards[b]
					break	
			for i in self.cards:
				print(i)
				if a.value>i.value and i.suit != self.trump[1]:
					a=i
		a = self.cards.index(a)
		return a+1
	
	def my_lowest_card_to_podkinut(self):
		self.cards_on_table.sort()
		for i in self.cards_on_table:
			for j in self.cards:
				if j.value == i[0] and j.suit != self.trump[1]:
					j = self.cards.index(j)
					return j
		for i in self.cards_on_table:
			for j in self.cards:
				if j.value == i[0]:
					j = self.cards.index(j)
					return j
		return "end"
			
	def my_lowest_card_to_otbit(self):
		print("self.cards_on_table")
		print(self.cards_on_table)
		possible_cards=[]
		suit = self.cards_on_table[-1][1]
		value = self.cards_on_table[-1][0]
		for j in self.cards:
			if j.suit == suit and j.suit != self.trump:
				if j.value > value:
					j = self.cards.index(j)
					return j
		for j in self.cards:
			if j.suit == suit:
				if j.value > value:
					j = self.cards.index(j)
					return j
		return "get"
		
	def attack(self):
		if len(self.cards_on_table)==0:
			self.command.append(self.my_lowest_card_to_pohodit())
			self.command.append("put")
			print(self.cards)
			print(self.command)
		else:
			self.command.append(self.my_lowest_card_to_podkinut())
			if self.command[0] != "end":
				self.command.append("put")
				
	def defend(self):
		self.command.append(self.my_lowest_card_to_otbit())
		if self.command[0] != "put":
			self.command.append("put")
		
	def razdacha(self):
		for i in range(10):
			self.cards.append(self.deck.get_card())
			
# b=Bot()
# b.razdacha()
# b.send_msg("Cards on table [[6 Bubna], [7 Cherva], [8 Krest], [9 Krest], [9 Cherva], [12 Bubna]]")
# b.send_msg("--------Defend--------")

# b.send_msg("Cards on hends: [[6 Krest], [7 Bubna], [9 Bubna], [10 Bubna], [12 Pika], [12 Pika]]")
#print(b.attack())

		
