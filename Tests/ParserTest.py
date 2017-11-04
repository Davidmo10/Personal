from unittest import TestCase

from Parser import Parser


class MockUser:
	@staticmethod
	def returns_two():
		return 2

	def returns_arg(self, arg):
		return arg

	def list_commands(self) -> dict:
		ret = {'two': self.returns_two(), 'arg': (lambda arg: self.returns_arg(arg))}  # TODO: Figure out lambdas
		return ret


class TestParser(TestCase):
	def setUp(self):
		self.par = Parser()
		self.user = MockUser()

	def test_set_user(self):
		self.par.parse("login user test")
		self.assertEqual(self.par.user, self.user, "Should be able to login")
		self.assertEqual(self.par.commandsDict, self.user.list_commands(), "setting user should set commands dict")

	def test_empty_call(self):
		self.par.commandsDict = self.user.list_commands()
		self.assertEqual(self.par.parse("two"), "2")

	def test_argument_call(self):
		self.par.commandsDict = self.user.list_commands()
		self.assertEqual(self.par.parse("arg foo"), "foo", "a command with an argument doesn't pass correctly")

	def test_argument_quantity_low(self):
		self.par.commandsDict = self.user.list_commands()
		self.assertEqual(self.par.parse("arg"), "Please add an argument to that command", "a command that requires an argument should alert the user they need an argument")

	def test_argument_quantity_high(self):
		self.par.commandsDict = self.user.list_commands()
		self.assertEqual(self.par.parse("arg foo aaaaa bar"), "foo", "a command too many arguments ignores extra args")
		pass

	def test_invalid_command(self):
		self.par.commandsDict = self.user.list_commands()
		self.assertEqual(self.par.parse("s"), "You can't access that command", "invalid command shouldn't pass")