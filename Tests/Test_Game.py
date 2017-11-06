from Game import Game
import unittest
from DBMock import DBMock
from UI import InvalidUserException



class Test_Game:

	def setUp(self):
		try:
			self.g = Game(0)
		except UserInterfaceException:
			self.assertTrue(False, "Game failed to fetch info from DB")
		
	def tearDown(self):
		pass
	
	def test_teams_cur_lm_correct(self):
		self.assertEqual(self.g.teams_current_landmark(1), 2, "Game: current_teams_landmark() doesn't return right landmark after correct answer")
		
	
	def test_teams_cur_lm_incorrect(self):
		self.assertEqual(self.g.teams_current_landmark(0), 1, "Game: current_teams_landmark() doesn't return right landmark after incorrect answer")
		
	
	def test_teams_cur_lm_empty(self):
		self.assertEqual(self.g.teams_current_landmark(2), 0, "Game: current_teams_landmark() doesn't return first landmark")
		
	
	def test_teams_cur_lm_done(self):
		with self.assertRaises(UserInterfaceException):
			self.g.teams_current_landmark(3)
	
	