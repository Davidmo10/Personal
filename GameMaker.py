# interfaces
# TODO: Where Does LandmarkGameMaker fit in Exactly?
from Game import Game
# Classes used
from GameGameMaker import GameGameMaker
from User import User
<<<<<<< HEAD
from Landmark import Landmark
from StringQuestion import StringQuestion
from StringClue import StringClue
=======
from Game import Game
>>>>>>> 43972caa8ccb7fe1c61110f6e3a802b9e9d28e99


class GameMaker(User):
	def __init__(self, game):
		super().__init__()
		self.commands = {"login": (lambda user, password: self.login(user, password)), 1: "logout(self)", 2: "list_commands(self)"}  # dict
		self.password = "pw"
		self.name = "un"
		self.myGame = game

	# # User Inheritance:
	# def login(self, password, name) -> bool:
	# 	return self.password == password and self.name == name

<<<<<<< HEAD
	# def logout(self):
	# 	return None
=======
	def login(self) -> bool:
		pass

<<<<<<< HEAD
	def __init__(self, user_id):
		super().__init__(user_id)
=======
	def logout(self):
		pass
>>>>>>> 43972caa8ccb7fe1c61110f6e3a802b9e9d28e99

	def list_commands(self) -> dict:
		return self.commands

	# Game Maker Specific:
<<<<<<< HEAD
	# def create_game(self):
	# 	self.myGame.start();
	# 	return self.myGame

	def create_landmark(self, name) -> bool:
		temp_landmark = Landmark(name)

		# temp_landmark.add_confirmation(question, answer)
		# temp_landmark.add_clue(clue, clue)

		self.myGame.landmarkList.append(temp_landmark)
		return True

	def edit_landmark_clue(self, name, new_clue: str) -> bool:
		tempClue = StringClue(new_clue)
		self.myGame.get_landmark_by_name(name).add_clue(tempClue)
		return True

	def edit_landmark_question(self, name, new_question, new_answer) -> bool:
		tempQuestion = StringQuestion(new_question, new_answer)
		self.myGame.get_landmark_by_name(name).add_confirmation(tempQuestion)
		return True
=======
>>>>>>> master
>>>>>>> 43972caa8ccb7fe1c61110f6e3a802b9e9d28e99

	def list_landmarks(self) -> str:
		stringlist = None
		for i in self.myGame.landmarkList:
			stringlist += ''.join(self.myGame.landmarkList[i].name)
		return stringlist



	# def create_team(self, name) -> bool:
	# 	self.temp_user = User


	# def create_scavenger_hunt(self):
	# 	pass

	# def add_landmark_to_scavenger_hunt(self):
	# 	pass

	def end_game(self):
		self.myGame.stop()
