from unittest import TestCase

from Game import Game
from GameMaker import GameMaker
from Parser import Parser


class MockUser:
	@staticmethod
	def returns_two():
		return 2

	def returns_arg(self, arg):
		return arg

	def returns_bool(self, i):
		return int(i) == 1

	def list_commands(self) -> dict:
		ret = {'two': self.returns_two(), 'arg': (lambda arg: self.returns_arg(arg)), "retTru": (lambda i: self.returns_bool(i))}
		return ret


class ParserTest(TestCase):
	def setUp(self):
		self.par = Parser(Game())
		self.user = MockUser()

	def test_empty_call(self):
		self.par.commandsDict = self.user.list_commands()
		self.assertEqual(self.par.parse("two"), "2")

	def test_argument_call(self):
		self.par.commandsDict = self.user.list_commands()
		self.assertEqual(self.par.parse("arg foo"), "foo", "a command with an argument doesn't pass correctly")

	def test_argument_quantity_low(self):
		self.par.commandsDict = self.user.list_commands()
		self.assertEqual(self.par.parse("arg"), "Please add more arguments to that command", "a command that requires an argument should alert the user they need an argument")
		pass

	def test_argument_quantity_high(self):
		self.par.commandsDict = self.user.list_commands()
		self.assertEqual(self.par.parse("arg foo aaaaa bar"), "foo", "a command too many arguments ignores extra args")
		pass

	def test_invalid_command(self):
		self.par.commandsDict = self.user.list_commands()
		self.assertEqual(self.par.parse("s"), "You can't access that command", "invalid command shouldn't pass")

	def test_bool_return_true(self):
		self.par.commandsDict = self.user.list_commands()
		self.assertEqual(self.par.parse("retTru 1"), "Success!", "return of true shouldn't just be true string")

	def test_bool_return_fail(self):
		self.par.commandsDict = self.user.list_commands()
		self.assertEqual(self.par.parse("retTru 0"), "A problem occurred", "boolean return shouldn't just be 'false'")

	def test_quoted_args(self):
		self.par.commandsDict = self.user.list_commands()
		self.assertEqual(self.par.parse("arg \"this is a test\""), "this is a test", "Arguments in quotes should be collected")


class LoginTests(TestCase):
	def setUp(self):
		self.par = Parser(Game())

	def test_set_user(self):
		self.par.parse("login maker password")
		self.assertTrue(isinstance(self.par.user, GameMaker), "Should be able to login")
		self.assertNotEqual(self.par.commandsDict, {"login": (lambda u, p: self._login(u, p))}, "setting user should change commands dict from login")


class LogoutTests(TestCase):
	def setUp(self):
		self.par = Parser(Game())

	def test_logout_no_user(self):
		self.assertEqual(self.par.parse("logout"), "You can't access that command", "Shouldn't be able to log out until logged in")

	def test_logout_user(self):
		self.par.parse("login maker password")
		self.par.parse("logout")
		self.assertEqual(self.par.user, None, "user should be reset")

	def test_logout_game_maker(self):
		self.par.parse("login maker password")
		self.par.parse("logout")
		self.assertEqual(self.par.parse("mklm a b c"), "You can't access that command", "logout should clear commands dict")