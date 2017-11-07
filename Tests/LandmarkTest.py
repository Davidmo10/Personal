import unittest
from Landmark import Landmark
from StringQuestion import StringQuestion


class TestLandmarkConfirmation(unittest.TestCase):

	def setUp(self):
		self.string_question = StringQuestion("What color is the car?", "Red")
		self.landmark = Landmark()
		self.landmark.confirmation["Confirmation"] = self.string_question
		pass

	def test_getQuestion(self):
		self.assertEqual(
			self.landmark.get_confirmation(), "What color is the car?", "Returned: " + self.landmark.get_confirmation()
			+ " instead of proper question")

	def test_answerCorrect(self):
		self.assertTrue(self.landmark.check_answer("Red"), "Did not accept correct answer")

	def test_answerIncorrect(self):
		self.assertFalse(self.landmark.check_answer("Blue"), "Accepted incorrect answer")
