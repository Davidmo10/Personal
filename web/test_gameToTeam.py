from django.test import TestCase
from web.classes.game import Game
from web.models import *
from web.tests import TestData


class RequestClueTests(TestCase):
	# TODO

	def setUp(self):
		TestData.wipe()
		TestData.build()
		self.game = Game(GameDetails.objects.all()[0])

	def test_request_clue(self):
		pass

	def test_team_not_playing(self):
		pass

	def test_game_not_active(self):
		pass


class RequestQuestionTests(TestCase):
	# TODO

	def setUp(self):
		TestData.wipe()
		TestData.build()
		self.game = Game(GameDetails.objects.all()[0])

	def test_request_question(self):
		pass

	def  test_team_not_playing(self):
		pass

	def test_game_not_active(self):
		pass

	def test_question_pending(self):
		pass


class SubmitAnswerTests(TestCase):
	# TODO

	def setUp(self):
		TestData.wipe()
		TestData.build()
		self.game = Game(GameDetails.objects.all()[0])

	def test_submit_correct(self):
		pass

	def test_submit_incorrect(self):
		pass

	def test_team_not_playing(self):
		pass

	def test_game_not_active(self):
		pass

	def test_no_question_pending(self):
		pass


class RequestStatusTests(TestCase):
	# TODO

	def setUp(self):
		TestData.wipe()
		TestData.build()
		self.game = Game(GameDetails.objects.all()[0])

	def test_request_status(self):
		pass


class EditCredentialsTests(TestCase):
	# TODO

	def setUp(self):
		TestData.wipe()
		TestData.build()
		self.game = Game(GameDetails.objects.all()[0])

	def test_edit_credentials(self):
		pass

	def test_nonexistent_team(self):
		pass

	def test_illegal_type(self):
		pass


class ForfeitTests(TestCase):
	# TODO

	def setUp(self):
		TestData.wipe()
		TestData.build()
		self.game = Game(GameDetails.objects.all()[0])

	def test_forfeit(self):
		pass

	def test_team_not_playing(self):
		pass

	def test_game_not_active(self):
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
