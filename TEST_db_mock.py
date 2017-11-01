from unittest import TestCase 
from db_mock import DBMock, Team_DBMock, Master_DBMock, Game_DBMock, Landmark_DBMock
from escavenger_db_exceptions import InvalidGameException, InvalidTeamException, InvalidLandmarkException, InvalidUserException, InvalidGameStateException, InvalidTeamStateException, EmptyGameSetException, EmptyTeamListException, LandmarkAlreadyInGameException, SettingAnswerWithNoQuestionException
import copy

class Static_Tests(TestCase):

	def setUp(self):
		self.mock = DBMock()
	
	def test_real_game(self):
		self.assertEqual(self.mock.fetch_game(0), {"game_id" : 0,  "title" : "Pokemon", "desc" : "Catch those fuckers", "master_id" : 2,"on" : 1,"landmarks" : [{ "landmark_id" : 0, "title" : "uwm" ,  "desc" : "blah uwm blah" ,  "clue" : "it's uwm" ,  "question" : "am i uwm?",  "answer" : "yes"},  { "landmark_id" : 1,  "title" : "ems" ,  "desc" : "blah ems blah" ,  "clue" : "it's ems" ,  "question" : "am i ems?",  "answer" : "yes"}, { "landmark_id" : 2,  "title" : "jimmy johns" ,  "desc" : "blah jimmy johns blah" ,  "clue" : "it's jimmy johns" ,  "question" : "am i jimmy johns?",  "answer" : "yes"}  ],  "teams" : [{ "team_id" : 0, "events" : [{ "landmark_id" : 0,"correct" : 1  },  { "landmark_id" : 1,"correct" : 0  },  { "landmark_id" : 1,"correct" : 0  } ], "playing" : 1},{ "team_id" : 1, "events" : [{ "landmark_id" : 0,"correct" : 1  },  { "landmark_id" : 1,"correct" : 0  },  ], "playing" : 1},{ "team_id" : 2, "events" : [  ], "playing" : 1},{ "team_id" : 3, "events" : [{ "landmark_id" : 0,"correct" : 1  },  { "landmark_id" : 1,"correct" : 1  },  { "landmark_id" : 2,"correct" : 1  } ], "playing" : 1} ]}, "fetch_game to equate on real id = 0")
		
	def test_fake_game(self):
		with self.assertRaises(InvalidGameException):
			self.mock.fetch_game(100)
	
	def test_real_team(self):
		self.assertEqual(self.mock.fetch_team(0,0), { "team_id" : 0,"events" : [ { "landmark_id" : 0,"correct" : 1},{ "landmark_id" : 1,"correct" : 0},{ "landmark_id" : 1,"correct" : 0}],"playing" : 1}, "fetch_team failed to equate on real team id 0 in game id 0")
		
	def test_fake_team_real_game(self):
		with self.assertRaises(InvalidTeamException):
			self.mock.fetch_team(0, 100)
			
	def test_fake_team_fake_game(self):
		with self.assertRaises(InvalidGameException):
			self.mock.fetch_team(100, 100)
	
	def test_real_team_fake_game(self):
		with self.assertRaises(InvalidGameException):
			self.mock.fetch_team(100, 0)

	def test_real_landmark(self):
		self.assertEqual(self.mock.fetch_lm(0, 0), { "landmark_id" : 0,"title" : "uwm" , "desc" : "blah uwm blah" , "clue" : "it's uwm" , "question" : "am i uwm?", "answer" : "yes"}, "fetch_landmark failed to equate on real game_id = 0, real lm_id = 0")
		
	def test_fake_landmark_real_game(self):
		with self.assertRaises(InvalidLandmarkException):
			self.mock.fetch_lm(100, 0)

	def test_fake_landmark_fake_game(self):
		with self.assertRaises(InvalidGameException):
			self.mock.fetch_lm(100, 100)
			
	def test_real_landmark_fake_game(self):
		with self.assertRaises(InvalidGameException):
			self.mock.fetch_lm(0, 100)


