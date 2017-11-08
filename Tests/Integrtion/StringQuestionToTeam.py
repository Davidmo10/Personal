import unittest
from Team import Team
from Game import Game
from Landmark import Landmark
from StringQuestion import StringQuestion


class TestTeamToStringQuestion(unittest.TestCase):

	def setUp(self):
		self.string_question = StringQuestion("What color is the car?", "Red")
		self.landmark = Landmark("bobTheBuilderMuseum")
		self.landmark.confirmation = self.string_question
		self.game = Game()
		self.game.landmarkList[0] = self.landmark
		self.team = Team("name", "Password", self.game)
		self.team.game = self.game

	def test_get_question(self):
		self.assertEqual(
			self.team.request_question(), "What color is the car?", "Returned: " + str(self.landmark.get_confirmation())
			+ " instead of proper question")

	def test_answer_without_get_question(self):
		with self.assertRaises(Exception):
			self.team.answer("Red")

	def test_answer_correct(self):
		self.team.request_question()
		self.assertTrue(self.team.answer("Red"), "Did not accept correct answer")

	def test_answer_incorrect(self):
		self.team.request_question()
		self.assertFalse(self.team.answer("Blue"), "Accepted incorrect answer")

	def test_landmark_id_after_incorrect(self):
		self.team.request_question()
		self.team.answer("Blue")
		self.assertEqual(self.team.landmark_index, 0, "Landmark id was incremented despite incorrect answer")

	def test_landmark_id_after_correct(self):
		self.team.request_question()
		self.team.answer("Red")
		self.assertEqual(self.team.landmark_index, 1, "Landmark id was not incremented despite correct answer")
