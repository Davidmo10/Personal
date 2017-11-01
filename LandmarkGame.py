from abc import ABC


class LandmarkGame(ABC):

	def get_clue(self):
		pass

	def get_confirmation(self):
		pass

	def check_answer(self, string: str) -> bool:
		pass