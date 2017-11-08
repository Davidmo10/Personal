from Clue import Clue
from Confirmation import Confirmation
from LandmarkGameMaker import LandmarkGameMaker
from LandmarkGame import LandmarkGame


class Landmark(LandmarkGame, LandmarkGameMaker):
    def __init__(self, name):
        self.clue = None
        self.confirmation = None
        self.name = name

    def set_confirmation(self, confirmation: Confirmation):
        self.confirmation = confirmation

    def set_clue(self, clue: Clue):
        self.clue = clue

    def get_confirmation(self) -> Confirmation:
        return self.confirmation

    def get_clue(self) -> Clue:
        return self.clue

    def check_answer(self, string: str) -> bool:
        return self.confirmation.validate(string)
