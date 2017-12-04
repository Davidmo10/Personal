from django.shortcuts import render
from web.models import *
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django import forms
from web.classes.game import Game

class LoginForm(forms.Form):
    uname = forms.CharField(label='Username ', max_length=100)
    upwd = forms.CharField(label='    Password ', max_length=100)

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
            s = Status.objects.get(team = u)
            gd = s.game
            g = Game(gd)
            lm = g.hunt[s.cur].lmark
            clu = Clue.objects.get(lmark = lm)
            progress = g.process_team_progress(team = u)
            return render(request, 'teamdash.html', {'name' : u.name, 'gmdet' : gd, 'clue' : clu.value, 'progress' : progress})
        except:
            return HttpResponseRedirect('/login')
    else:
        return HttpResponseRedirect('/login')