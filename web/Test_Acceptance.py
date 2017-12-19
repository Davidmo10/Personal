from django.test import TestCase
from web.models import *
from web.classes.game import Game


class UserLoginTests(TestCase):
    def test_login_maker(self):
        # given the gameMaker has entered a valid username
        # and has entered a valid password
        # and is_mkr is true
        # Login(request) returns a response on the server
        # allowing the Game Maker to successfully log in
        pass

    def test_logout_maker(self):
        # Game Maker selects logout link
        # game maker successfully logs out of game (through Logout method in do(?))
        pass

    def test_login_team(self):
        # given the TeamUser has entered a valid username
        # and has entered a valid password
        # and is_mkr is false
        # Login(request) returns a response on the server
        # allowing the TeamUser to successfully log in
        pass

    def test_logout_team(self):
        # Team User selects logout link
        # Team User successfully logs out of game (through Logout method in do)
        pass

class TestGameLandmark(TestCase):
    def setUp(self):
        user = User(name="mkr0", pwd="pwd0", is_mkr=True)
        user.save()
        scheme = ScoreScheme()
        scheme.save()
        u = GameDetails(name="name0", desc="desc0", on=True, winner=10, maker=user, scheme=scheme)
        self.game = Game(u)

    def tearDown(self):
        Status.objects.all().delete()
        Hunt.objects.all().delete()
        Clue.objects.all().delete()
        Confirmation.objects.all().delete()
        Landmark.objects.all().delete()
        GameDetails.objects.all().delete()
        ScoreScheme.objects.all().delete()
        User.objects.all().delete()
        LmScore.objects.all().delete()


    def test_make_landmark(self):
        lmark1 = Landmark(name = None , desc = None)
        self.game.edit_lmark(lmark1,"mark1","desc1")
        self.assertEquals(self.game.hunt[0].name,"mark1")

    def test_make_landmark_errors(self):
        lmark1 = Landmark(name=None, desc=None)
        self.assertRaises(ValueError,self.game.edit_lmark(lmark1, "mark1",1))
        self.game.edit_lmark(lmark1,"mark1","desc1")
        lmark2 = Landmark(name="mark1", desc="desc1")
        self.assertRaises(NameError,self.game.edit_lmark(lmark2,"mark2","desc2"))

    def test_remove_landmark(self):
        lmark1 = Landmark(name=None, desc=None)
        self.game.edit_lmark(lmark1, "mark1", "desc1")
        self.assertRaises(IndexError,self.game.rm_lmark(-1))
        self.game.rm_lmark(0)
        self.assertEquals(len(self.game.hunt),0)

class TestGameReorder(TestCase):
    def setUp(self):
        user = User(name="mkr0", pwd="pwd0", is_mkr=True)
        user.save()
        u = GameDetails(name="name0", desc="desc0", on=True, winner=10, maker=user, scheme=None)
        self.game = Game(u)


    def tearDown(self):
        User.objects.all().delete()
        GameDetails.objects.all().delete()
        Landmark.objects.all().delete()
        Clue.objects.all().delete()


    def test_reorder_hunt(self):
        lmark1 = Landmark(name=None, desc=None)
        lmark2 = Landmark(name=None, desc=None)
        lmark3 = Landmark(name=None, desc=None)
        order = [1, 2, 0]
        self.game.reorder_hunt(order)
        self.assertEquals(self.game.hunt[0].name,"mark2")
        self.assertEquals(self.game.hunt[1].name,"mark3")
        self.assertEquals(self.game.hunt[2].name,"mark1")

    def test_reorder_Errors(self):
        lmark1 = Landmark(name=None, desc=None)
        lmark2 = Landmark(name=None, desc=None)
        lmark3 = Landmark(name=None, desc=None)
        self.game.edit_lmark(lmark1, "mark1", "desc1")
        self.game.edit_lmark(lmark2, "mark2", "desc2")
        self.game.edit_lmark(lmark3, "mark3", "desc3")
        order = [0, 2, 1, 3]
        self.assertRaises(IndexError, self.game.reorder_hunt(order))
        order = [0, 1, 4]
        self.assertRaises(ValueError, self.game.reorder_hunt(order))

