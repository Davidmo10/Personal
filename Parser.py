from inspect import signature


class Parser:
	def __init__(self):
		self.user = None
		self.commandsDict = {}

	def parse(self, command: str) -> str:
		args_list = command.split(" ")
		if args_list[0] not in self.commandsDict.keys():
			return "You can't access that command"

		command = self.commandsDict[args_list[0]]
		if not callable(command):
			return str(command)
		required_args = signature(command).parameters
		if (len(args_list)-1) < len(required_args):
			return "Please add more arguments to that command"
		if len(required_args) is 1:
			return str(command(args_list[1]))
		elif len(required_args) is 2:
			return str(command(args_list[1],args_list[2]))
		elif len(required_args) is 3:
			return str(command(args_list[1],args_list[2],args_list[3]))
		elif len(required_args) is 4:
			pass
		else:
			return "this is a switch statement, and you've exceeded the max number of args"
