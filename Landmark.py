from Clue import Clue
from Confirmation import Confirmation
from LandmarkGame import LandmarkGame
from LandmarkGameMaker import LandmarkGameMaker


class Landmark(LandmarkGameMaker, LandmarkGame):


	def __init__(self, name):
		self.clue = None
		self.confirmation = None
		self.name = name

	def add_confirmation(self, confirmation: Confirmation):
		pass

	def add_clue(self, clue: Clue):
		pass

	def get_confirmation(self):
		return self.confirmations.get("Confirmation").display()

	def get_clue(self):
		pass

	def check_answer(self, string: str) -> bool:
		return self.confirmations.get("Confirmation").validate()
