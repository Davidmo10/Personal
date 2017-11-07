from GameGameMaker import GameGameMaker
from GameTeam import GameTeam
from Landmark import Landmark


class Game(GameGameMaker, GameTeam):
	def __init__(self):
		self.on = False
		self.myUserDict = []
		self.landmarkList = []

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
		return self.landmarkList[index].get_confirmation()

	def check_answer(self, index: int, answer: str):
		return self.landmarkList[index].check_answer(answer)

	def get_landmark_by_name(self, name) -> Landmark:
		for i in self.landmarkList:
			if i.name == name:
				return i
