from abc import ABC, abstractmethod


class Clue(ABC):
	@abc.abstractmethod
	def display(self):
		pass
	