class TestGameClue(TestCase):
    def setUp(self):
        user = User(name="mkr0", pwd="pwd0", is_mkr=True)
        user.save()
        u = GameDetails(name="name0", desc="desc0", on=True, winner=10, maker=user, scheme=None)
        self.game = Game(u)


    def tearDown(self):
        User.objects.all().delete()
        GameDetails.objects.all().delete()
        Landmark.objects.all().delete()
        Clue.objects.all().delete()

    def test_edit_clue(self):
        lmark1 = Landmark(name = None,desc = None)
        lmark1.save()
        self.game.edit_lmark(lmark1,"mark1","desc1")
        clue1 = Clue(lmark = lmark1, value = "clue1")
        clue1.save()
        self.game.edit_clue(lmark1,"A math problem")
        c = Clue.objects.filter(lmark=lmark1)
        c = c.first()
        self.assertEquals(c.value,"clue1","Clue was not properly changed")

    def test_edit_clue_errors(self):
        lmark1 = Landmark(name=None, desc=None)
        lmark1.save()
        self.assertRaises(IndexError,self.game.edit_clue(lmark1,"Test"))
        self.game.edit_lmark(lmark1,"lmark1","desc1")
        self.assertRaises(ValueError,self.game.edit_clue(lmark1,1))

    def test_add_clue(self):
        lmark1 = Landmark(name=None, desc=None)
        lmark1.save()
        self.game.edit_lmark(lmark1, "mark1", "desc1")
        self.game.edit_clue(lmark1,"A math problem")
        c = Clue.objects.filter(lmark=lmark1)
        c = c.first()
        self.assertEquals(c.value, "A math problem", "Clue was not properly added")

class TestGameConfirmation(TestCase):

    def setUp(self):
        user = User(name="mkr0", pwd="pwd0", is_mkr=True)
        user.save()
        u = GameDetails(name="name0", desc="desc0", on=True, winner=10, maker=user, scheme=None)
        self.game = Game(u)

    def tearDown(self):
        Status.objects.all().delete()
        Hunt.objects.all().delete()
        Clue.objects.all().delete()
        Confirmation.objects.all().delete()
        Landmark.objects.all().delete()
        GameDetails.objects.all().delete()
        ScoreScheme.objects.all().delete()
        User.objects.all().delete()
        LmScore.objects.all().delete()

    def test_add_confirmation(self):
        # as a Game Maker I can successfully edit a confirmation
        lmark1 = Landmark(name=None, desc=None)
        lmark1.save()
        self.game.edit_lmark(lmark1,"lmark1","desc1")
        self.game.edit_conf(lmark1,"What is two plus two?","four")
        c = Confirmation.objects.filter(lmark=lmark1)
        c = c.first()
        self.assertEquals(c.ques,"What is two plus two?","Error setting confirmation")
        self.assertEquals(c.ans,"four","Error setting confirmation")


    def test_edit_confirmation(self):
        lmark1 = Landmark(name=None, desc=None)
        lmark1.save()
        self.game.edit_lmark(lmark1, "lmark1", "desc1")
        self.game.edit_conf(lmark1, "What is two plus two?", "four")
        self.game.edit_conf(lmark1,"What is two plus three?","five")
        c = Confirmation.objects.filter(lmark=lmark1)
        c = c.first()
        self.assertEquals(c.ques, "What is two plus three?", "Error setting confirmation")
        self.assertEquals(c.ans, "five", "Error setting confirmation")

    def test_edit_confirmation_errors(self):
        lmark1 = Landmark(name=None, desc=None)
        lmark1.save()
        self.assertRaises(IndexError, self.game.edit_conf(lmark1, "What is two plus two?", "four"))
        self.assertRaises(ValueError, self.game.edit_conf(lmark1, 1, "four"))
        self.assertRaises(ValueError, self.game.edit_conf(lmark1, "What is two plus two?", 1))

