from django.test import TestCase
from web.classes.game import Game
from web.models import *
from web.tests import TestData


class EditLandmarkTests(TestCase):

	def setUp(self):
		TestData.wipe()
		TestData.build()
		self.game = Game(GameDetails.objects.all()[0])
		self.landmarks = Landmark.objects.all()

	def test_edit_landmark(self):
		self.assertEqual(self.landmarks[0].name, "Landmark 1", "Name incorrect: something wrong with setup")
		self.assertEqual(self.landmarks[0].desc, "Test landmark 1", "Description incorrect: something wrong with setup")
		self.game.edit_lmark(self.landmarks[0], "NewName", "NewDesc")
		self.landmarks = Landmark.objects.all()
		self.assertEqual(self.landmarks[0].name, "NewName", "Landmark name not changed correctly")
		self.assertEqual(self.landmarks[0].desc, "NewDesc", "Landmark description not changed correctly")

	def test_duplicate_name(self):
		with self.assertRaises(NameError):
			self.game.edit_lmark(self.landmarks[0], "Landmark 7", "RandomDesc")

	def test_illegal_type(self):
		with self.assertRaises(ValueError):
			self.game.edit_lmark(self.landmarks[0], False, True)

	def test_edit_nonexistent(self):
		self.game.edit_lmark(Landmark(name="FakeLandmark", desc="FakeDesc"), "NewLandmark", "NewDesc")
		self.newLandmark = Landmark.objects.filter(name="NewLandmark")
		self.assertEqual(self.newLandmark, "NewDesc", "New landmark not created properly")


class ReorderHuntTests(TestCase):
	# TODO

	def setUp(self):
		TestData.wipe()
		TestData.build()
		self.game = Game(GameDetails.objects.all()[0])

	def test_reorder(self):
		pass

	def test_below_zero(self):
		pass

	def test_above_bounds(self):
		pass

	def test_invalid_order(self):
		pass

	def test_illegal_type(self):
		pass


class EditClueTests(TestCase):
	# TODO

	def setUp(self):
		TestData.wipe()
		TestData.build()
		self.game = Game(GameDetails.objects.all()[0])
		self.clues = Clue.objects.all()

	def test_edit_clue(self):
		pass

	def test_illegal_type(self):
		pass

	def test_illegal_landmark(self):
		pass

	def test_edit_multiple(self):
		pass


class EditConfirmation(TestCase):

	def setUp(self):
		TestData.wipe()
		TestData.build()
		self.game = Game(GameDetails.objects.all()[0])
		self.confirmations = Confirmation.objects.all()
		self.landmark = Landmark.objects.all()[0]

	def test_edit_confirmation(self):
		self.assertEqual(self.confirmations[0].ques, "Question 1", "Incorrect question: something wrong with setup")
		self.game.edit_conf(self.landmark, "NewQuestion", "NewAnswer")
		self.assertEqual(self.confirmations[0].ques, "NewQuestion", "Question not changed correctly")
		self.assertEqual(self.confirmations[0].ans, "NewAnswer", "Answer not changed correctly")

	def test_illegal_type(self):
		with self.assertRaises(ValueError):
			self.game.edit_conf(self.landmark, False, True)

	def test_illegal_landmark(self):
		with self.assertRaises(IndexError):
			self.game.edit_conf(Landmark(name="Dummy", desc="Dummy"), "This test", "Should raise IndexError")


class MakeTeamTests(TestCase):

	def setUp(self):
		TestData.wipe()
		TestData.build()
		self.game = Game(GameDetails.objects.all()[0])
		self.teams = User.objects.filter(is_mkr=False)

	def test_make_team(self):
		self.assertEqual(len(self.teams), 14, "Wrong number of teams: something wrong in setup")
		self.game.mk_team("TeamName", "TeamPass")
		self.assertEqual(len(User.objects.filter(is_mkr=False)), 15, "Number of teams did not increment on team creation")
		self.newTeam = User.objects.filter(name="TeamName")
		self.assertEqual(self.newTeam.count(), 1, "Team not found in list of users")

	def test_make_duplicate_team(self):
		with self.assertRaises(NameError):
			self.game.mk_team("team1", "Pass")


class RemoveTeamTests(TestCase):
	# I am testing based on the decision made that rm_team would delete the team from the database, not remove from game
	def setUp(self):
		TestData.wipe()
		TestData.build()
		self.teams = User.objects.filter(is_mkr=False)
		self.game = Game(GameDetails.objects.all()[0])

	def test_delete_team(self):
		self.assertEqual(User.objects.filter(
			is_mkr=False).count(), 14,
			"Size of teams incorrect. Might be setup issues")
		self.assertTrue(self.game.rm_team(self.teams[0]), "Did not return true when deleting team")
		self.assertEqual(User.objects.filter(is_mkr=False).count(), 13, "Amount of teams not decreased after deletion")

	def test_delete_multiple_teams(self):
		self.assertEqual(User.objects.filter(
			is_mkr=False).count(), 14,
			"Size of teams incorrect. Might be setup issues")
		self.assertTrue(self.game.rm_team(self.teams[0]), "Did not return true when deleting team")
		self.assertEqual(User.objects.filter(is_mkr=False).count(), 13, "Amount of teams not decreased after deletion")
		self.assertTrue(self.game.rm_team(self.teams[1]), "Did not return true when deleting team")
		self.assertEqual(User.objects.filter(is_mkr=False).count(), 12, "Amount of teams not decreased after deletion")

	def test_delete_nonexistent_team(self):
		# Test fails when method fails to raise KeyError when trying to delete a team not in the database.
		with self.assertRaises(KeyError):
			self.game.rm_team(User(name="faketeam", pwd="pass"))


