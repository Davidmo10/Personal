from django.test import TestCase

class UserLoginTests(TestCase):

	def test_login_maker(self):
		#given the gameMaker has entered a valid username
		#and has entered a valid password
		#and is_mkr is true
		#Login(request) returns a response on the server
		#allowing the Game Maker to successfully log in
		pass
	
	def test_logout_maker(self):
		#Game Maker selects logout link 
		#game maker successfully logs out of game (through Logout method in do(?))
		pass

	def test_login_team(self):
		#given the TeamUser has entered a valid username
		#and has entered a valid password
		#and is_mkr is false
		#Login(request) returns a response on the server
		#allowing the TeamUser to successfully log in
		pass

	def test_logout_team(self):
		#Team User selects logout link
		#Team User successfully logs out of game (through Logout method in do)
		pass


class GameMakerTests(TestCase):

	def test_make_landmark(self):
		#as a Game Maker I can successfully create a landmark
		pass

	def test_reorder_hunt(self):
		#as a Game Maker I can successfully reorder a hunt
		pass

	def test_edit_clue(self):
		#as a Game Maker I can successfully edit a clue
		pass

	def test_edit_confirmation(self):
		#as a Game Maker I can successfully edit a confirmation
		pass

	def test_make_team(self):
		#as a Game Maker I can successfully create a team
		pass

	def test_remove_team(self):
		#as a Game Maker I can successfully remove a team
		pass

	def test_edit_team_credentials(self):
		#as a Game Maker I can successfully edit team credentials
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

	def test_request_clue(self):
		#as 
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
