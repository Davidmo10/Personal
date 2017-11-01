from GameGameMaker import GameGameMaker
from GameTeam import GameTeam
from Landmark import Landmark


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
		return self.myLandmarkDict[int].get_confirmation()

	def check_answer(self, index: int, answer: str):
		return self.myLandmarkDict[int].check_answer()