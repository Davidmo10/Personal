from django.test import TestCase
from web.classes import game
from web.models import *
from web.tests import TestData


class TestEditGameDetails(TestCase):

	def setup(self):
		TestData.wipe()
		TestData.build()
		GameDetails.objects.all()
		self.game = game.Game(GameDetails.objects.all()[0])
		# TODO login?

	def test_edit_values(self):
		self.assertTrue(self.game.edit("NewName", "NewDescription"), "Did not return true after editing game details.")
		self.assertEqual(GameDetails.name, "NewName", "Did not change name of game details to NewName")
		self.assertEqual(GameDetails.desc, "NewDescription", "Did not change description of game details to NewDescription")

	def test_invalid_entry(self):
		# needs to raise a ValueError if given the wrong types
		self.assertRaises(ValueError, self.game.edit(123, "Test"))
		self.assertRaises(ValueError, self.game.edit("Test", 123))
		self.assertRaises(ValueError, self.game.edit(123, 456))
