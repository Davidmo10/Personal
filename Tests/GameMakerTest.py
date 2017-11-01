import unittest
from GameMaker import GameMaker
from Game import Game


class TestGameMaker(unittest.TestCase):

	def setUp(self):
		self.GM = GameMaker()
		self.GA = Game()
		
	def test_createGame(self):
		self.assertTrue(self.GM.create_game, "The game has been created.")

	def test_endGame(self):
		self.assertFalse(self.GA.is_on)
		self.assertTrue(self.GM.end_game, "The game was ended successfully")
		
	# Cannot create a game, when game is happening
	# Only GM can create game
	# Creates only one game
