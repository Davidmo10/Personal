from Clue import Clue
from Game import Game
from User import User


class Team(User):
    def __init__(self, game: Game):
        super().__init__()
        self.commands = {"getclue": lambda: self.request_clue(),
                         "getquestion": lambda: self.request_question(),
                         "answer": lambda ans: self.answer(ans),
                         "forfeit": lambda: self.forfeit()}  # dict
        self.landmark_index = 0  # index
        # self.this_team_index = team_index  # This index has to come from outside team to logout
        # 								   # Each team will need an index in username list so when they
        # 								   # login they are linked to the right team
        self.myGame = game
        self.has_requested = False
        self.logged_in = False  # Until we can pass user indexes between game and user to flag login

    # This is a temporary solution

    # def login(self):
    # 	pass
    #
    # def logout(self):
    # 	pass

    def list_commands(self) -> dict:
        return self.commands

    def request_clue(self) -> Clue:
        if self.logged_in:
            return self.myGame.get_clue(self.landmark_index)

    def request_question(self):
        if self.logged_in:
            self.has_requested = True
            return self.myGame.get_question(self.landmark_index)

    def answer(self, string):
        if self.logged_in:
            if self.has_requested:
                raise Exception

        correct = self.myGame.check_answer(self.landmark_index, string)

        if correct:
            self.has_requested = False
            self.landmark_index += 1

        return correct

    def forfeit(self) -> bool:
        if self.logged_in:
            self.logged_in = False
            return self.logged_in
