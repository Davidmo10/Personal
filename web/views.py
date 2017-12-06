from django.shortcuts import render
from web.models import *
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django import forms
from web.classes.game import Game
from datetime import datetime as dt
from pytz import timezone as tz

class LoginForm(forms.Form):
    uname = forms.CharField(label='Username ', max_length=100)
    upwd = forms.CharField(label='    Password ', max_length=100, widget = forms.PasswordInput())

class AnswerForm(forms.Form):
    ans = forms.CharField(label='Answer ', max_length=200)

class CredsForm(forms.Form):
    name = forms.CharField(label='Team Name ', max_length=100)
    oldpwd = forms.CharField(label='Old Password ', max_length=100, widget = forms.PasswordInput())
    newpwd = forms.CharField(label='New Password ', max_length=100, widget = forms.PasswordInput())
    user = forms.IntegerField(widget = forms.HiddenInput())

class EditLmForm(forms.Form):
    name = forms.CharField(label='Landmark Name ', max_length=100)
    desc = forms.CharField(label='Landmark Description ', max_length=500)
    clue = forms.CharField(label='Landmark Clue ', max_length=500)
    ques = forms.CharField(label='Landmark Question ', max_length=500)
    ans = forms.CharField(label='Landmark Answer ', max_length=500)
    lm_id = forms.IntegerField(widget = forms.HiddenInput())

class ReorderForm(forms.Form):
    id = forms.IntegerField(widget=forms.HiddenInput())

class BaseReorderForm(forms.BaseFormSet):
    def add_fields(self, form, index):
        super().add_fields(form, index)
        form.fields["h_" + str(index)] = forms.IntegerField(initial=index+1, label="", widget=forms.TextInput(attrs={'class':'reorder_box'}))

class SchemeForm(forms.ModelForm):
    create_new_scheme = forms.BooleanField(initial=False)
    class Meta:
        model = ScoreScheme
        fields = ['name', 'wrong', 'right', 'place_numerator', 'ans_per_sec', 'game_per_sec']

class EditGameForm(forms.ModelForm):
    class Meta:
        model = GameDetails
        fields = ['name', 'desc']

def login(request):
    if request.method == 'POST':
        form= LoginForm(request.POST)
        if(form.is_valid()):
            try:
                u = User.objects.get(name = form.cleaned_data["uname"])
                if u.pwd != form.cleaned_data["upwd"]:
                    raise ValueError
                else:
                    request.session['loggedin'] = True
                    request.session['name'] = u.name
                    request.session['mkr'] = u.is_mkr
                    return HttpResponseRedirect('/')
            except:
                form = LoginForm()
                return render(request, 'login.html', {'form' : form, 'attempted': True })
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form, 'attempted' : False})

def dash(request):
    if request.session.get('loggedin', False):
        try:
            u = User.objects.get(name = request.session['name'])
        except:
            return HttpResponseRedirect('/login')
        if request.session['mkr'] :
            try:
                gd = GameDetails.objects.get(maker = u)
            except:
                return HttpResponseRedirect('/do/mkgame')
            g = Game(gd)
            h = g.req_hunt()
            hForms : [{EditLmForm, int}] = []
            for i in range(len(h)):
                x = h[i]
                lm = Landmark.objects.get(name = x["name"])
                try:
                    cl = Clue.objects.get(lmark__name = x["name"]).value
                except:
                    cl = ""
                try:
                    co = Confirmation.objects.get(lmark__name = x["name"])
                    ques = co.ques
                    ans = co.ans
                except:
                    ques = ""
                    ans = ""
                hForms.append({"form" : EditLmForm(initial= {"name" : x["name"], "desc" : lm.desc, "clue" : cl, "ques" : ques, "ans" : ans}), "index" : i,  "lm_id" : lm.pk})
            tms = g.req_team_statuses()
            tForms : [{CredsForm, int}] = []
            for x in tms:
                t = x["tm"]
                cf = CredsForm(initial={"name":t.name, "user":t.pk})
                cf.fields["oldpwd"].label = "Your Password: "
                tForms.append({"form" :cf, "index" : x["index"]})
            rformset = forms.formset_factory(ReorderForm, formset=BaseReorderForm, extra=len(h))
            rForm = rformset()
            sForm = SchemeForm(instance=gd.scheme)
            if gd.scheme.name == 'default':
                sForm.fields["create_new_scheme"] = True
                sForm.fields["create_new_scheme"].widget = forms.HiddenInput()
            return render(request, 'makerdash.html', {'name' : u.name, 'gmdet' : gd, 'teams' : tms, 'hunt' : zip(rForm.forms, h), 'sch' : gd.scheme, "cForms" : tForms, "hForms" : hForms, "schemeForm" : sForm })
        else:
            try:
                s = Status.objects.get(team = u)
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
                ansForm = AnswerForm()
                credsForm = CredsForm(initial = {"name" : u.name, "user" : u.pk})
                return render(request, 'teamdash.html',
                              {'name': u.name, 'type': status["curtype"], 'gmdet': status["game"], 'title': title, 'feedback': feedback,
                               'progress': progress, 'total' : status["total"], 'ansForm' :ansForm, 'credsForm' : credsForm, 'pending' : s.pending })
            except Exception as e:
                title = "Error"
                feedback= str(e)
                return render(request, 'teamdash.html', {'name': u.name, 'type': "error", 'feedback' : feedback, 'title': title})

    else:
        return HttpResponseRedirect('/login')

