import unittest
from GameMaker import GameMaker


class TestGameMaker(unittest.TestCase):

	def setUp(self):
		self.GM = GameMaker()
		
	def test_createGame(self):
		self.assertTrue(self.GM.create_game, "The game has been created.")

	# Cannot create a game, when game is happening
	# Only GM can create game
	# Creates only one game
