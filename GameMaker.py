from Landmark import Landmark
from StringClue import StringClue
from StringQuestion import StringQuestion
from User import User
from Test import Test


class GameMaker(User):
	def __init__(self, game):
		super().__init__()
		self.commands = {1: "logout(self)", 2: "list_commands(self)"}  # dict
		self.password = "pw"
		self.name = "un"
		self.myGame = game
		self.myTeams = {}

	# # User Inheritance:
	# def login(self, password, name) -> bool:
	# 	return self.password == password and self.name == name

	def list_commands(self) -> dict:
		return self.commands

	# Game Maker Specific:

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
		self.myGame.get_landmark_by_name(name).set_clue(tempClue)
		return True

	def edit_landmark_question(self, name, new_question, new_answer) -> bool:
		tempQuestion = StringQuestion(new_question, new_answer)
		self.myGame.get_landmark_by_name(name).set_confirmation(tempQuestion)
		return True

	def list_landmarks(self) -> str:
		stringlist = None
		for i in self.myGame.landmarkList:
			stringlist += ''.join(self.myGame.landmarkList[i].name)
		return stringlist
	
	def create_team(self, name):
		tempTeam = Team(name)
		self.myTeams{tempTeam:User}


	# def create_scavenger_hunt(self):
	# 	pass

	# def add_landmark_to_scavenger_hunt(self):
	# 	pass

	def end_game(self) -> bool:
		self.myGame.stop()
		return True
