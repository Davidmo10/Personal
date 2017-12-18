from django.test import TestCase
from web.classes.game import Game
from web.models import *
from web.tests import TestData


class RequestClueTests(TestCase):

	def setUp(self):
		TestData.wipe()
		TestData.build()
		self.game = Game(GameDetails.objects.all()[0])
		self.teams = User.objects.filter(is_mkr=False)

	def test_request_clue(self):
		self.game.dtls.on = True
		self.assertEqual(self.game.req_clue(self.teams[0]), "Clue 1", "Did not return clue properly")

	def test_team_not_playing(self):
		self.game.dtls.on = True
		with self.assertRaises(ReferenceError):
			self.game.req_clue(self.teams[12])

	def test_game_not_active(self):
		with self.assertRaises(IndexError):
			self.game.req_clue(self.teams[0])


class RequestQuestionTests(TestCase):

	def setUp(self):
		TestData.wipe()
		TestData.build()
		self.game = Game(GameDetails.objects.all()[0])
		self.teams = User.objects.filter(is_mkr=False)

	def test_request_question(self):
		self.game.dtls.on = True
		self.assertEqual(self.game.req_ques(self.teams[0]), "Question 1", "Did not return question properly")

	def test_team_not_playing(self):
		self.game.dtls.on = True
		with self.assertRaises(ReferenceError):
			self.game.req_ques(self.teams[12])

	def test_game_not_active(self):
		with self.assertRaises(IndexError):
			self.game.req_ques(self.teams[0])

	def test_question_pending(self):
		# Not sure if testing this correctly
		self.game.dtls.on = True
		self.game.req_ques(self.teams[0])
		with self.assertRaises(EnvironmentError):
			self.game.req_ques(self.teams[0])


class SubmitAnswerTests(TestCase):

	def setUp(self):
		TestData.wipe()
		TestData.build()
		self.game = Game(GameDetails.objects.all()[0])
		self.teams = User.objects.filter(is_mkr=False)

	def test_submit_correct(self):
		self.game.dtls.on = True
		self.game.req_ques(self.teams[0])
		self.assertTrue(self.game.submit_ans(self.teams[0], "Answer 1"), "Did not accept correct answer")

	def test_submit_incorrect(self):
		self.game.dtls.on = True
		self.game.req_ques(self.teams[0])
		self.assertFalse(self.game.submit_ans(self.teams[0], "Incorrect answer"), "Did not reject incorrect answer")

	def test_team_not_playing(self):
		# Different error may be raised depending on check order, which is okay
		self.game.dtls.on = True
		with self.assertRaises(ReferenceError):
			self.game.submit_ans(self.teams[12], "Blarg")

	def test_game_not_active(self):
		# Different error may be raised depending on check order, which is okay
		with self.assertRaises(IndexError):
			self.game.submit_ans(self.teams[0], "Oh")

	def test_no_question_pending(self):
		# Different error may be raised depending on check order, which is okay
		self.game.dtls.on = True
		with self.assertRaises(KeyError):
			self.game.submit_ans(self.teams[0], "Answer")


class RequestStatusTests(TestCase):

	def setUp(self):
		TestData.wipe()
		TestData.build()
		self.game = Game(GameDetails.objects.all()[0])
		self.teams = User.objects.filter(is_mkr=False)

	def test_request_status(self):
		# Not asserting, it's just passing object
		self.game.req_status(self.teams[0])


class EditCredentialsTests(TestCase):

	def setUp(self):
		TestData.wipe()
		TestData.build()
		self.game = Game(GameDetails.objects.all()[0])
		self.teams = User.objects.filter(is_mkr=False)

	def test_edit_credentials(self):
		self.assertEqual(self.teams[0].name, "team1", "Incorrect name, something wrong with setup")
		self.assertEqual(self.teams[0].pwd, "team1pwd", "Incorrect password, something wrong with setup")
		self.assertTrue(self.game.edit_creds(self.teams[0], "NewName", "NewPassword"), "Method should return true")
		self.assertEqual(self.teams[0].name, "NewName", "Name not changed properly")
		self.assertEqual(self.teams[0].pwd, "NewPassword", "Password not changed properly")

	def test_nonexistent_team(self):
		with self.assertRaises(KeyError):
			self.game.edit_creds(User(name="Fake", pwd="User"), "NewName", "NewPassword")

	def test_illegal_type(self):
		with self.assertRaises(ValueError):
			self.game.edit_creds(self.teams[0], False, True)


class ForfeitTests(TestCase):

	def setUp(self):
		TestData.wipe()
		TestData.build()
		self.game = Game(GameDetails.objects.all()[0])
		self.teams = User.objects.filter(is_mkr=False)

	def test_forfeit(self):
		self.game.dtls.on = True
		self.assertTrue(Status.objects.get(team=self.teams[0]).playing, "Team not playing, something wrong with setup")
		self.assertTrue(self.game.forfeit(self.teams[0]), "Method should return true")
		self.assertFalse(Status.objects.get(team=self.teams[0]).playing, "Did not set playing field to false")

	def test_team_not_playing(self):
		self.game.dtls.on = True
		self.game.forfeit(self.teams[0])
		with self.assertRaises(ReferenceError):
			self.game.forfeit(self.teams[0])

	def test_game_not_active(self):
		with self.assertRaises(IndexError):
			self.game.forfeit(self.teams[0])


class IsOnTests(TestCase):

	def setUp(self):
		TestData.wipe()
		TestData.build()
		self.game = Game(GameDetails.objects.all()[0])

	def test_is_on(self):
		self.game.dtls.on = True
		self.assertTrue(self.game.is_on(), "Should return true when game is on")

	def test_is_off(self):
		self.assertFalse(self.game.is_on(), "Should return false when game is off")
