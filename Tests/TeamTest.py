import unittest

from Game import Game
from Landmark import Landmark
from StringQuestion import StringQuestion
from StringClue import StringClue
from Team import Team


class TestTeamConfirmation(unittest.TestCase):

	def setUp(self):
		self.MyGame = Game()
		self.myTeam = Team(self.MyGame)
		self.landmark = Landmark()
		self.tempQuestion = StringQuestion("question", "answer")
		self.tempClue = StringClue("clue")
		self.landmark.confirmation = self.tempQuestion

	def test_getQuestion(self):
		self.assertEqual(self.myTeam.request_question(), self.tempQuestion, "Can not retrieve proper Question ")

	def test_answerWithoutGetQuestion(self):
		with self.assertRaises(Exception):
			self.myTeam.answer()

	def test_answerCorrect(self):
		self.assertTrue(self.team.answer("Red"), "Did not accept correct answer")

	def test_answerIncorrect(self):
		self.assertFalse(self.team.answer("Blue"), "Accepted incorrect answer")

	def test_landmarkIdAfterIncorrect(self):
		self.team.request_question()
		self.team.answer("Blue")
		self.assertEqual(self.team.landmark, 0, "Landmark id was incremented despite incorrect answer")

	def test_landmarkIdAfterCorrect(self):
		self.team.request_question()
		self.team.answer("Red")
		self.assertEqual(self.team.landmark, 1, "Landmark id was not incremented despite correct answer")
		

class TestTeam(unittest.TestCase):

	def setUp(self):
		self.TM = Team()
		self.GA = Game()

	def test_forfeit(self):
		if self.assertTrue(self.GA.start):
			self.assertTrue(self.TM.forfeit, "The game was successfully forfeited")
