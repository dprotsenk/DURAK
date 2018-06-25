from card import Card_deck
from player import Player
from basicplayer import BasicPlayer
from bot import Bot

class Desk:
	def __init__(self):
		self.players=[]
		self.re_hand_out_cards()
		
	def hand_out_cards(self):
		for i in self.players:
			for j in range(0,6):
				try:
					i.add_card(self.deck.get_card())
				except IndexError:
					print("podbor pust")
			print(i.get_cards())
	
	def send_msg_to_all(self, msg):
		for i in self.players:
			i.send_msg(msg)
			
	def check_cards(self, a):
		for i in self.cards_on_table:
			if a.value==i.value:
				return True	
		return False
				
	def check_defend_cards(self, a):
		trump=self.deck.get_trump().suit
		if a.suit==trump and self.cards_on_table[-1].suit!=trump:
			return True
		elif a.suit==self.cards_on_table[-1].suit and a.value>self.cards_on_table[-1].value:
			return True
		else:	
			return False				
	
	def who_first(self):
		if self.players[0].get_min_trump(self.deck.get_trump()) == None and self.players[1].get_min_trump(self.deck.get_trump()) == None:
			self.re_hand_out_cards()
		elif (self.players[0].get_min_trump(self.deck.get_trump()) == None and self.players[1].get_min_trump(self.deck.get_trump()) != None) or (self.players[0].get_min_trump(self.deck.get_trump()) != None and self.players[1].get_min_trump(self.deck.get_trump()) != None and self.players[1].get_min_trump(self.deck.get_trump()).value < self.players[0].get_min_trump(self.deck.get_trump()).value):
			return 1
		elif (self.players[1].get_min_trump(self.deck.get_trump()) == None and self.players[0].get_min_trump(self.deck.get_trump()) != None) or (self.players[0].get_min_trump(self.deck.get_trump()) != None and self.players[1].get_min_trump(self.deck.get_trump()) != None and self.players[1].get_min_trump(self.deck.get_trump()).value > self.players[0].get_min_trump(self.deck.get_trump()).value):
			return 0
			
	def re_hand_out_cards(self):
		self.cards_on_table=[]
		#self.players.append(Player())
		self.players.append(Bot())
		self.players.append(Player())
		self.deck=Card_deck()
		self.hand_out_cards()
		print("Trump is {}".format(self.deck.get_trump()))	
		self.players[0].set_user_name("BOT") ############  NAME SET
		self.players[1].set_user_name("JOE") ############  NAME SET
		self.current_player=self.who_first()
			
	def put_card(self, index):
		if not self.cards_on_table or self.check_cards(self.get_current_player().get_cards()[index]):
			self.cards_on_table.append(self.players[self.current_player].get_card(index))
			#self.send_msg_to_all(self.cards_on_table[-1])
		else:
			self.get_current_player().send_msg("You cannot podkinut etu kartu")
			self.attack()
	
	def defend_card(self, index, card):
		if self.check_defend_cards(card):
			self.cards_on_table.append(self.players[self.current_player].get_card(index))
			self.get_oposit_player().send_msg("Player {} otbilsy kartoy {}".format(self.get_current_player().get_user_name(), self.cards_on_table[-1]))
			#print("error 6")
			#self.send_msg_to_all(self.cards_on_table[-1])
			#print("error 7")
			self.change_player()
		else:
			self.get_current_player().send_msg("you cannot bittn this card")
			self.deffend()
	
	def get_card_from_table(self):
		self.players[self.current_player].add_cards(self.cards_on_table)
		self.cards_on_table=[]
		self.change_player()

			
