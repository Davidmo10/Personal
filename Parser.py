import shlex
from inspect import signature

from Game import Game
from UserFactory import UserFactory


class Parser:
	def __init__(self, game: Game):
		self.user = None
		self.commandsDict = {"login": (lambda u, p: self._login(u, p))}
		self.game = game

	def parse(self, command: str) -> str:
		tokens = shlex.split(command)
		args_list = tokens[1:]

		if tokens[0] not in self.commandsDict.keys():
			return "You can't access that command"

		command = self.commandsDict[tokens[0]]
		if not callable(command):
			return self._parser_str(command)

		args_required = len(signature(command).parameters)  # Number of args required for command
		if len(args_list) < args_required:
			return "Please add more arguments to that command"

		command_args = args_list[0:args_required]

		return self._parser_str(command(*command_args))

	@staticmethod
	def _parser_str(o) -> str:
		if type(o) is bool:
			if o:
				return "Success!"
			else:
				return "A problem occurred"
		return str(o)

	def _login(self, username: str, password: str):
		self.user = UserFactory.make_user(username, password, self.game)
		self.commandsDict = self.user.list_commands()
		self.commandsDict["logout"] = lambda: self._logout()

	def _logout(self):
		self.user = None
		self.commandsDict = {"login": (lambda u, p: self._login(u, p))}