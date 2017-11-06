from Clue import Clue
from Confirmation import Confirmation
from LandmarkGame import LandmarkGame
from LandmarkGameMaker import LandmarkGameMaker


class Landmark(LandmarkGameMaker, LandmarkGame):

	clues = {}
	confirmations = {}

	def __init__(self, name, clue, question, answer):
		self.name = name
		self.clue = clue
		self.question = question
		self. answer = answer

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
