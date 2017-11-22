from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    pwd = models.CharField(max_length=100)
    is_mkr = models.BooleanField(default=False)
    def __str__(self):
        if self.is_mkr:
            return str('< User ModInst (Maker) :: name = '+ self.name + ' >')
        else:
            return str('< User ModInst (Team) :: name = '+ self.name + ' >')


class ScoreScheme(models.Model):
    name = models.CharField(default = "default", max_length = 100)
    wrong = models.FloatField(default = -10)
    right = models.FloatField(default = 50)
    place_numerator = models.FloatField(default = 100) # i.e. first place gets 100/1 (100), second gets 100/2 (50), third gets 100/3 (33.3), etc
    ans_per_sec = models.FloatField(default = -0.1)
    game_per_sec = models.FloatField(default = -.00001)
    def __str__(self):
        return str('< ScoreSchem ModInst :: name = ' + self.name + ' >')

class Game(models.Model):
    name = models.CharField(max_length = 100)
    desc = models.CharField(max_length = 500, null = True, blank = True)
    on = models.BooleanField(default = False)
    winner = models.IntegerField(default = -1)
    maker = models.ForeignKey(User, on_delete = models.CASCADE)
    scheme = models.ForeignKey(ScoreScheme)
    def __str__(self):
        return str('< Game ModInst :: name = ' + self.name + ', maker = '+ str(self.maker) + ' >')


class Status(models.Model):
    game = models.ForeignKey(Game, on_delete = models.CASCADE)
    team = models.ForeignKey(User, on_delete = models.CASCADE)
    cur = models.IntegerField(default = 0)
    pending = models.DateTimeField(default = None, null = True)
    playing = models.BooleanField(default = False)
    score = models.FloatField(default = 0)
    def __str__(self):
        return str('< Status ModInst ::  team = '+ str(self.team) + ', game = '+ str(self.game) + ' >')



class Landmark(models.Model):
    name = models.CharField(max_length = 100)
    desc = models.CharField(max_length = 500, blank=True, default="")
    def __str__(self):
        return str('<Landmark ModInst :: name = ' + self.name+ ', game = ' + str(self.game) + ' >')


class Clue(models.Model):
    lmark = models.ForeignKey(Landmark, on_delete = models.CASCADE)
    value = models.CharField(max_length=500)
    def __str__(self):
        return str('< Clue ModInst :: value = '+ self.value+ ', lmark = '+ str(self.lmark) + ' >')


class Confirmation(models.Model):
    lmark = models.ForeignKey(Landmark, on_delete = models.CASCADE)
    ques = models.CharField(max_length=500)
    ans = models.CharField(max_length=500)
    def __str__(self):
        return str('< Clue ModInst :: ques = '+ self.ques+ ', ans = '+ self.ans+ ', lmark = '+ str(self.lmark) + ' >')

class Hunt(models.Model):
    lmark = models.ForeignKey(Landmark, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    h_order = models.IntegerField(default = -1 )
    def __str__(self):
        return str('< Hunt ModInst :: h_order = ' + str(self.h_order) + 'game = ' + str(self.game) + 'lmark = ' + str(self.lmark) + ' >')
    def save(self, *args, **kwargs):
        if(self.h_order == -1):
            self.h_order = Hunt.objects.filter(game = self.game).count()
        super().save(*args, **kwargs)