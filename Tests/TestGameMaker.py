import unittest

from Game import Game
from GameMaker import GameMaker


class TestGameMaker(unittest.TestCase):
	def setUp(self):
		self.GM = GameMaker(Game())

	# Not sure if this is a proper test: TODO: Verify Test_start
	# def test_createGame(self):
	# 	self.assertTrue(self.GM.create_game, "The game has been created.")
	#
	# def test_start(self):
	# 	self.this_game = self.GM.create_game()
	# 	# self.this_game.start()
	# 	self.assertTrue(self.this_game.is_on(), "The game has not been created.")

	def test_list_commands(self):
		test_object = self.GM.list_commands()
		# noinspection PyTypeChecker
		self.assertTrue(isinstance(test_object, dict))

	def test_create_landmark(self):
		self.assertTrue(self.GM.create_landmark("name"), "The landmark has not been created")

	def test_create_landmark_duplicate(self):
		self.GM.create_landmark("name")
		self.assertFalse(self.GM.create_landmark("name"), "The landmark has been created twice.")

	# def test_create_landmark_duplicate_side_effect(self):
	# 	pass  # TODO test that it didn't add a landmark and still return false

	def test_create_team(self):
		self.assertTrue(self.GM.create_team("name", "pass"), "The Team has not been created.")

	def test_create_team_duplicate(self):
		self.GM.create_team("name", "pass")
		self.assertFalse(self.GM.create_team("name", "pass"), "The Team has been created twice.")

	def test_edit_landmark_clue_when_landmark_non_existent(self):
		self.assertFalse(self.GM.edit_landmark_clue("name", "new_clue", ), "todo")

	def test_edit_landmark_clue_when_landmark_is_existent(self):
		self.GM.create_landmark("name")
		self.assertTrue(self.GM.edit_landmark_clue("name", "new_clue"), "todo")

	def test_edit_landmark_question_when_landmark_non_existent(self):
		self.assertFalse(self.GM.edit_landmark_question("name", "new_question", "new_answer"), "todo")

	def test_edit_landmark_question_when_landmark_is_existent(self):
		self.GM.create_landmark("name")
		self.assertTrue(self.GM.edit_landmark_question("name", "new_question", "new_answer"), "todo")

	def test_endGame(self):
		self.assertFalse(self.GM.myGame.on)
		self.assertTrue(self.GM.end_game, "The game was ended successfully")
		
	# Cannot create a game, when game is happening
	# Only GM can create game
	# Creates only one game

