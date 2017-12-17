from django.contrib import admin
from .models import *

@admin.register(Landmark, User, Status, GameDetails, Confirmation,
                Clue, Hunt, ScoreScheme, LmScore)
class PersonAdmin(admin.ModelAdmin):
    pass


