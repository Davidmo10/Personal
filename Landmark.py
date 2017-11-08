from Clue import Clue
from Confirmation import Confirmation


class Landmark():
    def __init__(self, name):
        self.clue = None
        self.confirmation = None
        self.name = name

    def add_confirmation(self, confirmation: Confirmation):
        self.confirmation = confirmation

    def add_clue(self, clue: Clue):
        self.clue = clue

    def get_confirmation(self):
        return self.confirmation

    def get_clue(self):
        return self.clue

    def check_answer(self, string: str) -> bool:
        return self.confirmation.get("Confirmation").validate(str)
