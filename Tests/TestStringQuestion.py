import unittest

from StringQuestion import StringQuestion


class TestStringQuestion(unittest.TestCase):
	def setUp(self):
		self.Question = StringQuestion("What is five plus five?", "Ten")

	def test_initialization(self):
		self.assertEqual(self.Question.question, "What is five plus five?")
		self.assertEqual(self.Question.answer, "Ten")

	def test_validate(self):
		self.assertFalse(self.Question.validate("Five"), "Should be false")
		self.assertTrue(self.Question.validate("Ten"), "Should be true")

	def test_display(self):
		self.assertEqual(self.Question.display(), "What is five plus five?", "Wrong display of question)
