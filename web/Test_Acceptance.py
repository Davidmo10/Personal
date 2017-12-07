from django.test import TestCase

class UserLoginTests(TestCase):

	def test_login_maker(self):
		#given the gameMaker has entered a valid username
		#and has entered a valid password
		#and is_mkr is true
		#Login(request) returns a response on the server
		#allowing the Game Maker to successfully log in
		pass
	
	def test_logout_maker(self):
		#Game Maker selects logout link 
		#game maker successfully logs out of game (through Logout method in do(?))
		pass

	def test_login_team(self):
		#given the TeamUser has entered a valid username
		#and has entered a valid password
		#and is_mkr is false
		#Login(request) returns a response on the server
		#allowing the TeamUser to successfully log in
		pass

	def test_logout_team(self):
		#Team User selects logout link
		#Team User successfully logs out of game (through Logout method in do)
		pass


class GameMakerTests(TestCase):

	def test_make_landmark(self):
		#as a Game Maker I can successfully create a landmark
		pass

	def test_reorder_hunt(self):
		#as a Game Maker I can successfully reorder a hunt
		pass

	def test_edit_clue(self):
		#as a Game Maker I can successfully edit a clue
		pass

	def test_edit_confirmation(self):
		#as a Game Maker I can successfully edit a confirmation
		pass

	def test_make_team(self):
		#as a Game Maker I can successfully create a team
		pass

	def test_remove_team(self):
		#as a Game Maker I can successfully remove a team
		pass

	def test_edit_team_credentials(self):
		#as a Game Maker I can successfully edit team credentials
		pass

	def test_make_score_scheme(self):
		#as a Game Maker I can successfully add a scoring scheme to game
		pass

	def test_edit_score_scheme(self):
		#as a Game Maker I can successfully edit a scorring scheme of game
		pass

	def test_request_status(self):
		#as a Game Maker I can get the status of a current game
		pass

	def test_edit_game_name_and_description(self):
		#as a Game Maker I can successfully edit name of game
		#as a Game Maker I can successfully edit description of game
		pass

	def test_start_game(self):
		#as a Game Maker I can set game staus to on
		pass

	def test_stop_game(self):
		#as a Game Maker I can set game status to off
		pass

	def test_game_is_on(self):
		#as a Game Maker I can check the status of a game
		pass


class TeamTests(TestCase):

	def test_request_clue(self):
		#as a Team I can successfully request a clue
		pass

	def test_request_question(self):
		#as a Team I can successfully request a question
		pass

	def test_submit_answer(self):
		#as a Team I can successfully submit an answer
		pass

	def test_edit_credentials(self):
		#as a Team I can edit username
		#as a Team I can edit password
		pass

	def test_forfeit(self):
		#as a Team I can forfeit the game, removing team from game
		pass

	def test_is_on(self):
		#as a Team I can check if on
		pass
	
class TestTeam(TestCase):

    def test_create_team(self):
        u = User(name = "team0", pwd = "pwd0")
        self.assertEqual(u.name, "team0")
        self.assertEqual(u.pwd, "pwd0")
        self.assertFalse(u.is_mkr)
        self.assertEqual(u.__str__(),'< User ModInst (Team) :: name = '+ u.name + ' >')

    def test_create_maker(self):
        u = User(name = "mkr0", pwd = "pwd0", is_mkr = True)
        self.assertTrue(u.is_mkr)
        self.assertEqual(u.__str__(),'< User ModInst (Maker) :: name = '+ u.name + ' >')

class TestLandmark(TestCase):

    def test_create_landmark(self):
        u = Landmark(name = "landmark0",desc = "a test landmark")
        self.assertEqual(u.name, "landmark0")
        self.assertEqual(u.desc, "a test landmark")
        self.assertEqual(u.__str__(), 'Landmark ModInst :: name = ' + u.name)

class TestClue(TestCase):

    def test_create_clue(self):
        landmark1 = Landmark(name = "landmark0",desc = "a test landmark")
        u = Clue(lmark = landmark1,value = "a clue")
        self.assertEqual(u.lmark.name, "landmark0", "Wrong landmark assigned")
        self.assertEqual(u.lmark.desc, "a test landmark","Wrong landmark assigned")
        self.assertEqual(u.value,"a clue")
        self.assertEqual(u.__str__(),'ModInst :: value = '+ u.value+ ', lmark = '+ u.lmark.name)

class TestConfirmation(TestCase):

    def test_create_confirmation(self):
        landmark1 = Landmark(name="landmark0", desc="a test landmark")
        u = Confirmation(lmark = landmark1, ques = "What is 2 + 2?", ans = "4")

        self.assertEqual(u.lmark.name, "landmark0")
        self.assertEqual(u.lmark.desc, "a test landmark")
        self.assertEqual(u.ques, "What is 2 + 2?")
        self.assertEqual(u.ans, "4")

        self.assertEqual(u.__str__(),'Clue ModInst :: ques = '+ u.ques+ ', ans = '+ u.ans+ ', lmark = '+ u.lmark.name)

