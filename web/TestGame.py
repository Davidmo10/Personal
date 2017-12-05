from django.test import TestCase
from web.classes.game import Game
from web.models import *


class TestDeleteTeam(TestCase):
	# I am testing based on the decision made that rm_team would delete the team from the database, not remove from game
	def setup(self):
		my_models = [
			User.objects.get(name = "maker1"),
			User.objects.get(name = "team1"),
			User.objects.get(name = "team2")
			
			#User(name="maker1", pwd="maker1pwd", is_mkr=True),
			#User(name="team1", pwd="team1pwd"),
			#User(name="team2", pwd="team2pwd"),
			ScoreScheme(),
		]
		for m in my_models:
			m.save()

		self.teams = User.objects.filter(is_mkr=False)
		makers = User.objects.filter(is_mkr=True)
		score_scheme = ScoreScheme.objects.all()
		game_details = GameDetails.objects.all()

		my_models = [
			GameDetails(name="Game 1", desc="Test game 1", maker=makers[0], scheme=score_scheme[0]),
		]
		for m in my_models:
			m.save()
		# is this the right way to setup?
		self.game = Game(game_details[0])
		#TODO log in as maker once able to log in

	def test_delete_team(self):
		self.assertEqual(User.objects.filter(is_mkr=False).count(), 2, "Size of teams incorrect. Might be setup issues")
		self.assertTrue(self.game.rm_team(self.teams[0]), "Did not return true when deleting team")
		self.assertEqual(User.objects.filter(is_mkr=False).count(), 1, "Amount of teams not decreased after deletion")

	def test_delete_multiple_teams(self):
		self.assertEqual(User.objects.filter(is_mkr=False).count(), 2, "Size of teams incorrect. Might be setup issues")
		self.assertTrue(self.game.rm_team(self.teams[0]), "Did not return true when deleting team")
		self.assertEqual(User.objects.filter(is_mkr=False).count(), 1, "Amount of teams not decreased after deletion")
		self.assertTrue(self.game.rm_team(self.teams[1]), "Did not return true when deleting team")
		self.assertEqual(User.objects.filter(is_mkr=False).count(), 0, "Amount of teams not decreased after deletion")

	def test_delete_nonexistent_team(self):
		# Test fails when method fails to raise KeyError when trying to delete a team not in the database.
		self.assertRaises(KeyError, self.game.rm_team(User(name="faketeam", pwd="pass")))
