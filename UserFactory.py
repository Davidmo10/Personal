from Game import Game
from User import User
from errors import LoginError


class UserFactory:
	@staticmethod
	def make_user(user: str, password: str, game: Game) -> User:
		"""
		Generates a user object based on whether the username specified is a GameMaker or a team
		:raises: LoginError if username does not exist or password does not match username
		:param user: Username of the user being logged into
		:param password: Password of the user being logged into
		:param game: game object
		:return: User object corresponding to login details
		"""
		user_index = game.get_user_index_by_name(user)

		if user_index == -1:
			raise LoginError("Invalid username " + user)
		if game.myUserDict[user_index].password != password:
			raise LoginError("Invalid User/Password " + user + " / " + password )
		return game.myUserDict[user_index]