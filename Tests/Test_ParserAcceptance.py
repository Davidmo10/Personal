import unittest
from Parser import Parser


class ParserAcceptanceGameMaker(unittest.TestCase):

	def setUp(self):
		self.parser = Parser()

	def test_login(self):
		self.assertEqual(self.parser.parse("login un pw"), "Success!", "Did not log in")

	def test_logout(self):
		self.assertEqual(self.parser.parse("logout"), "Success!", "Did not log out")

	def test_create_team(self):
		self.assertEqual(self.parser.parse("maketeam TestTeam SecretPassword"), "Success!", "Did not create team")

	def test_create_landmark(self):
		self.assertEqual(self.parser.parse("createlandmark TestLandmark"), "Success!", "Did not create landmark")

	def test_edit_landmark_clue(self):
		self.parser.parser("createlandmark TestLandmark")
		self.assertEqual(self.parser.parse("landmarkclue TestLandmark TestClue"), "Success!", "Did not create/edit clue")

	def test_edit_landmark_question(self):
		self.parser.parse("createlandmark TestLandmark")
		self.assertEqual(
			self.parser.parse("landmarkquestion TestLandmark TestQuestion TestAnswer"), "Success!", "Did not create/edit"
			" question")

	def test_start_game(self):
		self.assertEqual(self.parser.parse("startgame"), "Success!", "Did not start game")

	def test_list_commands(self):
		# Don't know how to assert here, but don't want to stop the tests because it "Fails"
		self.parser.parse("commands")

	def test_end_game(self):
		self.assertEqual(self.parser.parse("endgame"), "Success!", "dud not end game")

	def test_list_landmarks(self):
		self.parser.parse("createlandmark TestLandmark")
		self.parser.parse("createlandmark TestLandmark2")
		self.assertEqual(self.parser.parse("listlandmarks"), "TestLandmark, TestLandmark2", "Did not list landmarks")


class ParserAcceptanceTeam(unittest.TestCase):

	def setUp(self):
		self.parser = Parser()
		self.parser.parser("login un pe")
		self.parser.parse("maketeam TeamName TeamPass")

		self.parser.parse("createlandmark TestLandmark")
		self.parser.parse("landmarkclue TestLandmark TestClue")
		self.parser.parse("landmarkquestion TestLandmark TestQuestion TestAnswer")

		self.parser.parse("createlandmark TestLandmark2")
		self.parser.parse("landmarkclue TestLandmark2 TestClue2")
		self.parser.parse("landmarkquestion TestLandmark2 TestQuestion2 TestAnswer2")

		self.parser.parse("startgame")
		self.parser.parse("logout")

	def test_login(self):
		self.assertEqual(self.parser.parse("login TeamName TeamPass"), "Success!", "Did not log in")

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

	def test_list_commands(self):
		# Also don't want to stop the tests here, so not asserting
		self.parser.parse("login TeamName TeamPass")
		self.parser.parse("listcommands")

	def test_forfeit(self):
		self.parser.parse("login TeamName TeamPass")
		self.assertEqual(self.parser.parse("forfeit"), "Success!", "Did not forfeit game")
