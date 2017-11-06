class User():

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

	def