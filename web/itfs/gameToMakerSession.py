from abc import ABC

from web.models import *


class ITF(ABC):
    
    # UserWarning on similar landmark to existing in models somewhere
    # ValueError for illegal value
    # Warning for nonexistent Landmark (self, meaning one will be created)
    def edit_lmark(self, lm: Landmark, name: str, desc: str) -> bool:
        pass
    
    # ValueError if invalid order
    # IndexError if submitted order is longer than hunt or less than zero
    def reorder_hunt(self, order: [int]) -> bool:
        pass
    
    # ValueError for illegal value
    # IndexError for illegal landmark
    def edit_clue(self, clue: Clue, value: str) -> bool:
        pass
    
    # ValueError for illegal value
    # IndexError for illegal landmark
    def edit_conf(self, conf: Confirmation, ques: str, ans: str) -> bool:
        pass
    
    # NameError on same name
    def mk_team(self, name: str, pwd: str) -> bool: 
        pass
    
    # KeyError for nonexistent team
    # KeyError for team not in game
    def rm_team(self, team: User) -> bool: 
        pass
    
    # KeyError on nonexistent team
    # KeyError if team not in game
    # ValueError on illegal values
    def edit_team_creds(self, team: User, name: str, pwd: str) -> bool: 
        pass
    
    # NameError on same name
    def mk_score_sch(self, name: str) -> bool:
        pass
    
    # KeyError on nonexistent scheme
    # EnvironmentError if another game is using the same scheme
    # ValueError on non-float values
    def edit_score_sch(self, scheme: ScoreScheme) -> bool:
        pass
    
    def req_mkr_status(self) -> [Status]:
        pass

    def req_hunt(self, ) -> [Hunt]:
        pass
    
    # ValueError on illegal values
    def edit(self, name: str, desc: str) -> bool: 
        pass
    
    # UserWarning if Game in progress
    def start(self, ) -> bool:
        pass
    
    # UserWarning if Game not in progress
    def stop(self, ) -> bool:
        pass

    def is_on(self, ) -> bool: 
        pass
    
    # UserWarning if team not done with game
    # KeyError if nonexistent team
    # KeyError if team not in game
    def set_winner(self, team: User) -> bool:
        pass