from GameGameMaker import GameGameMaker
from GameTeam import GameTeam


class Game(GameGameMaker, GameTeam):

	on = False
	myUserDict = {}
	myLandmarkDict = {}

	def start(self):
		pass

	def stop(self):
		pass

	def get_landmarks(self)->dict:
		pass

	def add_landmark(self):
		pass

	def get_clue(self, index: int):
		pass

	def get_question(self, index: int):
		pass

	def check_answer(self, index: int,answer: str):
		pass