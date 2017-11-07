from abc import ABC


class GameTeam(ABC):
	def is_on(self)-> bool:
		pass

	def get_clue(self, index: int):
		pass

	def get_question(self, index: int):
		pass

	def check_answer(self, index: int, answer: str):
		pass