class TestTeam(TestCase):

    def setUp(self):
        user = User(name="mkr0", pwd="pwd0", is_mkr=True)
        user.save()
        u = GameDetails(name="name0", desc="desc0", on=True, winner=10, maker=user, scheme=None)
        self.game = Game(u)

    def tearDown(self):
        Status.objects.all().delete()
        Hunt.objects.all().delete()
        Clue.objects.all().delete()
        Confirmation.objects.all().delete()
        Landmark.objects.all().delete()
        GameDetails.objects.all().delete()
        ScoreScheme.objects.all().delete()
        User.objects.all().delete()
        LmScore.objects.all().delete()


    def test_make_team(self):
        # as a Game Maker I can successfully create a team
        self.game.mk_team("name1","pwd1")
        teams = User.objects.filter(name = "name1")
        teams = teams.first()
        self.assertEquals(teams.count(),1)

    def test_make_team_error(self):
        self.game.mk_team("name1", "pwd1")
        self.assertRaises(NameError,self.game.mk_team("name1","pwd1"))


    def test_remove_team(self):
        self.game.mk_team("name1", "pwd1")
        teams = User.objects.filter(name="name1")
        teams = teams.first()
        self.game.rm_team(teams)
        teams = User.objects.filter(name="name1")
        self.assertEquals(teams.count(),0)

    def test_remove_team_errors(self):
        self.game.mk_team("name1","pwd1")
        teams = User.objects.filter(name="name1")
        teams = teams.first()
        self.assertRaises(KeyError,self.game.rm_team(teams))


    def test_edit_team_credentials(self):
        # as a Game Maker I can successfully edit team credentials
        self.game.mk_team("name1","pwd1")
        teams = User.objects.filter(name="name1")
        teams = teams.first()
        self.game.edit_team_creds(teams,"name2","pwd2")
        teams = User.objects.filter(name="name2")
        self.assertEquals(teams.count(),1)

    def test_edit_team_credentials_errors(self):
        team1 = User(name = "1",pwd = "1")
        self.assertRaises(ValueError,self.game.edit_team_creds(team1,1,"pwd2"))
        self.assertRaises(ValueError, self.game.edit_team_creds(team1, "team2", 1))

    def test_make_score_scheme(self):
        self.game.mk_score_sch("scheme1")
        self.assertRaises(ValueError,self.game.mk_score_sch(1))
        s = ScoreScheme.objects.filter(name="scheme1")


    def test_edit_score_scheme(self):
        # as a Game Maker I can successfully edit a scoring scheme of game
        s = ScoreScheme()
        self.assertRaises(EnvironmentError,self.game.edit_score_sch(s))
        self.game.mk_score_sch("scheme1")
        s = ScoreScheme.objects.filter(name="scheme1")
        s = s.first()
        self.game.edit_score_sch(s)
        self.assertEqual(self.game.scheme.name,"scheme1","Scheme not set correctly")

 def test_edit_game_name_and_description(self):
        name = "newName"
        desc = "new game description"
        testName = 3 #cannot do integer value for this
        testDesc = 4 #must be string
        self.assertRaises(UserError, self.game.edit(testName, testDesc))
        self.game.edit(name, desc)
        self.assertEqual(self.u.name, "newName", "New name of game not set correctly")
        self.assertEqual(self.u.desc, "new game description", "New description of game not set correctly")

    def test_start_game(self):
        self.u.on = True
        self.assertRaises(UserWarning, self.game.start())
        self.u.on = False
        self.assertEquals(self.game.start(), True, "The game did not successfully start - game was already on")

    def test_stop_game(self):
        self.u.on = False
        self.assertRaises(UserWarning, self.game.stop())
        self.u.on = True
        self.assertEquals(self.game.stop(), True, "The game did not successfully stop - game was already off")

    def test_game_is_on(self):
        self.u.on = True
        self.assertEquals(self.game.is_on(), True, "Game is not on")
        self.u.on = False
        self.assertEquals(self.game.is_on(), False, "Game is on")

class TestTeam(TestCase):
    def test_create_team(self):
        u = User(name="team0", pwd="pwd0")
        self.assertEquals(u.name, "team0")
        self.assertEquals(u.pwd, "pwd0")
        self.assertFalse(u.is_mkr)
        self.assertEquals(u.__str__(), '< User ModInst (Team) :: name = ' + u.name + ' >')

    def test_create_maker(self):
        u = User(name="mkr0", pwd="pwd0", is_mkr=True)
        self.assertTrue(u.is_mkr)
        self.assertEquals(u.__str__(), '< User ModInst (Maker) :: name = ' + u.name + ' >')


class TestLandmark(TestCase):
    def test_create_landmark(self):
        u = Landmark(name="landmark0", desc="a test landmark")
        self.assertEquals(u.name, "landmark0")
        self.assertEquals(u.desc, "a test landmark")
        self.assertEquals(u.__str__(), 'Landmark ModInst :: name = ' + u.name)


class TestClue(TestCase):
    def test_create_clue(self):
        landmark1 = Landmark(name="landmark0", desc="a test landmark")
        u = Clue(lmark=landmark1, value="a clue")
        self.assertEquals(u.lmark.name, "landmark0", "Wrong landmark assigned")
        self.assertEquals(u.lmark.desc, "a test landmark", "Wrong landmark assigned")
        self.assertEquals(u.value, "a clue")
        self.assertEquals(u.__str__(), 'ModInst :: value = ' + u.value + ', lmark = ' + u.lmark.name)


class TestConfirmation(TestCase):
    def test_create_confirmation(self):
        landmark1 = Landmark(name="landmark0", desc="a test landmark")
        u = Confirmation(lmark=landmark1, ques="What is 2 + 2?", ans="4")

        self.assertEquals(u.lmark.name, "landmark0")
        self.assertEquals(u.lmark.desc, "a test landmark")
        self.assertEquals(u.ques, "What is 2 + 2?")
        self.assertEquals(u.ans, "4")

        self.assertEquals(u.__str__(),
                         'Clue ModInst :: ques = ' + u.ques + ', ans = ' + u.ans + ', lmark = ' + u.lmark.name)


