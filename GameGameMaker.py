from abc import ABC, abstractmethod


class GameGameMaker(ABC):

	def __init_subclass__(cls, **kwargs):
		pass
	
	@abstractmethod
	def start(self) -> bool:
		pass
	
	@abstractmethod
	def stop(self) -> bool:
		pass
	
	@abstractmethod
	def get_landmarks(self)-> dict:
		pass
	
	@abstractmethod
	def add_landmark(self) -> bool:
		pass
