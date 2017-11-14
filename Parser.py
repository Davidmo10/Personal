import shlex
from inspect import signature

from Game import Game
from UserFactory import UserFactory
from errors import LoginError

testing = False


class Parser:
	def __init__(self, game: Game):
		self.user = None
		self.commandsDict = {"login": (lambda username, password: self._login(username, password)),
							 "exit": (lambda: self.exit_game())}
		self.game = game

	def parse(self, command: str) -> str:
		try:
			tokens = shlex.split(command)
		except ValueError:
			return "Please end your quotations"

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

	def _login(self, username: str, password: str) -> str:
		try:
			self.user = UserFactory.make_user(username, password, self.game)
		except LoginError as err:
			if testing:
				return str(err.user)
			else:
				return "Unable to login as " + username
		self.commandsDict = self.user.list_commands()
		self.commandsDict["logout"] = lambda: self._logout()
		return "Logged in!"

	def _logout(self) -> bool:
		self.user = None
		self.commandsDict = {"login": (lambda username, password: self._login(username, password))}
		return True

	def print_commands(self) -> None:
		print("Available Commands:")
		for c in self.commandsDict:
			arg_string = str(signature(self.commandsDict[c]))
			if arg_string == "()":
				arg_string = "";
			else:
				arg_string = arg_string.replace("(", "<")
				arg_string = arg_string.replace(", ", "> <")
				arg_string = arg_string.replace(")", ">")
			print("  - ", c, arg_string)

	def exit_game(self) -> None:
		print("\nSee you at you the next site!", end="\n\n")
		exit(0)