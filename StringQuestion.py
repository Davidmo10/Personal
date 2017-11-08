from Confirmation import Confirmation


class StringQuestion(Confirmation):
	def __init__(self, question=None, answer=None):
		if question is None or answer is None:
			raise ValueError('Missing question and clue')  # Placeholder

		self.question = question
		self.answer = answer

	def __str__(self):
			return "< StringQuestion :: " + self.question + ' , ' + self.answer + '>'

	def validate(self, answer: str) -> bool:
		return self.answer == answer

	def display(self) -> str:
		return self.question
