from unittest import TestCase

from Game import Game
from GameMaker import GameMaker
from Team import Team
from UserFactory import UserFactory as Uf


class TestUF(TestCase):
	def setUp(self):
		self.game = Game()

	def test_make_user(self):
		user = Uf.make_user("maker", "password", self.game)
		self.assertTrue(isinstance(user, GameMaker), "maker should be an instance of GameMaker")

	def test_make_team(self):
		team = Team("team1", "pass",Game())
		self.game.myUserDict.append(team)
		user = Uf.make_user("team1", "pass", self.game)
		self.assertTrue(isinstance(user, Team), "user created should be a team")