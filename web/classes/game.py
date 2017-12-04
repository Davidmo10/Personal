import web.itfs.gameToMakerSession as GTMS
import web.itfs.gameToTeamSession as GTTS
from django.db import models
from web.models import *

class Game(GTMS.ITF, GTTS.ITF):

    def __init__(self, dtls: GameDetails):
        self.dtls = dtls
        self.maker : User = dtls.maker
        self.name : str = dtls.name
        self.desc : str= dtls.desc
        self.on : bool = dtls.on
        self.players : [Status] = []
        self.scheme : ScoreScheme = dtls.scheme
        self.hunt : [Landmark] = []

        sel : models.QuerySet = Status.objects.filter(game = dtls)
        for s in sel:
            self.players.append(s)
        sel : models.QuerySet = Hunt.objects.filter(game = dtls).order_by('h_order')
        for s in sel:
            self.hunt.append(s)

    def calc_score_entry(self, entry: LmScore) -> float:
        output : float = 0
        if entry.correct:
            output = output + self.scheme.right
        else:
            output = output + self.scheme.wrong
        output = output + self.scheme.ans_per_sec * entry.time
        return output

    def process_team_progress(self, team: User):
        progress = LmScore.objects.filter(game = self.dtls, team = team).order_by('which', 'correct')
        s = Status.objects.get(team = team)
        output : [{str, str, float}] = []
        for p in progress:
            lm = self.hunt[p.which].lmark.name
            if p.which == s.cur:
                lm = "********"
            if p.correct:
                corr = "Correct!"
            else:
                corr = "Incorrect"
            score = self.calc_score_entry(p)
            output.append({'lm' : lm, 'right' : corr, 'score' : score, 'order' : p.which})
        return output