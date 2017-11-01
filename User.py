from abc import ABC


class User(ABC):

	def login(self):
		pass

	def logout(self):
		pass

	def list_commands(self):
		pass