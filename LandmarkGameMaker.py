from abc import ABC

from Clue import Clue
from Confirmation import Confirmation


class LandmarkGameMaker(ABC):

	def set_confirmation(self, confirmation: Confirmation):
		pass

	def set_clue(self, clue: Clue):
		pass