from Clue import Clue


class StringClue(Clue):
	def __init__(self, string=None):
		if string is None:
			raise ValueError('Must specify clue during instantiation')  # Placeholder
		self.clue = string

	def display(self) -> str:
		return self.clue

