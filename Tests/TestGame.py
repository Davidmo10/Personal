import unittest

from Game import Game
from Landmark import Landmark
from StringQuestion import StringQuestion
from Team import Team


class TestGameConfirmation(unittest.TestCase):
	def setUp(self):
		self.string_question = StringQuestion("What color is the car?", "Red")
		self.landmark = Landmark("landmark1")
		self.landmark.confirmation = self.string_question

		self.string_question2 = StringQuestion("What is written on the board?", "Hello")
		self.landmark2 = Landmark("landmark2")
		self.landmark2.confirmation = self.string_question2

		self.game = Game()
		self.game.landmarkList.append(self.landmark)
		self.game.landmarkList.append(self.landmark2)
		pass

	def test_start(self):
		self.game.start()
		self.assertTrue(self.game.on, "Game not started")

	def test_stop(self):
		self.game.stop()
		self.assertFalse(self.game.on, "Game Still On")

	def test_get_landmarks(self):
		self.assertTrue(isinstance(self.game.get_landmarks(), list), "get_landmarks() did not return a list")

	def test_add_landmark(self):
		self.lm_test = Landmark("landmark3")
		self.assertTrue(self.game.add_landmark(self.lm_test),
		                "add_landmark cannot successfully add a landmark to your game")

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
			self.game.get_question(0), "What color is the car?", "Returned: " + str(self.landmark.get_confirmation())
			                                                     + " instead of proper question")

	def test_getQuestion2(self):
		self.assertEqual(
			self.game.get_question(1), "What is written on the board?",
			"Returned: " + str(self.landmark.get_confirmation().display())
			+ " instead of proper question")

	def test_answerCorrect(self):
		self.assertTrue(self.game.check_answer(0, "Red"), "Did not accept correct answer")

	def test_answerIncorrect(self):
		self.assertFalse(self.game.check_answer(0, "Blue"), "Accepted incorrect answer")

	def test_get_lm_by_name(self):
		self.assertEqual(self.game.get_landmark_by_name("landmark2"), self.landmark2,
		                 "Game couldn't retrieve landmark by name")

	def test_has_user_by_name(self):
		self.game.myUserDict.append(Team("foo", "bar", self.game))
		self.assertTrue(self.game.has_user_by_name("foo"), "Game couldn't find user by name")

	def test_get_user_index_by_name(self):
		self.game.myUserDict.append(Team("foo0", "bar", self.game))
		self.game.myUserDict.append(Team("foo1", "bar", self.game))
		self.game.myUserDict.append(Team("foo2", "bar", self.game))
		self.game.myUserDict.append(Team("foo3", "bar", self.game))
		self.game.myUserDict.append(Team("foo4", "bar", self.game))
		self.game.myUserDict.append(Team("foo5", "bar", self.game))
		self.assertTrue(self.game.get_user_index_by_name("foo3"), "Game couldn't get index of user by name")
