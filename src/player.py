from basicplayer import BasicPlayer

class Player(BasicPlayer):
	def send_msg(self, message):
		print(message)
		
	def get_command(self):
		a = input()
		return a
		