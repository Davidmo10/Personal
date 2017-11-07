import unittest

from StringClue import StringClue


class TestClue(unittest.TestCase):

    def setUp(self):
        self.Clue = StringClue("Clue Placeholder")
     
    def testDisplay(self):
        self.assertEqual(self.Clue.display(), "Clue Placeholder")