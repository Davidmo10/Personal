from GameGameMaker import GameGameMaker
from Landmark import Landmark
from StringClue import StringClue
from StringQuestion import StringQuestion
from Team import Team
from User import User


class GameMaker(User):
	# noinspection PyPep8,PyPep8,PyPep8,PyPep8,PyPep8,PyPep8,PyPep8
	def __init__(self, game: GameGameMaker):
		super().__init__()
		self.commands = {"createlandmark": lambda name: self.create_landmark(name),
		                 "createteam": lambda name, password: self.create_team(name, password),
		                 "landmarkclue": lambda name, clue: self.edit_landmark_clue(name, clue),
		                 "landmarkquestion": lambda name, question, answer: self.edit_landmark_question(name, question,
		                                                                                                answer),
		                 "endgame": lambda: self.end_game(),
		                 "startgame": lambda: self.start_game(),
		                 "listlandmarks": lambda: self.list_landmarks()}  # dict
		self.password = None
		self.name = None
		self.myGame = game

	# # User Inheritance:
	# def login(self, password, name) -> bool:
	# 	return self.password == password and self.name == name
	def list_commands(self) -> dict:
		return self.commands

	def start_game(self) -> bool:
		self.myGame.start()
		return self.myGame.is_on()

	# Game Maker Specific:

	# def create_game(self):
	# 	self.myGame.start();
	# 	return self.myGame

	def create_landmark(self, name: str) -> bool:
		if(self.myGame.get_landmark_by_name(name) != None):
			return False
		temp_landmark = Landmark(name)
		self.myGame.landmarkList.append(temp_landmark)
		return True

	def edit_landmark_clue(self, name: str, new_clue: str) -> bool:
		temp_clue = StringClue(new_clue)
		lm = self.myGame.get_landmark_by_name(name)
		if lm is None:
			return False
		lm.set_clue(temp_clue)
		return True

	def edit_landmark_question(self, name: str, new_question: str, new_answer: str) -> bool:
		temp_question = StringQuestion(new_question, new_answer)
		lm = self.myGame.get_landmark_by_name(name)
		if lm is None:
			return False
		lm.set_confirmation(temp_question)
		return True

	def list_landmarks(self) -> str:
		string_list = ""
		for i in self.myGame.landmarkList:
			string_list += f"- {i.name}\t{i.get_clue()}\n"
		return string_list

	def create_team(self, name: str, password: str) -> bool:
		if self.myGame.has_user_by_name(name):
			return False
		team = Team(name, password, self.myGame)
		self.myGame.myUserDict.append(team)
		return True


	# def create_scavenger_hunt(self):
	# 	pass

	# def add_landmark_to_scavenger_hunt(self):
	# 	pass

	def end_game(self) -> bool:
		self.myGame.stop()
		return True
