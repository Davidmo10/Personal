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
		return str(command(args_list[1]))