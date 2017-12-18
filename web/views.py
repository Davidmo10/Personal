import logging

from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render

from web.classes.game import Game
from web.models import *

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
logging.debug('This message should appear on the console')
logging.info('So should this')
logging.warning('And this, too')


class LoginForm(forms.Form):
	uname = forms.CharField(label='Username ', max_length=100)
	upwd = forms.CharField(label='    Password ', max_length=100, widget=forms.PasswordInput())


class AnswerForm(forms.Form):
	ans = forms.CharField(label='Answer ', max_length=200)


class CredsForm(forms.Form):
	name = forms.CharField(label='Team Name ', max_length=100)
	oldpwd = forms.CharField(label='Old Password ', max_length=100, widget=forms.PasswordInput())
	newpwd = forms.CharField(label='New Password ', max_length=100, widget=forms.PasswordInput())
	user_id = forms.IntegerField(widget=forms.HiddenInput())


class EditLmForm(forms.Form):
	name = forms.CharField(label='Landmark Name ', max_length=100)
	desc = forms.CharField(label='Landmark Description ', max_length=500)
	clue = forms.CharField(label='Landmark Clue ', max_length=500)
	ques = forms.CharField(label='Landmark Question ', max_length=500)
	ans = forms.CharField(label='Landmark Answer ', max_length=500)
	lm_id = forms.IntegerField(widget=forms.HiddenInput())


class ReorderForm(forms.Form):
	pass


class BaseReorderForm(forms.BaseFormSet):
	def add_fields(self, form, index):
		super().add_fields(form, index)
		form.fields["h_" + str(index)] = forms.IntegerField(initial=index + 1, label="",
		                                                    widget=forms.TextInput(attrs={'class': 'reorder_box'}))


class SchemeForm(forms.ModelForm):
	create_new_scheme = forms.BooleanField(initial=False, required=False)

	class Meta:
		model = ScoreScheme
		fields = ['name', 'wrong', 'right', 'place_numerator', 'ans_per_sec', 'game_per_sec']


class EditGameForm(forms.ModelForm):
	class Meta:
		model = GameDetails
		fields = ['name', 'desc']