class Test_Team(TestCase):
	
	def setUp(self):
		self.db_mock = DBMock()
		self.t = self.db_mock.fetch_team(0, 1)
		self.g = self.db_mock.fetch_game(0)
		self.mock = Team_DBMock()
	
	def tearDown(self):
		self.g["on"] = 1
		self.t["playing"] = 1
	
	def test_login_fail(self):
		with self.assertRaises(InvalidUserException):
			self.mock.login("foo", "bar")
	
	def test_login(self):
		self.assertEqual(self.mock.login("team2", "team2pwd"),  {"userid" : 1, "name" : "team2", "pwd" : "team2pwd"}, "team login didn't return team info")
	
	def test_forfeit(self):
		self.mock.forfeit(self.g["game_id"], self.t["team_id"])
		self.assertFalse(self.t["playing"], "forfeit(g[game_id], t[team_id]) didn't flip team 2's 'playing' flag")
	
	def test_forfeit_team_out(self):
		self.t["playing"] = 0
		with self.assertRaises(InvalidTeamStateException):
			self.mock.forfeit(self.g["game_id"], self.t["team_id"])

	def test_forfeit_game_off(self):
		self.g["on"] = 0
		with self.assertRaises(InvalidGameStateException):
			self.mock.forfeit(self.g["game_id"], self.t["team_id"])


class Test_Master(TestCase):
	
	def setUp(self):
		self.db_mock = DBMock()
		self.t = self.db_mock.fetch_team(0,1)
		self.g = self.db_mock.fetch_game(0)
		self.mock = Master_DBMock()
		self.new_g = {"game_id" : 1 , "master_id" : 2, "title" : "Default Title", "desc" : "Default Description", "on" : 0, "landmarks" : (), "teams" : () }

	def tearDown(self):
		self.g["on"] = 1

	def test_login(self):
		self.assertEqual(self.mock.login("master", "masterpass"),  {"user_id" : 2, "name" : "master", "pwd" : "masterpass", "game_id" : 0}, "master login didn't return master info")
	
	def test_login_fail(self):
		with self.assertRaises(InvalidUserException):
			self.mock.login("foo", "bar")
	
	def test_create_game(self):
		self.assertEqual(1, self.mock.create_game(2), "test_create_game didn't return correct game id")
		self.assertEqual(self.new_g, self.db_mock.fetch_game(1), "test_create_game didn't add game to list")
	
	def test_end_game(self):
		self.mock.end_game(0)
		self.assertFalse(self.g["on"], "end_game didn't end game")
	
	def test_end_game_fail(self):
		self.mock.end_game(0)
		with self.assertRaises(InvalidGameStateException):
			self.mock.end_game(0)

