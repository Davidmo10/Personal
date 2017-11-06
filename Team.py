from User import User
from Game import Game


class Team(User):

	def __init__(self, user_id):
		self.team_id = user_id
		self.db = Team_DBMock()
		try:
			info = self.db.fetch_info(user_id)
		except InvalidUserException:
			pass
		self.name = info.name
		self.game_id = info.game_id
		self.events = self.db.fetch_status(self.game_id, self.team_id)
		self.game = Game(self.game_id)

	def request_clue(self):
		self.game.get_clue(self.get_last_event())

	def request_question(self):
		self.game.get_question()

	def submit_answer(self, string):
		if not self.has_requested:
			raise Exception

		correct = self.game.check_answer(self.landmark, string)

		if correct:
			self.has_requested = False
			self.landmark += 1

		return correct

	def forfeit(self):
		pass

	def get_events(self, events):
		pass

	def is_playing(self):
		pass

	def get_last_event(self):
		pass


