from GameGameMaker import GameGameMaker
from GameMaker import GameMaker
from GameTeam import GameTeam
from Landmark import Landmark
from User import User


class Game(GameGameMaker, GameTeam):
	def __init__(self):
		self.on = False
		maker = GameMaker(self)
		maker.name = "maker"
		maker.password = "password"

		self.myUserDict = [maker]
		self.landmarkList = []

	def start(self) -> bool:
		self.on = True
		return self.on

	def stop(self) -> bool:
		self.on = False
		return self.on

	def get_landmarks(self) -> list:
		return self.landmarkList

	def add_landmark(self, landmark: Landmark) -> bool:
		self.landmarkList.append(Landmark)
		return True
		
	def get_clue(self, index: int):
		return self.landmarkList[index].get_clue().display()

	def get_question(self, index: int):
		return self.landmarkList[index].get_confirmation().display()

	def check_answer(self, index: int, answer: str):
		return self.landmarkList[index].check_answer(answer)

	def get_landmark_by_name(self, name) -> Landmark:
		for i in self.landmarkList:
			if i.get_name() == name:
				return i

	def is_on(self):
		return self.on

	def has_user_by_name(self, name: str) -> bool:
		return any(u.name == name for u in self.myUserDict)

	def get_user_index_by_name(self, search_for: str) -> int:
		for i in range(len(self.myUserDict)):
			if self.myUserDict[i].name == search_for:
				return i
		return -1

	def get_maker(self):
		return self.myUserDict[0]

	def get_user_by_name(self, search_for: str) -> User:
		for i in range(len(self.myUserDict)):
			if self.myUserDict[i].name == search_for:
				return self.myUserDict[i]