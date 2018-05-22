
class BasicPlayer:
	def __init__(self):
		self.cards=[]
		
	def add_card(self, a):
		self.cards.append(a)
		
	def add_cards(self, a):
		self.cards.extend(a)

	def get_card(self, a):
		return self.cards.pop(a)
	
	def get_cards(self):
		return self.cards
		
	def get_cards_amount(self):
		return len(self.cards)
		
	def get_min_trump(self, a):
		trump=None
		for i in self.cards:
			if i.suit==a.suit and (trump == None or (trump != None and i.value < trump.value)):
				trump=i
		return trump
		
	def get_command(self):
		pass
		
	def send_msg(self):
		pass
		
	def set_user_name(self, name):
		self.name=name
		
	def get_user_name(self):
		return self.name