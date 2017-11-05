from abc import ABC, abstractmethod


class Confirmation(ABC):
	@abstractmethod
	def validate(self, obj: object):
		pass

	@abstractmethod
	def display(self):
		pass
