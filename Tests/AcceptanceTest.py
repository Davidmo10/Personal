import unittest
from Parser import Parser


class ParserAcceptanceGameMaker(unittest.TestCase):

	def setUp(self):
		self.parser = Parser()

	def test_login(self):
		self.assertEqual(self.parser.parse("login un pw"), "Logged in", "Did not log in")

	def test_logout(self):
		self.assertEqual(self.parser.parse("logout"), "Logged out", "Did not log out")

	def test_create_team(self):
		self.assertEqual(self.parser.parse("maketeam TestTeam SecretPassword"), "Team created", "Did not create team")

	def test_create_landmark(self):
			self.assertEqual(self.parser.parse("CreateLandmark TestLandmark"), "Success!", "Did not create landmark")

	def test_edit_landmark_clue(self):
		pass

	def test_edit_landmark_question(self):
		pass

	def test_create_game(self):
		pass

	def test_add_landmark(self):
		pass

	def test_start_game(self):
		pass

	def test_list_commands(self):
		pass

	def test_end_game(self):
		pass

	def test_list_landmarks(self):
		pass


class ParserAcceptanceTeam(unittest.TestCase):

	def setUp(self):
		self.parser = Parser()

	def test_login(self):
		pass

	def test_logout(self):
		pass

	def test_request_clue(self):
		pass

	def test_request_question(self):
		pass

	def test_list_commands(self):
		pass

	def test_answer(self):
		pass

	def test_forfeit(self):
		pass

