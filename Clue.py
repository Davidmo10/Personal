from abc import ABC


class Clue(ABC):
	
	@abc.abstractmethod
	def display(self):
		pass
	
