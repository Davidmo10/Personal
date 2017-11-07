from Confirmation import Confirmation


class StringQuestion(Confirmation):
	def __init__(self, question=None, confirmation=None):
		if question is None or confirmation is None:
			raise ValueError('Missing question and clue')  # Placeholder

		self.question = question
		self.confirmation = confirmation

	def validate(self, answer):
		if answer is self.confirmation:
			return True
		return False

	def display(self):
		return self.question
