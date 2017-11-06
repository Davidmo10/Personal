# interfaces
from User import User

class GameMaker(User):

	def __init__(self, user_id):
		super().__init__(user_id)


	def create_game(self) -> Game:
		pass

	def create_landmark(self, name, clue, question, answer) -> bool:
		pass

	def edit_landmark_clue(self, name, old_clue, new_clue, index) -> bool:
		pass

	def edit_landmark_question(self, name, old_question, new_question, new_answer) -> bool:
		pass

	def create_team(self, name) -> bool:
		pass

	def create_scavenger_hunt(self):
		pass

	def add_landmark_to_scavenger_hunt(self):
		pass

	def end_game(self):
		pass