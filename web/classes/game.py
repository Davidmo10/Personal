import web.itfs.gameToMakerSession as GTMS
import web.itfs.gameToTeamSession as GTTS
from django.db import models
from web.models import *

class Game(GTMS.ITF, GTTS.ITF):

    def __init__(self, dtls: GameDetails):
        self.maker : User = dtls.maker
        self.name : str = dtls.name
        self.desc : str= dtls.desc
        self.on : bool = dtls.on
        self.players : [Status] = []
        self.scheme : dtls.scheme
        self.hunt : [Landmark] = []

        sel : models.QuerySet = Status.objects.filter(game = dtls)
        for s in sel:
            self.players.append(s)
        sel : models.QuerySet = Hunt.objects.filter(game = dtls)
        for s in sel:
            self.hunt.append(s)