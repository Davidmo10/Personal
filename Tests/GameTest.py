import unittest
from Game import Game
from StringQuestion import StringQuestion
from Landmark import Landmark


class TestGameConfirmation(unittest.TestCase):

	def setUp(self):
		self.string_question = StringQuestion("What color is the car?", "Red")
		self.landmark = Landmark()
		self.landmark.confirmation["Confirmation"] = self.string_question

		self.string_question2 = StringQuestion("What is written on the board?", "Hello")
		self.landmark2 = Landmark()
		self.landmark2.confirmation["Confirmation"] = self.string_question2

		self.game = Game()
		self.game.landmarkList[0] = self.landmark
		self.game.landmarkList[1] = self.landmark2
		pass

	def test_start(self):
		self.assertTrue(self.game.start(), "Game not started")

	def test_stop(self):
		self.assertFalse(self.game.start(), "Game Still On")

	def test_get_landmarks(self):
		self.assertEquals(isinstance(self.game.get_landmarks(), list), "get_landmarks() did not return a list")

	def test_add_landmark(self):
		self.lm_test = Landmark()
		self.assertTrue(self.game.add_landmark(self.lm_test), "add_landmark cannot successfully add a landmark to your game")

	# Would require mocking which we have not learned yet
	# Waiting to implement this test
	#
	# def test_get_clue(self):
	# 	self.assertEquals()

	

	# The following tests were implemented with a mock trial
	# Unsure if the code is correct - left implementations
	#
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
