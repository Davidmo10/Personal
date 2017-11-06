import unittest
from Game import Game
from StringQuestion import StringQuestion
from Landmark import Landmark


class TestGameConfirmation(unittest.TestCase):

	def setUp(self):
		self.string_question = StringQuestion("What color is the car?", "Red")
		self.landmark = Landmark()
		self.landmark.confirmations["Confirmation"] = self.string_question

		self.string_question2 = StringQuestion("What is written on the board?", "Hello")
		self.landmark2 = Landmark()
		self.landmark2.confirmations["Confirmation"] = self.string_question2

		self.game = Game()
		self.game.myLandmarkDict[0] = self.landmark
		self.game.myLandmarkDict[1] = self.landmark2
		pass

	def test_getQuestion(self):
		self.assertEqual(
			self.game.get_question(0), "What color is the car?", "Returned: " + self.landmark.get_confirmation()
			+ " instead of proper question")

	def test_getQuestion2(self):
		self.assertEqual(
			self.game.get_question(1), "What is written on the board?", "Returned: " + self.landmark.get_confirmation()
			+ " instead of proper question")

	def test_answerCorrect(self):
		self.assertTrue(self.game.check_answer(0, "Red"), "Did not accept correct answer")

	def test_answerIncorrect(self):
		self.assertFalse(self.game.check_answer(0, "Blue"), "Accepted incorrect answer")