class Test_Game(TestCase):
	
	def setUp(self):
		self.db_mock = DBMock()
		self.g = self.db_mock.fetch_game(0)
		self.t = self.db_mock.fetch_team(0,0)
		self.mock = Game_DBMock()
		self.saved_lm = copy.deepcopy(self.g["landmarks"])
		self.saved_teams = copy.deepcopy(self.g["teams"])
	
	def tearDown(self):
		self.g["on"] = 1
		self.g["landmarks"] = self.saved_lm
		self.g["teams"] = self.saved_teams
		del self.db_mock.fetch_team(0, 2)["events"] [:]
	
	def test_start(self):
		self.g["on"] = 0
		self.mock.start(self.g["game_id"])
		self.assertTrue(self.g["on"], "start didn't turn game on");
	
	def test_start_fail(self):
		with self.assertRaises(InvalidGameStateException):
			self.mock.start(self.g["game_id"])
	
	def test_stop(self):
		self.mock.stop(self.g["game_id"])
		self.assertFalse(self.g["on"], "stop didn't turn game off");
	
	def test_stop_fail(self):
		self.g["on"] = 0
		with self.assertRaises(InvalidGameStateException):
			self.mock.stop(self.g["game_id"])
	
	def test_fetch_landmarks(self):
		self.assertEqual(self.mock.fetch_landmarks(self.g["game_id"]), [{ "landmark_id" : 0,"title" : "uwm" , "desc" : "blah uwm blah" , "clue" : "it's uwm" , "question" : "am i uwm?", "answer" : "yes"},  { "landmark_id" : 1, "title" : "ems" , "desc" : "blah ems blah" , "clue" : "it's ems" , "question" : "am i ems?", "answer" : "yes"}, { "landmark_id" : 2, "title" : "jimmy johns" , "desc" : "blah jimmy johns blah" , "clue" : "it's jimmy johns" , "question" : "am i jimmy johns?", "answer" : "yes"}], "fetch_landmark did not return the landmark" )
	
	def test_fetch_landmarks_empty(self):
		with self.assertRaises(EmptyGameSetException):
			self.g["landmarks"] = None
			self.mock.fetch_landmarks(self.g["game_id"])
	
	def test_fetch_team_list(self):
		self.assertEqual(self.mock.fetch_team_list(self.g["game_id"]), [{ "team_id" : 0,"events" : [ { "landmark_id" : 0,"correct" : 1},{ "landmark_id" : 1,"correct" : 0},{ "landmark_id" : 1,"correct" : 0}],"playing" : 1},{ "team_id" : 1,"events" : [ { "landmark_id" : 0,"correct" : 1},{ "landmark_id" : 1,"correct" : 0}, ],"playing" : 1},{ "team_id" : 2,"events" : [ ],"playing" : 1},{ "team_id" : 3,"events" : [ { "landmark_id" : 0,"correct" : 1},{ "landmark_id" : 1,"correct" : 1},{ "landmark_id" : 2,"correct" : 1}],"playing" : 1}], "fetch_team_list did not return the list" )
	
	def test_fetch_team_empty(self):
		with self.assertRaises(EmptyTeamListException):
			self.g["teams"] = None
			self.mock.fetch_team_list(self.g["game_id"])
	
	def test_fetch_team_status(self):
		self.assertEqual(self.mock.fetch_team_status(self.g["game_id"], self.t["team_id"] ), { "team_id" : 0,"events" : [ { "landmark_id" : 0,"correct" : 1},{ "landmark_id" : 1,"correct" : 0},{ "landmark_id" : 1,"correct" : 0}],"playing" : 1}, "fetch_team_status did not return the right status" )
	
	def test_fetch_team_status_fail(self):
		with self.assertRaises(InvalidTeamException):
			self.mock.fetch_team_status(0, 100)
	
	def test_submit_answer_correct(self):
		self.mock.submit_answer(0, 2, 0, "yEs")
		tmp = self.db_mock.fetch_team(0, 2)
		self.assertEqual(tmp["events"][0]["landmark_id"], 0, "submit_answer did not add the answer to teams events")
		self.assertTrue(tmp["events"][0]["correct"], "submit_answer did not record answer as correct")
	
	def test_submit_answer_wrong(self):
		self.mock.submit_answer(0, 2, 0, "no")
		tmp = self.db_mock.fetch_team(0, 2)
		self.assertFalse(tmp["events"][0]["correct"], "submit_answer did not record answer as incorrect")


class Test_Landmark(TestCase):
	
	def setUp(self):
		self.db_mock = DBMock()
		self.g = self.db_mock.fetch_game(0)
		self.l = self.db_mock.fetch_lm(0, 0)
		self.mock = Landmark_DBMock()
