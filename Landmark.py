from Clue import Clue
# from StringQuestion import StringQuestion
from Confirmation import Confirmation
from LandmarkGame import LandmarkGame
from LandmarkGameMaker import LandmarkGameMaker


class Landmark(LandmarkGameMaker, LandmarkGame):

	def __init__(self, name):
		self.clue = None
		self.confirmation = None
		self.name = name

	def set_confirmation(self, confirmation: Confirmation) -> bool:
		self.confirmation = confirmation
		return True

	def set_clue(self, clue: Clue) -> bool:
		self.clue = clue
		return True

	def get_confirmation(self) -> Confirmation:
		return self.confirmation

	def get_clue(self) -> Clue:
		return self.clue

	def check_answer(self, string: str) -> bool:
		return self.get_confirmation() == string
