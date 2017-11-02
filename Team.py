from User import User
from Game import Game


class Team(User):

	commands = {}   # dict

	landmark = 0    # index

	def __init__(self):
		self.game = Game()
		self.has_requested = False

	def login(self):
		pass

	def logout(self):
		pass

	def list_commands(self):
		pass

	def request_clue(self):
		pass

	def request_question(self):
		self.has_requested = True
		return self.game.get_question(self.landmark)

	def answer(self, string):
		if not self.has_requested:
			raise Exception

		correct = self.game.check_answer(self.landmark, string)

		if correct:
			self.has_requested = False
			self.landmark += 1

		return correct

	def forfeit(self):
		pass

