from django.test import TestCase


# TODO need a frontend
class UserLoginTests(TestCase):
	# TODO method names not defined in UML
	def setup(self):
		pass

	def test_login_maker(self):
		pass

	def test_logout_maker(self):
		pass

	def test_login_team(self):
		pass

	def test_logout_team(self):
		pass


class GameMakerTests(TestCase):

	def setup(self):
		pass

	def test_make_landmark(self):
		pass

	def test_reorder_hunt(self):
		pass

	def test_edit_clue(self):
		pass

	def test_edit_confirmation(self):
		pass

	def test_make_team(self):
		pass

	def test_remove_team(self):
		pass

	def test_edit_team_credentials(self):
		pass

	def test_make_score_scheme(self):
		pass

	def test_edit_score_scheme(self):
		pass

	def test_request_status(self):
		pass

	def test_edit_game_name_and_description(self):
		pass

	def test_start_game(self):
		pass

	def test_stop_game(self):
		pass

	def test_game_is_on(self):
		pass


class TeamTests(TestCase):

	def setup(self):
		pass

	def test_request_clue(self):
		pass

	def test_request_question(self):
		pass

	def test_submit_answer(self):
		pass

	def test_edit_credentials(self):
		pass

	def test_forfeit(self):
		pass

	def test_is_on(self):
		pass