def login(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			try:
				u = User.objects.get(name=form.cleaned_data["uname"])
				if u.pwd != form.cleaned_data["upwd"]:
					raise ValueError
				else:
					request.session['loggedin'] = True
					request.session['name'] = u.name
					request.session['mkr'] = u.is_mkr
					return HttpResponseRedirect('/')
			except (User.DoesNotExist, ValueError):
				form = LoginForm()
				return render(request, 'login.html', {'form': form, 'attempted': True})
	else:
		form = LoginForm()
	return render(request, 'login.html', {'form': form, 'attempted': False})


def dash(request):
	if request.session.get('loggedin', False):
		try:
			u = User.objects.get(name=request.session['name'])
		except (User.DoesNotExist, KeyError):
			return HttpResponseRedirect('/login')
		if request.session['mkr']:
			try:
				gd = GameDetails.objects.get(maker=u)
			except GameDetails.DoesNotExist:
				return HttpResponseRedirect('/do/create')
			g = Game(gd)
			h = g.req_hunt()
			h_forms: [{EditLmForm, int}] = []
			for i in range(len(h)):
				x = h[i]
				lm = Landmark.objects.get(name=x["name"])
				try:
					cl = Clue.objects.get(lmark__name=x["name"]).value
				except (Clue.DoesNotExist, KeyError):
					cl = ""
				try:
					co = Confirmation.objects.get(lmark__name=x["name"])
					ques = co.ques
					ans = co.ans
				except (Confirmation.DoesNotExist, KeyError):
					ques = ""
					ans = ""
				h_forms.append({"form": EditLmForm(
					initial={"name": x["name"], "desc": lm.desc, "clue": cl, "ques": ques, "ans": ans}), "index": i,
				               "lm_id": lm.pk})
			tms = g.req_team_statuses()
			t_forms: [{CredsForm, int, int}] = []
			for x in tms:
				t = x["tm"]
				cf = CredsForm(initial={"name": t.name})
				cf.fields["oldpwd"].label = "Your Password: "
				t_forms.append({"form": cf, "index": x["index"], "pk": t.pk})
			rformset = forms.formset_factory(ReorderForm, formset=BaseReorderForm, extra=len(h))
			reorder_form = rformset()
			scheme_form = SchemeForm(instance=gd.scheme)
			team_cred_form = CredsForm()
			team_cred_form.fields["oldpwd"].label = "Password"
			team_cred_form.fields["newpwd"].label = "Repeat Password"
			maker_cred_form = CredsForm(initial={"name": u.name})
			edit_game_form = EditGameForm(instance=g.dtls)
			landmark_form = EditLmForm()
			return render(request, 'makerdash.html', {'name': u.name, 'gmdet': gd, 'teams': tms, 'hunt': zip(reorder_form, h),
			                                          'hunt_mng_form': reorder_form.management_form, 'sch': gd.scheme,
			                                          "cForms": t_forms,
			                                          "hForms": h_forms, "schemeForm": scheme_form, 'ntForm': team_cred_form,
			                                          'credsForm': [maker_cred_form, u.pk],
			                                          "gameForm": edit_game_form, "newlmForm": landmark_form,
			                                          })
		else:
			try:
				s = Status.objects.get(team=u)
				g = Game(s.game)
				status = g.req_status(u)
				progress = g.req_team_progress(u)
				if status["curtype"] == 'gameoff':
					title = 'Game Off'
					feedback = 'This game is not currently playable'
				elif status["curtype"] == 'forfeited':
					title = 'Your team has forfeited'
					feedback = 'Quitters never win'
				elif status["curtype"] == 'done':
					title = "You're done"
					feedback = 'Good job!'
				elif status["curtype"] == 'pending':
					title = "Current Question"
					q = g.req_ques(u)
					feedback = q
				else:
					title = "Current Clue"
					feedback = g.req_clue(u)
				answer_form = AnswerForm()
				credential_form = CredsForm(initial={"name": u.name})
				return render(request, 'teamdash.html',
				              {'name': u.name, 'type': status["curtype"], 'gmdet': status["game"], 'title': title,
				               'feedback': feedback,
				               'progress': progress, 'total': status["total"], 'ansForm': answer_form,
				               'credsForm': [credential_form, u.pk], 'pending': s.pending,

				               })
			except Exception as e:
				feedback = str(e)
				return render(request, 'error.html', {'feedback': feedback})

	else:
		return HttpResponseRedirect('/login')


def req(request, kind):
	if request.session.get('loggedin', False):
		try:
			u = User.objects.get(name=request.session['name'])
			s = Status.objects.get(team=u)
		except (User.DoesNotExist, Status.DoesNotExist, KeyError):
			return HttpResponseRedirect('/login')
		g = Game(s.game)
		if kind == "ques":
			g.req_ques(u)
		elif kind == "ans":
			if request.method == "POST":
				form = AnswerForm(request.POST)
				if form.is_valid():
					g.submit_ans(u, form.cleaned_data["ans"])
		return HttpResponseRedirect("/")
	return HttpResponseRedirect("/login")


def do(request, action):
	if request.session.get('loggedin', False):
		try:
			u = User.objects.get(name=request.session['name'])
		except (User.DoesNotExist, KeyError):
			return HttpResponseRedirect('/login')
		if action == 'logout':
			request.session.flush()
		if not u.is_mkr:
			s = Status.objects.get(team=u)
			if action == 'forfeit':
				s.playing = False
				s.save()
		else:
			try:
				gd = GameDetails.objects.get(maker=u)
			except GameDetails.DoesNotExist:
				if request.method == 'POST':
					cf = EditGameForm(request.POST)
					if cf.is_valid():
						cd = cf.cleaned_data
						GameDetails(name=cd["name"], desc=cd["desc"], maker=u,
						            scheme=ScoreScheme.objects.get(name='default')).save()
					return HttpResponseRedirect('/')
				else:
					cf = EditGameForm()
					return render(request, "create.html", {"maker": u.pk, "createForm": cf})
			g = Game(gd)
			if action == 'stop':
				g.stop()
			if action == 'start':
				g.start()
		return HttpResponseRedirect("/")
	return HttpResponseRedirect("/login")


def edit(request, to_edit):
	if request.session.get('loggedin', False):
		try:
			u = User.objects.get(name=request.session['name'])
		except (User.DoesNotExist, KeyError):
			return HttpResponseRedirect('/login')
		try:
			if to_edit == 'creds':
				if request.method == "POST":
					form = CredsForm(request.POST)
					if form.is_valid():
						cd = form.cleaned_data
						t_pk = cd['user_id']
						if t_pk == -1 and u.is_mkr:
							if cd['newpwd'] != cd['oldpwd']:
								return render(request, 'error.html', {'feedback': "Passwords did not match"})
							gd = GameDetails.objects.get(maker=u)
							g = Game(gd)
							g.mk_team(cd["name"], cd["newpwd"])
							return HttpResponseRedirect('/')
						t = User.objects.get(pk=t_pk)
						if t.pwd == cd['oldpwd'] or (u.is_mkr and cd['oldpwd'] == u.pwd):
							t.pwd = cd['newpwd']
							t.name = cd['name']
							t.save()
						else:
							return render(request, 'error.html', {'feedback': 'Invalid login information'})
					else:
						return form.errors.as_json()
			if u.is_mkr and request.method == 'POST':
				gd = GameDetails.objects.get(maker=u)
				g = Game(gd)
				if to_edit == 'reorder':
					neworder: [int] = []
					for i in range(len(g.landmarks)):
						order = request.POST.get("form-{0!s}-h_{0!s}".format(i), default=False)
						logging.debug(order)
						if not order:
							raise Exception("Invalid reordering")
						neworder.append(int(order) - 1)
					logging.debug(neworder)
					g.reorder_hunt(neworder)
				elif to_edit == 'scheme':
					form = SchemeForm(request.POST)
					if form.is_valid():
						if not form.cleaned_data["create_new_scheme"]:
							form = SchemeForm(request.POST, instance=gd.scheme)
						sch = form.save(commit=False)
						g.edit_score_sch(sch)
				elif to_edit == 'lmark':
					form = EditLmForm(request.POST)
					if form.is_valid():
						cd = form.cleaned_data
						lm_pk = int(cd['lm_id'])
						if lm_pk != -1:
							lm = Landmark.objects.get(pk=lm_pk)
						else:
							lm = Landmark(name=cd['name'], desc=cd['desc'])
						g.edit_lmark(lm=lm, name=cd['name'], desc=cd['desc'])
						lm = Landmark.objects.get(name=cd['name'])
						g.edit_clue(lm=lm, value=cd['clue'])
						g.edit_conf(lm=lm, ques=cd['ques'], ans=cd['ans'])
					else:
						return form.errors.as_json()
				elif to_edit == 'game':
					form = EditGameForm(request.POST)
					if form.is_valid():
						cd = form.cleaned_data
						g.edit(name=cd["name"], desc=cd["desc"])
			elif u.is_mkr and request.method == "GET":
				gd = GameDetails.objects.get(maker=u)
				g = Game(gd)
				if to_edit == "winner":
					w = User.objects.get(pk=request.GET.get('u'))
					g.set_winner(w)
				elif to_edit == "remove":
					tm = request.GET.get('u', default=False)
					if tm is not False:
						t = User.objects.get(pk=tm)
						g.rm_team(t)
					lm = request.GET.get('lm', default=False)
					if lm is not False:
						g.rm_lmark(int(lm))
			return HttpResponseRedirect("/")
		except Exception as e:
			return render(request, "error.html", {"feedback": " {0!s} - {1!s}".format(e, e.args)})
	return HttpResponseRedirect("/login")
