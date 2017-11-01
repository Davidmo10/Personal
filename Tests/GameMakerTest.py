import unittest
from GameMaker import GameMaker


class TestGameMaker(unittest.TestCase):
	def setUp(self):
		self.GM = GameMaker()

	# Not sure if this is a proper test: TODO: Verify Test_start

	def test_start(self):
		self.this_game = self.GM.create_game()
		self.assertTrue(self.this_game.is_on(), "The game has not been created.")

	def test_create_landmark(self):
		self.assertTrue(self.GM.create_landmark("name", "place"), "The landmark has not been created")

	def test_create_landmark_duplicate(self):
		self.GM.create_landmark("name", "place")
		self.assertFalse(self.GM.create_landmark("name", "place"), "The landmark has been created twice.")

	def test_create_team(self):
		self.assertTrue(self.GM.create_team("name"), "The Team has not been created.")

	def test_create_team_duplicate(self):
		self.GM.create_team("name")
		self.assertFalse(self.GM.create_team("name"), "The Team has been created twice.")

	def test_edit_landmark_clue_when_landmark_non_existent(self):
		self.assertFalse(self.GM.edit_landmark_clue("name", "old_clue", "new_clue"), "todo")

	def test_edit_landmark_clue_when_landmark_is_existent(self):
		self.GM.create_landmark("name", "place")
		self.assertTrue(self.GM.edit_landmark_clue("name", "old_clue", "new_clue"), "todo")

	def test_edit_landmark_question_when_landmark_non_existent(self):
		self.assertFalse(self.GM.edit_landmark_question("name", "old_question", "new_question"), "todo")

	def test_edit_landmark_question_when_landmark_is_existent(self):
		self.GM.create_landmark("name", "place")
		self.assertFalse(self.GM.edit_landmark_question("name", "old_question", "new_question"), "todo")

