import unittest

from Landmark import Landmark
from StringClue import StringClue
from StringQuestion import StringQuestion


class LandmarkTest(unittest.TestCase):

	def setUp(self):
		self.landmark = Landmark("Landmark1")
		self.tempQuestion = StringQuestion("question", "answer")
		self.tempclue = StringClue("clue")
		self.landmark.confirmation = self.tempQuestion

	def test_set_confirmation(self):
		self.landmark.set_confirmation(self.tempQuestion)
		self.assertEqual(self.tempQuestion, self.landmark.confirmation, "Confirmation question not correctly set")

	def test_set_clue(self):
		self.landmark.set_clue(self.tempclue)
		self.assertEqual(self.tempclue, self.landmark.clue, "Clue question not correctly set")

	def test_get_confirmation(self):
		self.landmark.confirmation = self.tempQuestion
		self.assertEqual(self.landmark.get_confirmation(), self.tempQuestion, "Cannot retrieve confirmation question")

	def test_get_clue(self):
		self.landmark.clue = self.tempclue
		self.assertEqual(self.landmark.get_clue(), self.tempclue, "Cannot retrieve clue")

	def test_answerCorrect(self):
		self.assertTrue(self.landmark.check_answer("answer"), "Did not accept correct answer")

	def test_answerIncorrect(self):
		self.assertFalse(self.landmark.check_answer("Blue"), "Accepted incorrect answer")