def req(request, type):
    if request.session.get('loggedin', False):
        try:
            u = User.objects.get(name = request.session['name'])
            s = Status.objects.get(team = u)
        except:
            return HttpResponseRedirect('/login')
        # try:
        g = Game(s.game)
        status = g.req_status(u)
        if type == "ques":
            g.req_ques(u)
        elif type == "ans":
            if request.method == "POST":
                form = AnswerForm(request.POST)
                if(form.is_valid()):
                    g.submit_ans(u, form.cleaned_data["ans"])
        return HttpResponseRedirect("/")
    # except Exception as e:
        #     return render(request, "teamdash.html", {"name" : u.name, "feedback" : str(e), "title": "Error", "type" : "error"})
    return HttpResponseRedirect("/login")

def do(request, type):
    if request.session.get('loggedin', False):
        try:
            u = User.objects.get(name = request.session['name'])
            s = Status.objects.get(team = u)
        except:
            return HttpResponseRedirect('/login')
        if type == 'forfeit':
            s.playing = False
            s.save()
        if type == 'logout':
            request.session.flush()
        return HttpResponseRedirect("/")
    # except Exception as e:
        #     return render(request, "teamdash.html", {"name" : u.name, "feedback" : str(e), "title": "Error", "type" : "error"})
    return HttpResponseRedirect("/login")

def edit(request, type):
    if request.session.get('loggedin', False):
        try:
            u = User.objects.get(name = request.session['name'])
        except:
            return HttpResponseRedirect('/login')
        if type == 'creds':
            if request.method == "POST":
                form = CredsForm(request.POST)
                if form.is_valid():
                    t = User.objects.get(pk = form.cleaned_data['user'])
                    if t.pwd == form.cleaned_data['oldpwd'] or u.is_mkr:
                        t.pwd = form.cleaned_data['newpwd']
                        t.save()
                    else:
                        return render(request, 'teamdash.html', {'name' : u.name, 'type': 'error', 'title':'Error', 'feedback':'Invalid old password'})
        if u.is_mkr and request.method == 'POST':
            gd = GameDetails.objects.get(maker=u)
            g = Game(gd)
            if type == 'reorder':
                formset = request.POST
                neworder = []
                #for i in range(len(g.hunt)):
                # fuck this
            elif type == 'scheme':
                form = SchemeForm(request.POST)
                if form.is_valid():
                    if not form.cleaned_data["create_new_scheme"]:
                        form = SchemeForm(request.POST, instance = gd.scheme)
                    form.save()
            elif type == 'lmark':
                form = EditLmForm(request.POST)
                if form.is_valid():
                    cd = form.cleaned_data
                    lm = Landmark.objects.get(pk = int(cd['lm_id']))
                    g.edit_lmark(lm = lm, name = cd['name'], desc = cd['desc'])
                    g.edit_clue(lm = lm, value = cd['clue'])
                    g.edit_conf(lm = lm, ques=cd['ques'], ans=cd['ans'])
                else:
                    return form.errors.as_json()
            elif type == 'game':
                form = EditGameForm(request.POST)
                if form.is_valid():
                    cd = form.cleaned_data
                    g.edit(name = cd["name"], desc = cd["desc"])
        elif u.is_mkr and request.method == "GET":
            gd = GameDetails.objects.get(maker=u)
            g = Game(gd)
            if type == "winner":
                w = User.objects.get(pk= request.GET.get('u'))
                g.set_winner(w)
            elif type == "remove":
                t = User.objects.get(pk= request.GET.get('u'))
                g.rm_team(t)
        return HttpResponseRedirect("/")
    # except Exception as e:
        #     return render(request, "teamdash.html", {"name" : u.name, "feedback" : str(e), "title": "Error", "type" : "error"})
    return HttpResponseRedirect("/login")

