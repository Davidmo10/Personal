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

        # UserWarning on similar landmark to existing in models somewhere
        # ValueError for illegal value
        # Warning for nonexistent Landmark (meaning one will be created)
        def edit_lmark(lm: Landmark, name: str, desc: str) -> bool:
            pass

        # ValueError if invalid order
        # IndexError if submitted order is longer than hunt or less than zero
        def reorder_hunt(order: [int]) -> bool:
            if len(self.hunt) != len(order):
                raise IndexError
            iMax = len(order)
            seen : [bool] = [False] * iMax
            for i in range(iMax):
                cur = order[i]
                if cur not in range(iMax):
                    raise ValueError
                if seen[cur]:
                    raise ValueError
                seen[cur] = True
                self.hunt[i].h_order = cur
            for h in self.hunt:
                h.save()
            return True

        # ValueError for illegal value
        # IndexError for illegal landmark
        def edit_clue(lm: Landmark, value: str) -> bool:
            if type(value) != str:
                raise ValueError
            if Hunt.objects.filter(lmark = lm, game = self.dtls):
                raise IndexError
            c = Clue.objects.filter(lmark = lm)
            if c.count() == 0:
                c = Clue(lmark = lm, value = value)
                c.save()
            else:
                c = c.first()
                c.value = value
                c.save()
            return True


        # ValueError for illegal value
        # IndexError for illegal landmark
        def edit_conf(lm: Landmark, ques: str, ans: str) -> bool:
            if type(ques) != str:
                raise ValueError
            if type(ans) != str:
                raise ValueError
            if Hunt.objects.filter(lmark=lm, game=self.dtls):
                raise IndexError
            c = Confirmation.objects.filter(lmark=lm)
            if c.count() == 0:
                c = Confirmation(lmark=lm, ques = ques, ans = ans)
                c.save()
            else:
                c = c.first()
                c.ques = ques
                c.ans = ans
                c.save()
            return True


        # NameError on same name
        def mk_team(name: str, pwd: str) -> bool:
            if User.objects.filter(name = name).count() != 0:
                raise NameError
            u = User(name = name, pwd = pwd)
            u.save()
            s = Status(team = u, game = self.dtls)
            s.save()
            return True

        # KeyError for nonexistent team
        # KeyError for team not in game
        def rm_team(team: User) -> bool:
            try:
                u = User.objects.get(pk = team.pk)
                if Status.objects.filter(team = team, game = self.dtls).count() == 0:
                    raise KeyError
                u.delete()
            except:
                raise KeyError
            return True


        # KeyError on nonexistent team
        # KeyError if team not in game
        # ValueError on illegal values
        def edit_team_creds(team: User, name: str, pwd: str) -> bool:
            try:
                u = User.objects.get(pk = team.pk)
                if Status.objects.filter(team = team, game = self.dtls).count() == 0:
                    raise KeyError
            except:
                raise KeyError
            if type(name) != str:
                raise ValueError
            if type(pwd) != str:
                raise ValueError
            if name.strip() == '':
                raise ValueError
            if pwd.strip() == '':
                raise ValueError
            u.name = name
            u.pwd = pwd
            u.save()
            return True

        # NameError on same name
        # ValueError on non string
        def mk_score_sch(name: str) -> bool:
            if type(name) != str:
                raise ValueError
            if ScoreScheme.objects.filter(name = name).count() != 0:
                raise NameError
            s = ScoreScheme(name = name)
            s = save()
            return True

        # KeyError on nonexistent scheme
        # EnvironmentError if another game is using the same scheme
        # ValueError on non-float values
        def edit_score_sch(scheme: str, wrong: float, right: float, plc_num: float, ans_time: float,
                           gm_time: float) -> bool:
            try:
                s = ScoreScheme.objects.get(name = scheme)
            except:
                raise KeyError
            if type(wrong) != float or type(right) != float or type(plc_num) != float or type(ans_time) != float or type(gm_time) != float:
                raise ValueError
            if GameDetails.objects.filter(scheme = s).exclude(name = self.name) != 0:
                raise EnvironmentError
            s.right = right
            s.wrong = wrong
            s.place_numerator = plc_num
            s.ans_per_sec = ans_time
            s.game_per_sec = gm_time
            s.save()
            return True

        def req_status() -> [Status]:
            pass

        def req_hunt() -> [Hunt]:
            pass

        # ValueError on illegal values
        def edit(name: str, desc: str) -> bool:
            if type(name) != str or type(desc) is not str:
                raise ValueError
            self.dtls.name = name
            self.dtls.desc = desc
            self.dtls.save()
            return True

        # UserWarning if Game in progress
        def start() -> bool:
            if self.is_on():
                raise UserWarning
            self.dtls.on = True
            self.dtls.save()
            return True


        # UserWarning if Game not in progress
        def stop() -> bool:
            if not self.is_on():
                raise UserWarning
            self.dtls.on = False
            self.dtls.save()
            return True

        def is_on() -> bool:
            return self.dtls.on

        # UserWarning if team not done with game
        # KeyError if nonexistent team
        # KeyError if team not in game
        def set_winner(team: User) -> bool:
            pass