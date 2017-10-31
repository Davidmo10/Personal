from abc import ABC


class GameGameMaker(ABC):
	def start(self):
		pass

	def stop(self):
		pass

	def get_landmarks(self)->dict:
		pass

	def add_landmark(self):
		pass