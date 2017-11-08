import unittest

from StringQuestion import StringQuestion


class TestStringQuestion(unittest.TestCase):
	def setUp(self):
		self.Question = StringQuestion("What is five plus five?", "Ten")

	def test_initialization(self):
		self.assertEqual(self.Question.question, "What is five plus five?")
		self.assertEqual(self.Question.confirmation, "Ten")

	def test_validate(self):
		self.assertFalse(self.Question.validate("Five"))
		self.assertTrue(self.Question.validate("Ten"))

	def test_display(self):
		self.assertEqual(self.Question.display(), "What is five plus five?")
