from abc import ABC, abstractmethod


class Confirmation(ABC):
	@abstractmethod
	def validate(self, Object):
		pass

	@abstractmethod
	def display(self):
		pass
