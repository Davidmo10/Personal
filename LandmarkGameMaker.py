from abc import ABC

from Clue import Clue
from Confirmation import Confirmation


class LandmarkGameMaker(ABC):

	def add_confirmation(self, confirmation: Confirmation):
		pass

	def add_clue(self, clue: Clue):
		pass