class TestScoreScheme(TestCase):
    def test_create_score_scheme(self):
        u = ScoreScheme(name="scoring1", wrong=1, right=2, place_numerator=3, ans_per_sec=4, game_per_sec=5)

        self.assertEquals(u.name, "scoring1")
        self.assertEquals(u.wrong, 1)
        self.assertEquals(u.right, 2)
        self.assertEquals(u.place_numerator, 3)
        self.assertEquals(u.ans_per_sec, 4)
        self.assertEquals(u.game_per_sec, 5)

        self.assertEquals(u.__str__(), 'ScoreScheme ModInst :: name = ' + u.name)

    def test_default_score_scheme(self):
        u = ScoreScheme()
        self.assertEquals(u.name, "default")
        self.assertEquals(u.wrong, -10)
        self.assertEquals(u.right, 50)
        self.assertEquals(u.place_numerator, 100)
        self.assertEquals(u.ans_per_sec, -0.1)
        self.assertEquals(u.game_per_sec, -.00001)


class TestGameDetails(TestCase):
    def test_create_game_details(self):
        user = User(name="mkr0", pwd="pwd0", is_mkr=True)
        user.save()

        scheme1 = ScoreScheme()
        scheme1.save()

        u = GameDetails(name="name0", desc="desc0", on=True, winner=10, maker=user, scheme=scheme1)

        self.assertEquals(u.name, "name0")
        self.assertEquals(u.desc, "desc0")
        self.assertTrue(u.on)
        self.assertEquals(u.winner, 10)
        self.assertEquals(u.maker.pk, user.pk, "Wrong user assigned to game details")
        self.assertEquals(u.scheme.pk, scheme1.pk, "Wrong scheme assigned to game details")
        self.assertEquals(u.__str__(), 'Game ModInst :: name = ' + u.name + ', maker = ' + u.maker.name)

    def test_default_create_game_details(self):
        u = GameDetails(name="name0", desc="desc0", maker=None, scheme=None)
        self.assertFalse(u.on)
        self.assertEquals(u.winner, -1)


class TestStatus(TestCase):
    def test_create_status(self):
        team = User(name="team0", pwd="pwd0")
        team.save()

        game = GameDetails(name="name0", desc="desc0", maker=None, scheme=None)
        game.save()

        status = Status(game=game, team=team, cur=1, playing=True, score=100)

        self.assertEquals(status.cur, 1)
        self.assertTrue(status.playing)
        self.assertEquals(status.score, 100)
        self.assertEquals(status.game.pk, game.pk, "Wrong game initiated with status")
        self.assertEquals(status.team.pk, team.pk, "Wrong team initiated with status")

        self.assertEquals(status.__str__(),
                         'Status ModInst ::  team = ' + status.team.name + ', game = ' + status.game.name + ', current = ' + str(
                             status.cur))

    def test_default_create_status(self):
        status = Status(game=None, team=None)

        self.assertEquals(status.pending, None)
        self.assertFalse(status.playing)
        self.assertEquals(status.score, 0)


class TestHunt(TestCase):
    def test_create_hunt(self):
        landmark1 = Landmark(name="landmark0", desc="a test landmark")
        landmark1.save()
        game = GameDetails(name="name0", desc="desc0", maker=None, scheme=None)
        game.save()
        hunt = Hunt(lmark=landmark1, game=game, h_order=-1)

        self.assertEquals(hunt.lmark.pk, landmark1.pk, "Wrong landmark assigned")
        self.assertEquals(hunt.game.pk, game.pk, "Wrong game assigned")
        self.assertEquals(hunt.h_order, -1)

        self.assertEquals(hunt.__str__(), 'Hunt ModInst :: h_order = ' + str(
            hunt.h_order) + 'game = ' + hunt.game.name + 'lmark = ' + hunt.lmark.name)


class TestLmScore(TestCase):
    def test_create_LmScore(self):
        game = GameDetails(name="name0", desc="desc0", maker=None, scheme=None)
        game.save()

        team = User(name="team0", pwd="pwd0")
        team.save()

        score = LmScore(game=game, team=team, which=0, correct=False, time=0)
        self.assertEquals(score.game.pk, game.pk, "Wrong game assigned")
        self.assertEquals(score.team.pk, team.pk, "Wrong team assigned")
        self.assertEquals(score.which, 0)
        self.assertEquals(score.correct, False)
        self.assertEquals(score.time, 0)
