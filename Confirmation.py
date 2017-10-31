from abc import ABC, abstractmethod


class Confirmation(ABC):
	@abc.abstractmethod
	def validate(self):
		pass

	@abc.abstractmethod
	def display(self):
		pass
