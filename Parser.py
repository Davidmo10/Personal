from inspect import signature


class Parser:
	def __init__(self):
		self.user = None
		self.commandsDict = {}

	def parse(self, command: str) -> str:
		# TODO: fix up variable names
		args_list = command.split(" ")
		if args_list[0] not in self.commandsDict.keys():
			return "You can't access that command"

		command = self.commandsDict[args_list[0]]
		actual_args = args_list[1:]
		if not callable(command):
			return str(command)
		required_args = signature(command).parameters
		if (len(actual_args)) < len(required_args):
			return "Please add more arguments to that command"

		user_args = []
		for i in range(len(required_args)):
			user_args.append(actual_args[i])

		return str(command(*user_args))
