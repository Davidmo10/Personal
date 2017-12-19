from datetime import datetime as dt

from pytz import timezone as tz

import web.itfs.gameToMakerSession as GTMS
import web.itfs.gameToTeamSession as GTTS
from web.models import *


class Game(GTMS.ITF, GTTS.ITF):
	def __init__(self, dtls: GameDetails):
		self.dtls = dtls
		self.maker: User = dtls.maker
		self.name: str = dtls.name
		self.desc: str = dtls.desc
		self.on: bool = dtls.on
		self.players: [Status] = []
		self.scheme: ScoreScheme = dtls.scheme
		self.landmarks: [Landmark] = []

		sel: models.QuerySet = Status.objects.filter(game=dtls)
		for s in sel:
			self.players.append(s)
		sel: models.QuerySet = Hunt.objects.filter(game=dtls).order_by('h_order')
		for s in sel:
			self.landmarks.append(s)

	def calc_score_entry(self, entry: LmScore) -> float:
		output: float = 0
		if entry.correct:
			output = output + self.scheme.right
		else:
			output = output + self.scheme.wrong
		output = output + self.scheme.ans_per_sec * entry.time
		return output

	def req_team_progress(self, team: User):
		progress = LmScore.objects.filter(game=self.dtls, team=team).order_by('which', 'correct')
		s = Status.objects.get(team=team)
		output: [{str, str, float}] = []
		for p in progress:
			lm = self.landmarks[p.which].lmark.name
			if p.which == s.cur:
				lm = "********"
			if p.correct:
				corr = "Correct!"
			else:
				corr = "Incorrect"
			score = self.calc_score_entry(p)
			output.append({'lm': lm, 'right': corr, 'score': score, 'order': p.which})
		return output

	# ValueError for illegal value
	# Warning for nonexistent Landmark (meaning one will be created)
	def edit_lmark(self, lm: Landmark, name: str, desc: str) -> bool:
		if lm not in Landmark.objects.all():
			if Landmark.objects.filter(name=lm.name).count() != 0:
				raise NameError("A landmark with that name already exists")

		if type(name) != str or type(desc) != str or name.strip() == "" or desc.strip() == "":
			raise ValueError("Types for landmark must be string")

		lm.save()
		if Hunt.objects.filter(lmark=lm, game=self.dtls).count() == 0:
			h = Hunt(lmark=lm, game=self.dtls)
			h.save()

		return True

	# ValueError if invalid order
	# IndexError if submitted order is longer than hunt or less than zero
	def reorder_hunt(self, order: [int]) -> bool:
		if len(self.landmarks) != len(order):
			raise IndexError("Invalid order")
		i_max = len(order)
		seen: [bool] = [False] * i_max
		for i in range(i_max):
			cur = order[i]
			if cur not in range(i_max):
				raise ValueError("Invalid order")
			if seen[cur]:
				raise ValueError("Invalid order")
			seen[cur] = True
			self.landmarks[i].h_order = cur
		for h in self.landmarks:
			h.save()
		return True

	# ValueError for illegal value
	# IndexError for illegal landmark
	def edit_clue(self, lm: Landmark, value: str) -> bool:
		if type(value) != str:
			raise ValueError("Invalid clue value")
		if Hunt.objects.filter(lmark=lm, game=self.dtls).count() == 0:
			raise IndexError("That landmark is not in this game")
		c = Clue.objects.filter(lmark=lm)
		if c.count() == 0:
			c = Clue(lmark=lm, value=value)
			c.save()
		else:
			c = c.first()
			c.value = value
			c.save()
		return True

	# ValueError for illegal value
	# IndexError for illegal landmark
	def edit_conf(self, lm: Landmark, ques: str, ans: str) -> bool:
		if type(ques) != str:
			raise ValueError("Invalid question")
		if type(ans) != str:
			raise ValueError("Invalid answer")
		if not Hunt.objects.filter(lmark=lm, game=self.dtls):
			raise IndexError("That landmark is not in this game")
		c = Confirmation.objects.filter(lmark=lm)
		if c.count() == 0:
			c = Confirmation(lmark=lm, ques=ques, ans=ans)
			c.save()
		else:
			c = c.first()
			c.ques = ques
			c.ans = ans
			c.save()
		return True

	# NameError on same name
	def mk_team(self, name: str, pwd: str) -> bool:
		if User.objects.filter(name=name).count() != 0:
			raise NameError("A user with that name already exists")
		u = User(name=name, pwd=pwd)
		u.save()
		s = Status(team=u, game=self.dtls, playing=self.dtls.on)
		s.save()
		return True

	def rm_lmark(self, index: int) -> bool:
		if index < 0 or index >= len(self.landmarks):
			raise IndexError("Invalid landmark to remove")
		h = Hunt.objects.get(game=self.dtls, h_order=index)
		h.delete()
		return True

	# KeyError for nonexistent team
	# KeyError for team not in game
	def rm_team(self, team: User) -> bool:
		try:
			if Status.objects.filter(game=self.dtls, team=team).count() == 0:
				raise KeyError("That team is not in a game you manage")
			team.delete()
		except Exception as e:
			if type(e) is not KeyError:
				raise KeyError("That does not exist")
			raise e
		return True

	# KeyError on nonexistent team
	# KeyError if team not in game
	# ValueError on illegal values
	def edit_team_creds(self, team: User, name: str, pwd: str) -> bool:
		try:
			u = User.objects.get(pk=team.pk)
			if Status.objects.filter(team=team, game=self.dtls).count() == 0:
				raise KeyError("That team is not in a game you manage")
		except (Status.DoesNotExist, KeyError):
			raise KeyError("That team does not exist")
		if type(name) is not str or name.strip() == "":
			raise ValueError("Illegal name")
		if type(pwd) is not str or pwd.strip() == "":
			raise ValueError("Illegal password")
		u.name = name
		u.pwd = pwd
		u.save()
		return True

	# NameError on same name
	# ValueError on non string
	def mk_score_sch(self, name: str) -> bool:
		if type(name) != str:
			raise ValueError("Invalid name")
		if ScoreScheme.objects.filter(name=name).count() != 0:
			raise NameError("That name already exists")
		s = ScoreScheme(name=name)
		s.save()
		return True

	# KeyError on nonexistent scheme
	# EnvironmentError if another game is using the same scheme
	# ValueError on non-float values
	def edit_score_sch(self, scheme: ScoreScheme) -> bool:
		if scheme.name == "default":
			raise EnvironmentError("Cannot edit default scheme")
		if type(scheme.wrong) != float or type(scheme.right) != float or type(scheme.place_numerator) != float or type(
				scheme.ans_per_sec) != float or type(scheme.game_per_sec) != float:
			raise ValueError("Invalid scoring scheme")
		if GameDetails.objects.filter(scheme=scheme).exclude(name=self.name).count() != 0:
			raise EnvironmentError("Another game is using this scoring scheme, try creating a new one")
		scheme.save()
		self.dtls.scheme = scheme
		self.dtls.save()
		self.calc_scores()
		return True

	def req_status(self, team: User) -> {GameDetails, str, bool, float}:
		try:
			u = User.objects.get(pk=team.pk)
		except User.DoesNotExist:
			raise KeyError("User does not exist")
		progress = self.req_team_progress(team)
		tot_score = 0
		for p in progress:
			tot_score = tot_score + p["score"]
		s = Status.objects.get(team=u)
		if not self.is_on():
			curtype = "gameoff"
		elif not s.playing:
			if s.cur >= len(self.landmarks):
				curtype = "done"
			else:
				curtype = "forfeited"
		elif s.pending is not None:
			curtype = "pending"
		else:
			curtype = "clue"
		return {"game": self.dtls, "pending": s.pending, "curtype": curtype, "total": tot_score}

	def req_hunt(self) -> [{str, int}]:
		output: [{str, int}] = []
		for h in self.landmarks:
			output.append({"name": h.lmark.name, "order": h.h_order})
		return output

	def req_team_statuses(self) -> [{User, Status, int}]:
		output: [{User, Status, int}] = []
		for i in range(len(self.players)):
			p = self.players[i]
			if p.cur == -1:
				lmreport = "Done"
			else:
				lmreport = self.landmarks[p.cur].lmark.name
			output.append({"tm": p.team, "st": p, "index": i, "lm": lmreport})
		return output

	# ValueError on illegal values
	def edit(self, name: str, desc: str) -> bool:
		if type(name) != str or type(desc) is not str:
			raise ValueError("Illegal name or description")
		self.dtls.name = name
		self.dtls.desc = desc
		self.dtls.save()
		return True

	# UserWarning if Game in progress
	def start(self) -> bool:
		if self.is_on():
			raise UserWarning("This game is already in progress")
		self.dtls.on = True
		self.dtls.startTime = dt.now()
		self.dtls.save()
		return True

	# UserWarning if Game not in progress
	def stop(self) -> bool:
		if not self.is_on():
			raise UserWarning("This game is not in progress")
		self.dtls.on = False
		self.dtls.save()
		return True

	def is_on(self) -> bool:
		return self.dtls.on

	# UserWarning if team not done with game
	# KeyError if nonexistent team
	# KeyError if team not in game
	def set_winner_by_score(self, team: User) -> User:
		try:
			if Status.objects.filter(team=team, game=self.dtls).count() == 0:
				raise KeyError("That team is not in a game you manage")
		except (Status.DoesNotExist, KeyError):
			raise KeyError("Team does not exist")

		stat = Status.objects.filter(game__name=self.dtls)
		scores = []
		team = []

		for x in stat:
			scores.append(x.score)
			team.append(x.team.name)

		# because all scores are currently 0 - the first team will be returned
		return team[scores.index(max(scores))]

	def set_winner(self, team: User) -> bool:
		self.dtls.winner = team.pk
		self.dtls.on = False
		self.dtls.save()
		return True

	# ReferenceError if team is not playing
	# IndexError if game is not on
	# EnvironmentError if no clue
	# KeyError if team has question pending
	def req_clue(self, team: User) -> Clue:
		if not self.is_on():
			raise IndexError("Game is not on")
		s = Status.objects.filter(team=team, game=self.dtls)
		if s.count() == 0:
			raise ReferenceError("You are not in this game")
		s = s.first()
		if not s.playing:
			raise ReferenceError("You may not have a clue after forfeiting")
		if s.pending is not None:
			raise KeyError("You may not have a clue while a question is pending")
		lm = self.landmarks[s.cur].lmark
		try:
			c = Clue.objects.get(lmark=lm)
			return c.value
		except Clue.DoesNotExist:
			raise EnvironmentError("There is no clue associated with this landmark")

	# ReferenceError if team is not playing
	# IndexError if game is not on
	# EnvironmentError if no confirmation
	def req_ques(self, team: User) -> str:
		if not self.is_on():
			raise IndexError("Game is not on")
		s = Status.objects.filter(team=team, game=self.dtls)
		if s.count() == 0:
			raise ReferenceError("You are not in this game")
		s = s.first()
		if not s.playing:
			raise ReferenceError("You may not have a question after forfeiting")
		lm = self.landmarks[s.cur].lmark
		if s.pending is not None:
			return Confirmation.objects.get(lmark=lm).ques
		try:
			c = Confirmation.objects.get(lmark=lm)
			s.pending = dt.now(tz('US/Central'))
			s.save()
			return c.ques
		except Clue.DoesNotExist:
			raise EnvironmentError("There is no confirmation associated with this landmark")

	# ReferenceError if team is not playing
	# IndexError if game is not on
	# EnvironmentError if confirmation doesn't exist
	# KeyError if team has no quesitoni pending
	def submit_ans(self, team: User, ans: str) -> bool:
		if not self.is_on():
			raise IndexError("Game is not on")
		s = Status.objects.filter(team=team, game=self.dtls)
		if s.count() == 0:
			raise ReferenceError("You are not in this game")
		s = s.first()
		if not s.playing:
			raise ReferenceError("You may not submit an answer after forfeiting")
		if s.pending is None:
			raise KeyError("You may not submit an answer without a question pending")
		lm = self.landmarks[s.cur].lmark
		try:
			c = Confirmation.objects.get(lmark=lm)
			deltat = (dt.now(tz('US/Central')) - s.pending).total_seconds()
			sc = LmScore(team=team, game=self.dtls, which=s.cur, time=deltat, correct=(ans == c.ans))
			sc.save()
			s.pending = None
			s.score = s.score + self.calc_score_entry(sc)
			if ans == c.ans:
				if s.cur < len(self.landmarks):
					s.cur = s.cur + 1
				if s.cur >= len(self.landmarks):
					s.playing = False
				s.save()
				return True
			else:
				s.save()
				return False
		except Confirmation.DoesNotExist:
			raise EnvironmentError("There is no confirmation associated with this landmark")

	# KeyError on nonexistent team
	# ValueError on illegal values
	def edit_creds(self, team: User, name: str, pwd: str) -> bool:
		return self.edit_team_creds(team, name, pwd)

	# ReferenceError if team is not playing
	# IndexError if game is not on
	def forfeit(self, team: User) -> bool:
		try:
			t = User.objects.get(pk=team.pk)
		except User.DoesNotExist:
			raise KeyError("Nonexistent team may not forfeit")
		if not self.is_on():
			raise IndexError("Cannot forfeit a game that is not in progress")
		s = Status.objects.get(team=t)
		if not s.playing:
			raise ReferenceError("You have already forfeited")
		s.playing = False
		s.save()
		return True

	def calc_scores(self):
		for p in self.players:
			p.score = 0
			sc = LmScore.objects.filter(team=p.team, game=self.dtls)
			for x in sc:
				p.score = p.score + self.calc_score_entry(x)
			p.save()
