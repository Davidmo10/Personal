from User import User
from Game import Game
from Clue import Clue


class Team(User):

	def __init__(self, game: Game):
		super.__init__()
		self.commands = {"login": (lambda user, password: self.login(user, password)), 1: "logout(self)",
		                 2: "list_commands(self)"}  # dict
		self.landmark_index = 0  # index
		# self.this_team_index = team_index  # This index has to come from outside team to logout
		# 								   # Each team will need an index in username list so when they
		# 								   # login they are linked to the right team
		self.myGame = game
		self.has_requested = False
		self.forfeited = False   #Untill we can pass user indexes between game and user to flag login
								 #This is a temporary solution

	# def login(self):
	# 	pass
	#
	# def logout(self):
	# 	pass

	def list_commands(self) -> dict:
		return self.commands

	def request_clue(self) -> Clue:
		if self.forfeited:
			return self.myGame.get_clue(self.landmark_index)

	def request_question(self):
		if self.forfeited:
			self.has_requested = True
			return self.myGame.get_question(self.landmark_index)

	def answer(self, string):
		if self.forfeited:
			if self.has_requested:
				raise Exception

		correct = self.myGame.check_answer(self.landmark_index, string)

		if correct:
			self.has_requested = False
			self.landmark_index += 1

		return correct

	def forfeit(self) -> bool:
		if self.forfeited:
			self.forfeited = False
			return self.forfeited
