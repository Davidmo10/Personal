from abc import ABC, abstractmethod


class GameGameMaker(ABC):
	
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
