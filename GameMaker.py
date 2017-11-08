from Game import Game
from Landmark import Landmark
from StringClue import StringClue
from StringQuestion import StringQuestion
from Team import Team
from User import User


class GameMaker(User):
	def __init__(self, game: Game):
		super().__init__()
		self.commands = {"createlandmark": lambda name: self.create_landmark(name),
		                 "createteam": lambda name, password: self.create_team(name,password),
		                 "landmarkclue": lambda name, clue: self.edit_landmark_clue(name, clue),
		                 "landmarkquestion": lambda name, question, answer: self.edit_landmark_question(name, question, answer),
		                 "endgame": lambda: self.end_game(),
		                 "startgame": lambda: self.start_game(),
		                 "listlandmarks": lambda: self.list_landmarks()}  # dict
		self.password = None
		self.name = None
		self.myGame = game
		self.myTeams = {}

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
		string_list = ""
		for i in self.myGame.landmarkList:
			string_list += f"- {i.name}\t{i.get_clue}\n"
		return string_list

	def create_team(self, name: str, password: str) -> bool:
		team = Team(name, password, self.game)
		self.game.myUserDict[team.name] = team
		return True

	# def create_scavenger_hunt(self):
	# 	pass

	# def add_landmark_to_scavenger_hunt(self):
	# 	pass

	def end_game(self) -> bool:
		self.myGame.stop()
		return True
