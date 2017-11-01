from User import User


class UserFactory:
	def make_user(self, user: str, password: str) -> User:
		"""
		Generates a user object based on whether the username specified is a GameMaker or a team
		:raises: LoginError if username does not exist or password does not match username
		:param user: Username of the user being logged into
		:param password: Password of the user being logged into
		:return: User object corresponding to login details
		"""
		pass