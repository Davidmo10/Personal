from abc import ABC, abstractmethod
from Landmark import Landmark


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
	def add_landmark(self, landmark: Landmark) -> bool:
		pass

	@abstractmethod
	def is_on(self) -> bool:
		pass

	@abstractmethod
	def get_landmark_by_name(self, name: str) -> Landmark:
		pass
