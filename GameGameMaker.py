from abc import ABC, abstractmethod


class GameGameMaker(ABC):
	
	@abstractmethod
	def start(self):
		pass
	
	@abstractmethod
	def stop(self):
		pass
	
	@abstractmethod
	def get_landmarks(self)->dict:
		pass
	
	@abstractmethod
	def add_landmark(self):
		pass
