from Game import Game
from Parser import Parser


# Loads saved data from a .game file (Separate class?) - A later sprint
# Then just gets input, passes the input as a string to the parser, then prints the response
# Exports saved data when done - Also later


def main_loop():
	parser = Parser(Game())

	print("*"*10, "WELCOME TO E-SCAVENGE", "*"*10)
	print(" "*5, '\n', "Go ahead, find that landmark...all the cool kids are doing it\n")
	while True:
		parser.print_commands()
		user_response = input(">")
		print(parser.parse(user_response))


if __name__ == '__main__':
	main_loop()