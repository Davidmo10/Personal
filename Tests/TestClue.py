import unittest
from Clue import Clue

class TestClue(unittest.TestCase):

  def setUp(self):
     self.Clue = StringClue("Clue Placeholder")
     
  def testDisplay(self):
     assertEqual(self.Clue.display(), "Clue Placeholder")
     
  
