import unittest
from Team import Team

class TestTeam(unittest.TestCase):
  
  def setUp(self):
    self.TM = Team()
    
  def test_forfeit(self):
    self.assertTrue(self.TM.forfeit, "The game was successfully forfeited");
