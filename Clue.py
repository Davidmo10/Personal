from abc import ABC, abstractmethod


class Clue(ABC):
	@abstractmethod
	def display(self):
		pass
	
