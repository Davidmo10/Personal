from inspect import signature


class Parser:
	def __init__(self):
		self.user = None
		self.commandsDict = {}

	def parse(self, command: str) -> str:
		tokens = command.split(" ")
		args_list = tokens[1:]

		if tokens[0] not in self.commandsDict.keys():
			return "You can't access that command"

		command = self.commandsDict[tokens[0]]
		if not callable(command):
			return str(command)

		args_required = len(signature(command).parameters)  # Number of args required for command
		if len(args_list) < args_required:
			return "Please add more arguments to that command"

		command_args = args_list[0:args_required]

		return str(command(*command_args))
