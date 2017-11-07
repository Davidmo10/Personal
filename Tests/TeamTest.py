import unittest

from Game import Game
from Landmark import Landmark
from StringQuestion import StringQuestion
from Team import Team


class TestTeamConfirmation(unittest.TestCase):

	def setUp(self):
		self.MyGame = Game()
		self.myTeam = Team(self.MyGame)

	def test_getQuestion(self):
		self.assertEqual(
			self.team.request_question(), "What color is the car?", "Returned: " + self.landmark.get_confirmation()
			+ " instead of proper question")

	def test_answerWithoutGetQuestion(self):
		with self.assertRaises(Exception):
			self.team.answer("Red")

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
