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


class ParserTest(TestCase):
	def setUp(self):
		self.par = Parser()
		self.user = MockUser()

	def test_set_user(self):
		self.par.setUser(self.user)
		self.assertEqual(self.par.user, self.user, "Should be able to set user")
		self.assertEqual(self.par.commandsDict, self.user.list_commands(), "setting user should set commands dict")

	def test_empty_call(self):
		self.par.commandsDict = self.user.list_commands()
		self.assertEqual(self.par.parse("two"), "2")

	def test_argument_call(self):
		self.par.commandsDict = self.user.list_commands()
		self.assertEqual(self.par.parse("arg foo"), "foo", "a command with an argument doesn't pass correctly")

	def test_argument_quantity_low(self):
		# test like last one but don't have anything after arg
		pass

	def test_argument_quantity_high(self):
		# test like last one but have many things after arg; should just ignore everything but first arg
		pass

	def test_invalid_command(self):
		self.par.commandsDict = self.user.list_commands()
		self.assertEqual(self.par.parse("s"), "You can't access that command", "invalid command shouldn't pass")