import unittest
from GameMaker import GameMaker
from Game import Game


class TestGameMaker(unittest.TestCase):
	def setUp(self):
		self.GM = GameMaker()
		self.GA = Game()

	# Not sure if this is a proper test: TODO: Verify Test_start
	def test_createGame(self):
		self.assertTrue(self.GM.create_game, "The game has been created.")

	def test_start(self):
		self.this_game = self.GM.create_game()
		# self.this_game.start()
		self.assertTrue(self.this_game.is_on(), "The game has not been created.")

	def test_create_landmark(self):
		self.assertTrue(self.GM.create_landmark("name", "clue", "question", "answer"), "The landmark has not been created")

	def test_create_landmark_duplicate(self):
		self.GM.create_landmark("name", "clue", "question", "answer")
		self.assertFalse(self.GM.create_landmark("name", "clue", "question", "answer"), "The landmark has been created twice.")

	def test_create_landmark_duplicate_side_effect(self):
		pass  # ToDO test that it didn't add a landmark and still return false.

	def test_create_team(self):
		self.assertTrue(self.GM.create_team("name"), "The Team has not been created.")

	def test_create_team_duplicate(self):
		self.GM.create_team("name")
		self.assertFalse(self.GM.create_team("name"), "The Team has been created twice.")

	def test_create_team_duplicate_side_effect(self):
		pass  # ToDO test that it didn't add a duplicate team and still return false.

	def test_edit_landmark_clue_when_landmark_non_existent(self):
		self.assertFalse(self.GM.edit_landmark_clue("name", "old_clue", "new_clue", ), "todo")

	def test_edit_landmark_clue_when_landmark_is_existent(self):
		self.GM.create_landmark("name", "clue", "question", "answer")
		self.assertTrue(self.GM.edit_landmark_clue("name", "old_clue", "new_clue"), "todo")

	def test_edit_landmark_question_when_landmark_non_existent(self):
		self.assertFalse(self.GM.edit_landmark_question("name", "old_question", "new_question", "new_answer"), "todo")

	def test_edit_landmark_question_when_landmark_is_existent(self):
		self.GM.create_landmark("name", "clue", "question", "answer")
		self.assertFalse(self.GM.edit_landmark_question("name", "old_question", "new_question", "new_answer"), "todo")

	def test_endGame(self):
		self.assertFalse(self.GA.is_on)
		self.assertTrue(self.GM.end_game, "The game was ended successfully")
		
	# Cannot create a game, when game is happening
	# Only GM can create game
	# Creates only one game

