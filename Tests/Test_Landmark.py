import unittest
from Landmark import Landmark
from DBMock import DBMock
from DB_Interfaces import InvalidGameException,  InvalidTeamException,  InvalidUserException, InvalidLandmarkException,  InvalidGameStateException, InvalidTeamStateException, EmptyGameSetException, EmptyTeamListException, LandmarkAlreadyInGameException, SettingAnswerWithNoQuestionException
from UI import UserInterfaceException

class Test_Landmark(unittest.TestCase):

	def setUp(self):
		
		tester = {"landmark_id" : 3, "title" : "foo", "desc" : "bar", "clue" : "cmon", "question" : "man", "answer" : "shit" }
		DBMock.games[0]["landmarks"].append(tester)
		self.lm = Landmark(0, 3)
		
	def tearDown(self):
		g = DBMock.fetch_game(0)
		if( len(g["landmarks"]) > 3):
			del g["landmarks"][3]

	def test_instantiate_invalid(self):
		with self.assertRaises(UserInterfaceException):
			tester = Landmark(0, -1)
	
	def test_set_question(self):
		me = self.lm
		self.assertTrue(me.set_question("meaning of life?"), "Landmark test: valid set_question did not return true")
		self.assertEqual(me.question, "meaning of life?", "Landmark test: successful set_question did not change instance attribute")
	
	def test_set_question_fail(self):
		me = self.lm
		self.assertFalse(me.set_question(None), "Landmark test: invalid set_question returned true")
		self.assertNotEqual(me.question, None, "Landmark test: unsuccessful set_question cleared instance attribute")
	
	def test_set_answer(self):
		me = self.lm
		self.assertTrue(me.set_answer("dunno"), "Landmark test: valid set_answer did not return true")
		self.assertEqual(me.answer, "dunno", "Landmark test: successful set_answer did not change instance attribute")
	
	def test_set_answer_fail(self):
		me = self.lm
		self.assertFalse(me.set_answer(None), "Landmark test: invalid set_answer returned true")
		self.assertNotEqual(me.answer, None, "Landmark test: unsuccessful set_answer cleared instance attribute")
	
	def test_set_q_and_a(self):
		me = self.lm
		self.assertTrue(me.set_question_and_answer("what's the meaning of life", "dunno"), "Landmark test: valid set_question_and_answer returned false")
		self.assertEqual(me.question, "what's the meaning of life", "Landmark test: valid set_question_and_answer did not change question attribute")
		self.assertEqual(me.answer, "dunno", "Landmark test: valid set_question_and_answer did not change answer attribute")
	
	def test_add_clue(self):
		me = self.lm
		self.assertTrue(me.add_clue("where?"), "Landmark test: valid set_clue returned false")
		self.assertEqual(me.clue, "where?", "Landmark test: successful set_clue didn't change instance attribute")
	
	
	def test_add_clue_fail(self):
		me = self.lm
		self.assertFalse(me.add_clue(None), "Landmark test: invalid set_clue returned true")
		self.assertNotEqual(me.clue, None, "Landmark test: unsuccessful set_clue changed instance attribute")
	
	def test_edit_title(self):
		me = self.lm
		self.assertTrue(me.edit_title("foo"), "Landmark test: valid edit_title returned false")
		self.assertEqual(me.title, "foo", "Landmark test: valid edit_title did not change instance attribute")
	
	def test_edit_title_fail(self):
		me = self.lm
		self.assertFalse(me.edit_title(None), "Landmark test: invalid edit_title returned true")
		self.assertNotEqual(me.title, None, "Landmark test: invalid edit_title changed instance attribute")
	
	
	def test_edit_description(self):
		me = self.lm
		self.assertTrue(me.edit_description("foo"), "Landmark test: valid edit_description returned false")
		self.assertEqual(me.desc, "foo", "Landmark test: valid edit_description did not change instance attribute")
	
	def test_edit_description_fail(self):
		me = self.lm
		self.assertFalse(me.edit_description(None), "Landmark test: invalid edit_description returned true")
		self.assertNotEqual(me.desc, None, "Landmark test: invalid edit_description changed instance attribute")