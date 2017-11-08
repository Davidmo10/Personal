from Landmark import Landmark
from StringClue import StringClue
from StringQuestion import StringQuestion
from User import User


class GameMaker(User):
	def __init__(self, game):
		super().__init__()
		self.commands = {"crlm": lambda name: self.create_landmark(name),
		                 "crtm": lambda name, password: self.create_team(name,password),
		                 "edlmcl": lambda name, clue: self.edit_landmark_clue(name, clue),
		                 "edlmq": lambda name, question, answer: self.edit_landmark_question(name, question, answer),
		                 "end": lambda: self.end_game(),
		                 "lmks": lambda: self.list_landmarks()}  # dict
		self.password = "pw"
		self.name = "un"
		self.myGame = game

	# # User Inheritance:
	# def login(self, password, name) -> bool:
	# 	return self.password == password and self.name == name
	def list_commands(self) -> dict:
		return self.commands

	# Game Maker Specific:

	# def create_game(self):
	# 	self.myGame.start();
	# 	return self.myGame

	def create_landmark(self, name: str) -> bool:
		temp_landmark = Landmark(name)

		# temp_landmark.add_confirmation(question, answer)
		# temp_landmark.add_clue(clue, clue)

		self.myGame.landmarkList.append(temp_landmark)
		return True

	def edit_landmark_clue(self, name: str, new_clue: str) -> bool:
		temp_clue = StringClue(new_clue)
		self.myGame.get_landmark_by_name(name).set_clue(temp_clue)
		return True

	def edit_landmark_question(self, name: str, new_question: str, new_answer: str) -> bool:
		temp_question = StringQuestion(new_question, new_answer)
		self.myGame.get_landmark_by_name(name).set_confirmation(temp_question)
		return True

	def list_landmarks(self) -> str:
		string_list = None
		for i in self.myGame.landmarkList:
			string_list += ''.join(self.myGame.landmarkList[i].name)
		return string_list

	def create_team(self, name: str, password: str) -> bool:
		temp_user = User
		return False

	# def create_scavenger_hunt(self):
	# 	pass

	# def add_landmark_to_scavenger_hunt(self):
	# 	pass

	def end_game(self) -> bool:
		self.myGame.stop()
		return True