class TestScoreScheme(TestCase):

    def test_create_score_scheme(self):
        u = ScoreScheme(name = "scoring1",wrong = 1, right = 2, place_numerator = 3, ans_per_sec = 4, game_per_sec = 5)

        self.assertEqual(u.name, "scoring1")
        self.assertEqual(u.wrong, 1)
        self.assertEqual(u.right, 2)
        self.assertEqual(u.place_numerator, 3)
        self.assertEqual(u.ans_per_sec, 4)
        self.assertEqual(u.game_per_sec, 5)

        self.assertEqual(u.__str__(), 'ScoreScheme ModInst :: name = ' + u.name)

    def test_default_score_scheme(self):
        u = ScoreScheme()
        self.assertEqual(u.name, "default")
        self.assertEqual(u.wrong, -10)
        self.assertEqual(u.right, 50)
        self.assertEqual(u.place_numerator, 100)
        self.assertEqual(u.ans_per_sec, -0.1)
        self.assertEqual(u.game_per_sec, -.00001)

class TestGameDetails(TestCase):

    def test_create_game_details(self):
        user = User(name="mkr0", pwd="pwd0", is_mkr=True)
        user.save()

        scheme1 = ScoreScheme()
        scheme1.save()


        u = GameDetails(name = "name0",desc = "desc0", on = True, winner = 10, maker =  user, scheme = scheme1)

        self.assertEqual(u.name, "name0")
        self.assertEqual(u.desc, "desc0")
        self.assertTrue(u.on)
        self.assertEqual(u.winner, 10)
        self.assertEqual(u.maker.pk, user.pk, "Wrong user assigned to game details")
        self.assertEqual(u.scheme.pk, scheme1.pk, "Wrong scheme assigned to game details")
        self.assertEqual(u.__str__(), 'Game ModInst :: name = ' + u.name + ', maker = ' + u.maker.name)

    def test_default_create_game_details(self):
        u = GameDetails(name="name0", desc="desc0", maker=None, scheme=None)
        self.assertFalse(u.on)
        self.assertEqual(u.winner,-1)



class TestStatus(TestCase):


    def test_create_status(self):
        team = User(name="team0", pwd="pwd0")
        team.save()

        game = GameDetails(name="name0", desc="desc0", maker=None, scheme=None)
        game.save()

        status = Status(game = game, team = team, cur = 1, playing = True, score = 100)

        self.assertEqual(status.cur,1)
        self.assertTrue(status.playing)
        self.assertEqual(status.score, 100)
        self.assertEqual(status.game.pk, game.pk, "Wrong game initiated with status")
        self.assertEqual(status.team.pk, team.pk, "Wrong team initiated with status")

        self.assertEqual(status.__str__(),'Status ModInst ::  team = '+ status.team.name + ', game = '+ status.game.name + ', current = ' + str(status.cur))

    def test_default_create_status(self):

        status = Status(game=None, team=None)

        self.assertEqual(status.pending, None)
        self.assertFalse(status.playing)
        self.assertEqual(status.score,0)

class TestHunt(TestCase):

    def test_create_hunt(self):
        landmark1 = Landmark(name="landmark0", desc="a test landmark")
        landmark1.save()
        game = GameDetails(name="name0", desc="desc0", maker=None, scheme=None)
        game.save()
        hunt = Hunt(lmark = landmark1, game = game, h_order = -1)

        self.assertEqual(hunt.lmark.pk, landmark1.pk, "Wrong landmark assigned")
        self.assertEqual(hunt.game.pk, game.pk, "Wrong game assigned")
        self.assertEqual(hunt.h_order, -1)

        self.assertEqual(hunt.__str__(), 'Hunt ModInst :: h_order = ' + str(hunt.h_order) + 'game = ' + hunt.game.name + 'lmark = ' + hunt.lmark.name)

class TestLmScore(TestCase):

    def test_create_LmScore(self):
        game = GameDetails(name="name0", desc="desc0", maker=None, scheme=None)
        game.save()

        team = User(name="team0", pwd="pwd0")
        team.save()

        score = LmScore(game = game, team = team, which = 0, correct = False, time = 0)
        self.assertEqual(score.game.pk, game.pk, "Wrong game assigned")
        self.assertEqual(score.team.pk, team.pk, "Wrong team assigned")
        self.assertEqual(score.which, 0)
        self.assertEqual(score.correct, False)
        self.assertEqual(score.time, 0)

