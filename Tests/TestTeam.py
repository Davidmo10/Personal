import unittest

from Game import Game
from Landmark import Landmark
from StringClue import StringClue
from StringQuestion import StringQuestion
from Team import Team


class TestTeamConfirmation(unittest.TestCase):
	def setUp(self):
		self.MyGame = Game()
		self.myTeam = Team("name", "pass", self.MyGame)
		self.myTeam.is_playing = True
		self.landmark = Landmark("Landmark One")
		self.tempQuestion = StringQuestion("question", "answer")
		self.tempClue = StringClue("clue")
		self.landmark.confirmation = self.tempQuestion
		self.MyGame.landmarkList.append(self.landmark)

	def test_getQuestion(self):
		self.assertEqual(self.myTeam.request_question(), str(self.tempQuestion.question), "Can not retrieve proper Question ")

	def test_answerWithoutGetQuestion(self):
		with self.assertRaises(Exception):
			self.myTeam.answer("something")

	def test_answerCorrect(self):
		self.myTeam.request_question()
		self.assertTrue(self.myTeam.answer("answer"), "Did not accept correct answer")

	def test_answerIncorrect(self):
		self.myTeam.request_question()
		self.assertFalse(self.myTeam.answer("Blue"), "Accepted incorrect answer")

	def test_landmarkIdAfterIncorrect(self):
		self.myTeam.request_question()
		self.myTeam.answer("Blue")
		self.assertEqual(self.myTeam.landmark_index, 0, "Landmark id was incremented despite incorrect answer")

	def test_landmarkIdAfterCorrect(self):
		self.myTeam.request_question()
		self.myTeam.answer("answer")
		self.assertEqual(self.myTeam.landmark_index, 1, "Landmark id was not incremented despite correct answer")


class TestTeam(unittest.TestCase):
	def setUp(self):
		self.GA = Game()
		self.TM = Team("name", "pass", self.GA)

	def test_forfeit(self):
		if self.assertTrue(self.GA.start):
			self.assertTrue(self.TM.forfeit, "The game was successfully forfeited")
