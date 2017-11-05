# interfaces
# TODO: Where Does LandmarkGameMaker fit in Exactly?
from Game import Game
# Classes used
from GameGameMaker import GameGameMaker
from User import User


class GameMaker(User):
	commands = {}  # dict
	game = GameGameMaker  # TODO: Unsure about this?
	temp_landmarks = {}
	temp_users = {}

	# User Inheritance:

	def login(self) -> bool:
		pass

	def logout(self):
		pass

	def list_commands(self) -> dict:
		pass

	# Game Maker Specific:

	def create_game(self) -> Game:
		pass

	def create_landmark(self, name, clue, question, answer) -> bool:
		pass

	def edit_landmark_clue(self, name, old_clue, new_clue) -> bool:
		pass

	def edit_landmark_question(self, name, old_question, new_question, new_answer) -> bool:
		pass

	def create_team(self, name) -> bool:
		pass

	def create_scavenger_hunt(self):
		pass

	def add_landmark_to_scavenger_hunt(self):
		pass

	def end_game(self):
		pass
