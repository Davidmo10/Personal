from GameGameMaker import GameGameMaker
from GameTeam import GameTeam
from Landmark import Landmark


class Game(GameGameMaker, GameTeam):

	on = False
	myUserDict = {}
	myLandmarkDict = {}

	def start(self):
		self.on = True
		return self

	def stop(self):
		self.on = False
		return self

	def get_landmarks(self) -> dict:
		return self.myLandmarkDict

	def add_landmark(self, Landmark):		
		self.myLandmarkDict = self.myLandmarkDict + Landmark	#This will need to be changed
		return true
		
	def get_clue(self, index: int):
		pass

	def get_question(self, index: int):
		return self.myLandmarkDict[index].get_confirmation()

	def check_answer(self, index: int, answer: str):
		return self.myLandmarkDict[index].check_answer(answer)
