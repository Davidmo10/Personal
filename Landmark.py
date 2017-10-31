from Clue import Clue
from Confirmation import Confirmation
from LandmarkGame import LandmarkGame
from LandmarkGameMaker import LandmarkGameMaker


class Landmark(LandmarkGameMaker, LandmarkGame):

	clues = {}

	confirmations = {}

	def add_confirmation(self, confirmation: Confirmation):
		pass

	def add_clue(self, clue: Clue):
		pass

	def get_confirmation(self):
		pass

	def get_clue(self):
		pass

	def check_answer(self, string: str) -> bool:
		pass