class EditTeamCredentialsTests(TestCase):

	def setUp(self):
		TestData.wipe()
		TestData.build()
		self.game = Game(GameDetails.objects.all()[0])
		self.teams = User.objects.filter(is_mkr=False)

	def test_edit_credentials(self):
		self.game.edit_creds(self.teams[0], "NewName", "NewPass")
		self.assertEqual(self.teams[0].name, "NewName", "Team name not changed correctly")
		self.assertEqual(self.teams[0].pwd, "NewPass", "Team password not changed correctly")

	def test_invalid_team(self):
		with self.assertRaises(KeyError):
			self.game.edit_creds(User(name="FakeTeam", pwd="Should raise KeyError"), "NewName", "NewPass")

	def test_not_in_game(self):
		# Raises KeyError when trying to edit team not in game
		with self.assertRaises(KeyError):
			self.game.edit_creds(self.teams.filter(name="team12"), "NewName", "NewPass")

	def test_illegal_type(self):
		with self.assertRaises(ValueError):
			self.game.edit_creds(self.teams[0], False, True)

	def test_duplicate_name(self):
		# Doesn't seem like a requirement based on interface
		pass


class MakeScoreSchemeTests(TestCase):

	def setUp(self):
		TestData.wipe()
		TestData.build()
		self.game = Game(GameDetails.objects.all()[0])

	def test_make_scheme(self):
		self.game.mk_score_sch("NewScheme")
		self.assertTrue(ScoreScheme.objects.filter(name="NewScheme") is not None, "Scheme  not created correctly")

	def test_duplicate_name(self):
		with self.assertRaises(NameError):
			self.game.mk_score_sch("Test scheme")

	def test_illegal_type(self):
		with self.assertRaises(ValueError):
			self.game.mk_score_sch(False)


class EditScoreSchemeTests(TestCase):
	# TODO

	def setUp(self):
		TestData.wipe()
		TestData.build()
		self.game = Game(GameDetails.objects.all()[0])

	def test_edit_scheme(self):
		pass

	def test_nonexistent_scheme(self):
		pass

	def test_scheme_in_user(self):
		pass

	def test_illegal_type(self):
		pass


class RequestMakerStatusTests(TestCase):
	# TODO does this method exist anymore?

	def setUp(self):
		TestData.wipe()
		TestData.build()
		self.game = Game(GameDetails.objects.all()[0])

	def test_request_status(self):
		pass


class RequestHuntTests(TestCase):
	# TODO

	def setUp(self):
		TestData.wipe()
		TestData.build()
		self.game = Game(GameDetails.objects.all()[0])

	def test_request_hunt(self):
		pass


class EditGameTests(TestCase):

	def setUp(self):
		TestData.wipe()
		TestData.build()
		self.game = Game(GameDetails.objects.all()[0])
		self.details = GameDetails.objects.all()[0]

	def test_edit_values(self):
		self.assertTrue(self.game.edit("NewName", "NewDescription"), "Did not return true after editing game details.")
		self.assertEqual(self.details.name, "NewName", "Did not change name of game details to NewName")
		self.assertEqual(
			self.details.desc, "NewDescription",
			"Did not change description of game details to NewDescription")

	def test_invalid_entry(self):
		# needs to raise a ValueError if given the wrong types
		with self.assertRaises(ValueError):
			self.game.edit(123, "Test")
			self.game.edit("Test", 123)
			self.game.edit(123, 456)


class StartGameTests(TestCase):
	# TODO

	def setUp(self):
		TestData.wipe()
		TestData.build()
		self.game = Game(GameDetails.objects.all()[0])

	def test_start_game(self):
		pass

	def test_already_started(self):
		pass


class StopGameTests(TestCase):
	# TODO

	def setUp(self):
		TestData.wipe()
		TestData.build()
		self.game = Game(GameDetails.objects.all()[0])

	def test_stop_game(self):
		pass

	def test_already_stopped(self):
		pass


class IsOnTests(TestCase):
	# TODO

	def setUp(self):
		TestData.wipe()
		TestData.build()
		self.game = Game(GameDetails.objects.all()[0])

	def test_is_on(self):
		pass

	def test_is_off(self):
		pass


class SetWinnerTests(TestCase):
	# TODO

	def setUp(self):
		TestData.wipe()
		TestData.build()
		self.game = Game(GameDetails.objects.all()[0])

	def test_set_winner(self):
		pass

	def test_not_in_game(self):
		pass

	def test_nonexistent_team(self):
		pass

	def test_team_not_finished(self):
		pass