#		self.save_g = copy.deepcopy(self.g)
#		self.save_l = copy.deepcopy(self.l)
		self.new_lm = { "landmark_id" : 3, "title" : "foo" , "desc" : "blah foo blah", "clue" : None, "question" : None, "answer" : None}
	
	def tearDown(self):
		if len(self.g["landmarks"]) == 4:
			del self.g["landmarks"][3] 
		self.l["title"] = "uwm"
		self.l["desc"] = "blah uwm blah"
		self.l["question"] = "am i uwm?"
		self.l["answer"] = "yes"
		self.l["clue"] = "it's uwm"
		del self.g["teams"][2]["events"] [:]
		
	
	def test_create_landmark(self):
		self.mock.create_landmark(self.g["game_id"], "foo", "blah foo blah")
		self.assertEqual(self.g["landmarks"][3], self.new_lm, "create_landmark didn't add the landmark to the game")
	
	def test_create_landmark_duplicate(self):
		self.mock.create_landmark(self.g["game_id"], "foo", "blah foo blah")
		with self.assertRaises(LandmarkAlreadyInGameException):
			self.mock.create_landmark(self.g["game_id"], "foo", "blah foo blah")
			
	def test_edit_landmark(self):
		self.mock.edit_landmark(0, 0, "foo", "bar")
		self.assertEqual(self.l["title"], "foo", "edit_landmark(title, desc) didn't edit title")
		self.assertEqual(self.l["desc"], "bar", "edit_landmark(title, desc) didn't edit desc")
	
	def test_edit_landmark_title_only(self):
		self.mock.edit_landmark(0, 0, "foo", None)
		self.assertEqual(self.l["title"], "foo", "edit_landmark(title, None) didn't edit title")
	
	def test_edit_landmark_title(self):
		self.mock.edit_landmark(0, 0, None, "bar")
		self.assertEqual(self.l["desc"], "bar", "edit_landmark(None, desc) didn't edit desc")
	
	def test_edit_landmark_empty(self):
		self.assertFalse(self.mock.edit_landmark(0, 0, None, None), "edit_landmark(None, None) didn't return false")
		self.assertEqual(self.l["title"], "uwm", "edit_landmark(None, None) changed the title")
		self.assertEqual(self.l["desc"], "blah uwm blah", "edit_landmark(None, None) changed the desc")
	
	def test_set_clue_existing_landmark(self):
		self.mock.set_clue(0, 0, "foo")
		self.assertEqual(self.l["clue"], "foo", "set_clue on existing landmark did not change clue")
	
	def test_set_clue_new_landmark(self):
		tmp = self.mock.create_landmark(0, "foo", "bar")["landmark_id"]
		self.mock.set_clue(tmp, 0, "blah")
		self.assertEqual(self.g["landmarks"][ tmp ]["clue"], "blah", "set_clue on newly created landmark did not register")
	
	def test_set_clue_false(self):
		self.assertFalse(self.mock.set_clue(0, 0, None), "set_clue(None) did not return false")
	
	def test_set_q_and_a_existing_landmark(self):
		self.mock.set_question(0, 0, "foo", "bar")
		self.assertEqual(self.l["question"], "foo", "set_question(blah, blah) didn't set question on existing landmark")
		self.assertEqual(self.l["answer"], "bar", "set_question(blah, blah) didn't set answer on existing landmark")
	
	def test_set_q_existing_landmark(self):
		self.mock.set_question(0, 0, "foo", None)
		self.assertEqual(self.l["question"], "foo", "set_question(blah, blah) didn't set question on existing landmark")
		self.assertEqual(self.l["answer"], "yes", "set_question(blah) changed answer on existing landmark")
	
	def test_set_ans_existing_landmark(self):
		self.mock.set_question(0, 0, None, "bar")
		self.assertEqual(self.l["question"], "am i uwm?", "set_question(None, blah) changed question on existing landmark")
		self.assertEqual(self.l["answer"], "bar", "set_question(None, blah) didn't set answer on existing landmark")
	
	def test_set_q_and_a_new_landmark(self):
		tmp = self.mock.create_landmark(0, "foo", "bar")["landmark_id"]
		self.mock.set_question(tmp, 0, "foo", "bar")
		self.assertEqual(self.g["landmarks"][tmp]["question"], "foo", "set_question(blah, blah) didn't set question on created landmark")
		self.assertEqual(self.g["landmarks"][tmp]["answer"], "bar", "set_question(blah, blah) didn't set answer on created landmark")
	
	def test_set_q_new_landmark(self):
		tmp = self.mock.create_landmark(0, "foo", "bar")["landmark_id"]
		self.mock.set_question(tmp, 0, "foo", None)
		self.assertEqual(self.g["landmarks"][tmp]["question"], "foo", "set_question(blah, blah) didn't set question on created landmark")
		self.assertEqual(self.g["landmarks"][tmp]["answer"], None, "set_question(blah) created answer on created landmark")
	
	def test_set_answer_no_question(self):
		self.l["question"] = None
		with self.assertRaises(SettingAnswerWithNoQuestionException):
			self.mock.set_question(0, 0, None, "bar")
	