import unittest
from Team import Team
from Game import Game

class TestTeam(unittest.TestCase):
  
  def setUp(self):
    self.TM = Team()
    self.GA = Game()
    
  def test_forfeit(self):
    if(self.assertTrue(self.GA.start))
      self.assertTrue(self.TM.forfeit, "The game was successfully forfeited");
