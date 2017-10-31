from abc import ABC


class Confirmation(ABC):
	
	@abc.abstractmethod
	def display(self):
		pass
	
	@abc.abstractmethod
	def validate(self):
		pass
