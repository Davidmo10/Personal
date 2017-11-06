from Team import Team
import unittest
from DBMock import DBMock
from Landmark import InvalidUserException

class Test_Team(unittest.TestCase):

	def setUp(self):
		pass
	
	def tearDown(self):
		pass
	
	def test_creation(self):
		t = Team(0)
		created = {"user_id" : t.user_id, "name" : t.name, "pwd" : t.pwd, "game_id" : t.game_id}
		fetched = DBMock.teams[0] 
		self.assertEqual(created, fetched, "Team(id) did not retrieve team info")
	
	def test_event_history(self):
		t = Team(0)
		created = t.events
		fetched = DBMock.games[0]["teams"][0]["events"]
		self.assertEqual(created, fetched, "Team(id) did not retrieve team event history")
	