from django.test import TestCase
from web.models import *
from datetime import datetime as dt
from pytz import timezone as tz

class TestData:

    def __init__(self):
        pass

    @staticmethod
    def build():
        my_models = [
        User(name = "maker1", pwd="maker1pwd", is_mkr=True),
        User(name = "maker2", pwd="maker2pwd", is_mkr=True),
        User(name="team1", pwd="team1pwd"),
        User(name="team2", pwd="team2pwd"),
        User(name="team3", pwd="team3pwd"),
        User(name="team4", pwd="team4pwd"),
        User(name="team5", pwd="team5pwd"),
        User(name="team6", pwd="team6pwd"),
        User(name="team7", pwd="team7pwd"),
        User(name="team8", pwd="team8pwd"),
        User(name="team9", pwd="team9pwd"),
        User(name="team10", pwd="team10pwd"),
        User(name="team11", pwd="team11pwd"),
        User(name="team12", pwd="team12pwd"),
        User(name="team13", pwd="team13pwd"),
        User(name="team14", pwd="team14pwd"),
        ScoreScheme(),
        ScoreScheme(name = "Test scheme", wrong=-1, right=30)
        ]
        for m in my_models:
            m.save()
        tms = User.objects.filter(is_mkr = False)
        mkrs = User.objects.filter(is_mkr = True)
        s = ScoreScheme.objects.all()
        my_models = [
        GameDetails(name ="Game 1", desc="Test game 1", maker=mkrs[0], scheme=s[0]),
        GameDetails(name="Game 2", desc="Test game 2", maker=mkrs[1], scheme=s[1], on=True),
        Landmark(name="Landmark 1", desc="Test landmark 1"),
        Landmark(name="Landmark 2", desc="Test landmark 2"),
        Landmark(name="Landmark 3", desc="Test landmark 3"),
        Landmark(name="Landmark 4", desc="Test landmark 4"),
        Landmark(name="Landmark 5", desc="Test landmark 5"),
        Landmark(name="Landmark 6", desc="Test landmark 6"),
        Landmark(name="Landmark 7", desc="Test landmark 7"),
        Landmark(name="Landmark 8", desc="Test landmark 8"),
        Landmark(name="Landmark 9", desc="Test landmark 9"),
        Landmark(name="Landmark 10", desc="Test landmark 10")
        ]
        for m in my_models:
            m.save()
        gms = GameDetails.objects.all()
        lms = Landmark.objects.all()
        my_models = [
        Clue(lmark = lms[0], value="Clue 1"),
        Clue(lmark = lms[2-1], value="Clue 2"),
        Clue(lmark = lms[3-1], value="Clue 3"),
        Clue(lmark = lms[4-1], value="Clue 4"),
        Clue(lmark = lms[5-1], value="Clue 5"),
        Clue(lmark = lms[6-1], value="Clue 6"),
        Clue(lmark = lms[7-1], value="Clue 7"),
        Clue(lmark = lms[8-1], value="Clue 8"),
        Clue(lmark = lms[9-1], value="Clue 9"),
        Clue(lmark = lms[10-1], value="Clue 10"),
        Confirmation(lmark = lms[1-1], ques = "Question 1", ans = "Answer 1"),
        Confirmation(lmark = lms[2-1], ques = "Question 2", ans = "Answer 2"),
        Confirmation(lmark = lms[3-1], ques = "Question 3", ans = "Answer 3"),
        Confirmation(lmark = lms[4-1], ques = "Question 4", ans = "Answer 4"),
        Confirmation(lmark = lms[5-1], ques = "Question 5", ans = "Answer 5"),
        Confirmation(lmark = lms[6-1], ques = "Question 6", ans = "Answer 6"),
        Confirmation(lmark = lms[7-1], ques = "Question 7", ans = "Answer 7"),
        Confirmation(lmark = lms[8-1], ques = "Question 8", ans = "Answer 8"),
        Confirmation(lmark = lms[9-1], ques = "Question 9", ans = "Answer 9"),
        Confirmation(lmark = lms[10-1], ques = "Question 10", ans = "Answer 10"),
        Hunt(lmark = lms[1-1], game = gms[1-1]),
        Hunt(lmark = lms[2-1], game = gms[1-1]),
        Hunt(lmark = lms[3-1], game = gms[1-1]),
        Hunt(lmark = lms[4-1], game = gms[1-1]),
        Hunt(lmark = lms[5-1], game = gms[2-1]),
        Hunt(lmark = lms[6-1], game = gms[2-1]),
        Hunt(lmark = lms[7-1], game = gms[2-1]),
        Hunt(lmark = lms[8-1], game = gms[2-1]),
        Hunt(lmark = lms[9-1], game = gms[2-1]),
        Hunt(lmark = lms[10-1], game = gms[2-1]),
        Status(game = gms[1-1], team = tms[1-1]),
        Status(game = gms[1-1], team = tms[2-1]),
        Status(game = gms[1-1], team = tms[3-1]),
        Status(game = gms[1-1], team = tms[4-1]),
        Status(game = gms[1-1], team = tms[5-1]),
        Status(game = gms[1-1], team = tms[6-1]),
        Status(game = gms[1-1], team = tms[7-1]),
        Status(game = gms[1-1], team = tms[8-1]),
        Status(game = gms[1], team = tms[8], playing=True),
        Status(game = gms[1], team = tms[9], playing=True, cur = 4),
        Status(game = gms[1], team = tms[10], playing=True, cur = 4, pending = dt.now(tz('US/Central'))),
        Status(game = gms[1], team = tms[11], playing=True, pending = dt.now(tz('US/Central'))),
        Status(game = gms[1], team = tms[12], cur = 5),
        Status(game = gms[1], team = tms[13], cur = 3),
        LmScore(game = gms[1], team=tms[9], which=1, correct=True, time=56),
        LmScore(game = gms[1], team=tms[9], which=2, correct=False, time=102),
        LmScore(game = gms[1], team=tms[9], which=2, correct=True, time=88),
        LmScore(game = gms[1], team=tms[9], which=3, correct=True, time=33),
        LmScore(game = gms[1], team=tms[9], which=4, correct=False, time=12),
        ]
        for m in my_models:
            m.save()

    @staticmethod
    def huh():
        print("Game 1 -> landmarks 1-4, teams 1-8, maker 1, not started\n")
        print("Game 2 -> landmarks 5-10, teams 9-14, maker 2, started, teams in various states of play\n")
        print("All names are of the form 'Game 1', 'Maker 2', Team 8', etc")

    @staticmethod
    def wipe():
        Status.objects.all().delete()
        Hunt.objects.all().delete()
        Clue.objects.all().delete()
        Confirmation.objects.all().delete()
        Landmark.objects.all().delete()
        GameDetails.objects.all().delete()
        ScoreScheme.objects.all().delete()
        User.objects.all().delete()
        LmScore.objects.all().delete()
