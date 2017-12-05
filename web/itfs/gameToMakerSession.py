from abc import ABC
from web.models import *


class ITF(ABC):
    
    # UserWarning on similar landmark to existing in models somewhere
    # ValueError for illegal value
    # Warning for nonexistent Landmark (meaning one will be created)
    def edit_lmark(lm: Landmark, name: str, desc: str) -> bool:
        pass
    
    # IndexError if submitted order is longer than hunt or less than zero
    def reorder_hunt(order : [int] ) -> bool:
        pass
    
    # ValueError for illegal value
    # Warning for nonexistent Clue (meaning one will be created)
    def edit_clue(clue: Clue, value: str) -> bool:
        pass
    
    # ValueError for illegal value
    # Warning for nonexistent Confirmation (meaning one will be created)
    def edit_conf(conf: Confirmation, ques: str, ans: str) -> bool:
        pass
    
    # NameError on same name
    def mk_team(name: str, pwd: str) -> bool: 
        pass
    
    # KeyError for nonexistent team
    # KeyError for team not in game
    def rm_team(self, team: User) -> bool:
        pass
    
    # KeyError on nonexistent team
    # KeyError if team not in game
    # ValueError on illegal values
    def edit_team_creds(team: User, name: str, pwd: str) -> bool: 
        pass
    
    # NameError on same name
    def mk_score_sch(name: str) -> bool: 
        pass
    
    # KeyError on nonexistent scheme
    # EnvironmentError if another game is using the same scheme
    # ValueError on non-float values
    def edit_score_sch(scheme: ScoreScheme, wrong: float, right: float, plc_num: float, ans_time: float, gm_time: float) -> bool: 
        pass
    
    def req_status() -> [Status]:
        pass

    def req_hunt() -> [Hunt]:
        pass
    
    # ValueError on illegal values
    def edit(name: str, desc: str) -> bool: 
        pass
    
    # UserWarning if Game in progress
    def start () -> bool: 
        pass
    
    # UserWarning if Game not in progress
    def stop () -> bool: 
        pass

    def is_on() -> bool: 
        pass
    
    # UserWarning if team not done with game
    # KeyError if nonexistent team
    # KeyError if team not in game
    def set_winner(team: User) -> bool:
        pass