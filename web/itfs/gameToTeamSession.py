from abc import ABC
from web.models import *

class ITF(ABC):

    # ReferenceError if team is not playing
    # IndexError if game is not on
    def req_clue(team: User) -> Clue:
        pass

    # ReferenceError if team is not playing
    # IndexError if game is not on
    # EnvironmentError if team has a question pending
    def req_ques(team: User) -> str:
        pass

    # ReferenceError if team is not playing
    # IndexError if game is not on
    # EnvironmentError if team does not have a question pending
    def submit_ans(team: User, str) -> bool:
        pass

    def req_status(team: User) -> Status:
        pass

    # KeyError on nonexistent team
    # ValueError on illegal values
    def edit_creds(team: User, name: str, pwd: str)-> bool :
        pass

    # ReferenceError if team is not playing
    # IndexError if game is not on
    def forfeit(team: User) -> bool:
        pass

    def is_on() -> bool:
        pass