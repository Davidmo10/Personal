from abc import ABC, abstractmethod


class Confirmation(ABC):
	@abstractmethod
	def validate(self):
		pass

	@abstractmethod
	def display(self):
		pass
