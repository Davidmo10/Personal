from abc import ABC


class GameGameMaker(ABC):
	
	@abc.abstractmethod
	def start(self):
		pass
	
	@abc.abstractmethod
	def stop(self):
		pass
	
	@abc.abstractmethod
	def get_landmarks(self)->dict:
		pass
	
	@abc.abstractmethod
	def add_landmark(self):
		pass
