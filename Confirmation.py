from abc import ABC, abstractmethod


class Confirmation(ABC):
	@abstractmethod
	def validate(self, obj: object) -> object:
		pass

	@abstractmethod
	def display(self) -> str:
		pass
