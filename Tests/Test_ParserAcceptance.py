import unittest
from Parser import Parser
from Game import Game


class ParserAcceptanceGameMaker(unittest.TestCase):

	def setUp(self):
		self.parser = Parser(Game())

	def test_login(self):
		self.assertEqual(self.parser.parse("login maker password"), "Logged in!", "Did not log in")

	def test_logout(self):
		self.parser.parse("login maker password")
		self.assertEqual(self.parser.parse("logout"), "Success!", "Did not log out")

	def test_create_team(self):
		self.parser.parse("login maker password")
		self.assertEqual(self.parser.parse("createteam TestTeam SecretPassword"), "Success!", "Did not create team")

	def test_create_landmark(self):
		self.parser.parse("login maker password")
		self.assertEqual(self.parser.parse("createlandmark TestLandmark"), "Success!", "Did not create landmark")

	def test_edit_landmark_clue(self):
		self.parser.parse("login maker password")
		self.parser.parse("createlandmark TestLandmark")
		self.assertEqual(self.parser.parse("landmarkclue TestLandmark TestClue"), "Success!", "Did not create/edit clue")

	def test_edit_landmark_question(self):
		self.parser.parse("login maker password")
		self.parser.parse("createlandmark TestLandmark")
		self.assertEqual(
			self.parser.parse("landmarkquestion TestLandmark TestQuestion TestAnswer"), "Success!", "Did not create/edit"
			" question")

	def test_start_game(self):
		self.parser.parse("login maker password")
		self.assertEqual(self.parser.parse("startgame"), "Success!", "Did not start game")

	# def test_list_commands(self):
	# 	 Not part of sprint
	# 	 self.parser.parse("commands")

	def test_end_game(self):
		self.parser.parse("login maker password")
		self.parser.parse("startgame")
		self.assertEqual(self.parser.parse("endgame"), "Success!", "did not end game")

	def test_list_landmarks(self):
		# Not going to enforce list structure, so just calling it.
		self.parser.parse("login maker password")
		self.parser.parse("createlandmark TestLandmark")
		self.parser.parse("createlandmark TestLandmark2")
		self.parser.parse("listlandmarks")


class ParserAcceptanceTeam(unittest.TestCase):

	def setUp(self):
		self.parser = Parser(Game())
		self.parser.parse("login maker password")
		self.parser.parse("createteam TeamName TeamPass")

		self.parser.parse("createlandmark TestLandmark")
		self.parser.parse("landmarkclue TestLandmark TestClue")
		self.parser.parse("landmarkquestion TestLandmark TestQuestion TestAnswer")

		self.parser.parse("createlandmark TestLandmark2")
		self.parser.parse("landmarkclue TestLandmark2 TestClue2")
		self.parser.parse("landmarkquestion TestLandmark2 TestQuestion2 TestAnswer2")

		self.parser.parse("startgame")
		self.parser.parse("logout")

	def test_login(self):
		self.assertEqual(self.parser.parse("login TeamName TeamPass"), "Logged in!", "Did not log in")

	def test_logout(self):
		self.parser.parse("login TeamName TeamPass")
		self.assertEqual(self.parser.parse("logout"), "Success!", "Did not log out")

	def test_request_clue(self):
		self.parser.parse("login TeamName TeamPass")
		self.assertEqual(self.parser.parse("getclue"), "TestClue", "Did not return clue")

	def test_request_question(self):
		self.parser.parse("login TeamName TeamPass")
		self.assertEqual(self.parser.parse("getquestion"), "TestQuestion", "Did not return question")

	def test_answer(self):
		self.parser.parse("login TeamName TeamPass")
		self.parser.parse("getquestion")
		self.assertEqual(self.parser.parse("answer TestAnswer"), "Success!", "Did not process answering")

	# def test_list_commands(self):
	# 	# NOt part of sprint
	# 	self.parser.parse("login TeamName TeamPass")
	# 	self.parser.parse("listcommands")

	def test_forfeit(self):
		self.parser.parse("login TeamName TeamPass")
		self.assertEqual(self.parser.parse("forfeit"), "Success!", "Did not forfeit game")
