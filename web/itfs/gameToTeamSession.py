from abc import ABC
from web.models import *

class ITF(ABC):

    # ReferenceError if team is not playing
    # IndexError if game is not on
    def req_clue(self, team: User) -> Clue:
        pass

    # ReferenceError if team is not playing
    # IndexError if game is not on
    # EnvironmentError if team has a question pending
    def req_ques(self, team: User) -> str:
        pass

    # ReferenceError if team is not playing
    # IndexError if game is not on
    # KeyError if team does not have a question pending
    def submit_ans(self, team: User, str) -> bool:
        pass

    def req_status(self, team: User) -> Status:
        pass

    # KeyError on nonexistent team
    # ValueError on illegal values
    def edit_creds(self, team: User, name: str, pwd: str)-> bool :
        pass

    # ReferenceError if team is not playing
    # IndexError if game is not on
    def forfeit(self, team: User) -> bool:
        pass

    def is_on(self, ) -> bool:
        pass