#	def podbros(self):
#		self.change_player()
#		while True:
#			try:
#				self.get_current_player().send_msg("Exit - to finish")
#				index = int(input("Which card are you going to flip?"))-1
#			except ValueError:
#				break
#			self.put_card(index)
			
	def change_player(self):
		if self.current_player == 0:
			self.current_player=1
		else:
			self.current_player=0
		
	def podbor_cards(self):
		if self.deck.get_total_card_deck() != 0:
			while len(self.get_current_player().get_cards()) < 6:
				if len(self.get_current_player().get_cards()) < 6:
					try:
						self.get_current_player().add_card(self.deck.get_card())
					except IndexError:
						break
		elif self.players[0].get_cards_amount() == self.players[1].get_cards_amount() and (self.players[0].get_cards_amount() == 0 and self.players[1].get_cards_amount() == 0):
			self.send_msg_to_all("Played in a draw")
			quit(0)
		elif self.players[0].get_cards_amount() == 0 and self.players[1].get_cards_amount() > 0:
			self.send_msg_to_all("Victory of player {}".format(self.players[0].get_user_name()))
			quit(0)
		elif self.players[1].get_cards_amount() == 0 and self.players[0].get_cards_amount() > 0:
			self.send_msg_to_all("Victory of player {}".format(self.players[1].get_user_name()))
			quit(0)
			
		
	def get_current_player(self):
		# print("current_player!!!!!!!!!!!!!!!!!!!!!", self.current_player)
		return (self.players[self.current_player])
		
	def get_oposit_player(self):
		oposit=self.players[self.current_player-1]
		return oposit
	
	def flip_card(self):
		self.change_player()
		a=0
		for i in self.cards_on_table:
			for j in self.get_current_player().get_cards():
				if i.value == j.value:
					a=a+1
		if a == 0:
			return
		else:
			try:
				self.podbros()
			except ValueError:
				self.get_current_player().send_msg("Player {} najal ne tu knopku".format(self.get_current_player().get_user_name()))	
				
	def who_defend(self):
		a=self.current_player
		if a == 1:
			a = 0
		elif a == 0:
			a = 1
		return a
		
	def attack(self):
		self.get_current_player().send_msg("Cards on table {}".format(self.cards_on_table))
		self.get_current_player().send_msg("--------Attack--------")
		#self.get_current_player().send_msg("Cards on table {}".format(self.cards_on_table))
		self.get_current_player().send_msg("Trump is {}".format(self.deck.get_trump()))
		self.get_current_player().send_msg("Current player is {}".format(self.get_current_player().get_user_name()))
		self.get_current_player().send_msg("Cards on hends: {}".format(self.get_current_player().get_cards()))
		card = self.get_current_player().get_cards()
		put = self.get_current_player().get_command()
		if "put" == put:
			index = int(self.get_current_player().get_command())-1
			self.get_oposit_player().send_msg("Player {} pohodil kartoy {}".format(self.get_current_player().get_user_name(), self.players[self.current_player].get_cards()[index]))
			#print("error 2")
			self.put_card(index)
			self.change_player()
			self.counter=self.counter+1
		elif "end" == put:
			self.cards_on_table=[]
			self.podbor_cards()
			self.change_player()
			self.counter=1
		
	def deffend(self):
		self.get_current_player().send_msg("Cards on table {}".format(self.cards_on_table))
		self.get_current_player().send_msg("--------Defend--------")
		self.get_current_player().send_msg("Trump is {}".format(self.deck.get_trump()))
		self.get_current_player().send_msg("Current player is {}".format(self.get_current_player().get_user_name()))
		self.get_current_player().send_msg("Cards on hends: {}".format(self.get_current_player().get_cards()))
		card = self.get_current_player().get_cards()
		put = self.get_current_player().get_command()
		if "put" == put:
			index = int(self.get_current_player().get_command())-1
			self.defend_card(index, card[index])
			self.counter=self.counter+1
		elif "get" == put:
			self.get_oposit_player().send_msg("Player {} cannot bit this cards.".format(self.get_current_player().get_user_name()))
			#print("error 1")
			self.flip_card()
			self.change_player()
			self.get_card_from_table()
			self.podbor_cards()
			self.counter=1	
				
	def podbros(self):
		while True:
			self.get_current_player().send_msg("Cards on table {}".format(self.cards_on_table))
			self.get_current_player().send_msg("--------Podbros--------")
			self.get_current_player().send_msg("Player {} doljen podbrosit kartu ili vvesti 'end' dla okonchania podbrose".format(self.get_current_player().get_user_name()))
			#print("error 5")
			#self.get_current_player().send_msg(self.cards_on_table)
			self.get_current_player().send_msg(self.get_current_player().get_cards())
			card = self.get_current_player().get_cards()	
			put = self.get_current_player().get_command()
			if "put" == put:
				index = int(self.get_current_player().get_command())-1
				self.get_oposit_player().send_msg("Player {} pohodil kartoy {}".format(self.get_current_player().get_user_name(), self.players[self.current_player].get_cards()[index]))
				#print("error 4")
				self.put_card(index)
			elif "end" == put:
				self.get_oposit_player().send_msg("Player {} zakonchil podbros".format(self.get_current_player().get_user_name()))
				#print("error 3")
				self.counter=1
				return
	
	def main(self):
		self.counter=1
		while True:
			if self.counter%2 == 1:
				try:
					self.attack()
				except ValueError:
					self.get_current_player().send_msg("Player {} najal ne tu knopku".format(self.get_current_player().get_user_name()))
			else:
				try:
					self.deffend()
				except ValueError:
					self.get_current_player().send_msg("Player {} najal ne tu knopku".format(self.get_current_player().get_user_name()))
			
			
desk = Desk()
desk.main()