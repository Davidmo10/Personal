from abc import ABC, abstractmethod

class TeamDBInterface(ABC):
	
	def __init__(self):
		super().__init__()

	# Raises InvalidUserException
	@abstractmethod
	def login(self, name, pwd):
		pass
		
	# Raises InvalidUserException, InvalidGameStateException, InvalidTeamStateException
	@abstractmethod
	def forfeit(self, game_id, team_id):
		pass


class MasterDBInterface(ABC):
	
	def __init__(self):
		super().__init__()
	
	# Raises InvalidUserException
	@abstractmethod
	def login(self, name, pwd):
		pass
	
	# Raises InvalidUserException
	@abstractmethod
	def create_game(self, master_id, title, desc):
		pass
	
	# Raises InvalidUserException, InvalidGameStateException
	@abstractmethod
	def end_game(self, game_id):
		pass


class GameDBInterface(ABC):
	
	def __init__(self):
		super().__init__()

	# Throws InvalidGameException
	@abstractmethod
	def is_on(self, game_id):
		pass

	# Throws InvalidGameException, InvalidGameStateException
	@abstractmethod
	def start(self, game_id):
		pass
	
	# Throws InvalidGameException, InvalidGameStateException
	@abstractmethod
	def stop(self, game_id):
		pass
	
	# Throws InvalidGameException, EmptyGameSetException
	@abstractmethod
	def fetch_landmarks(self, game_id):
		pass

	# Throws InvalidGameException
	@abstractmethod
	def fetch_team_list(self, game_id):
		pass
	
	# Throws InvalidGameException, InvalidTeamException
	@abstractmethod
	def fetch_team_status(self, game_id, team):
		pass
	
	# Throws InvalidGameException, InvalidLandmarkException, InvalidTeamException
	@abstractmethod
	def submit_answer(self, game_id, team_id, lm_id, answer):
		pass
	
	
	
class LandmarkDBInterface(ABC):
	
	def __init__(self):
		super().__init__()

	# Throws InvalidGameException, LandmarkAlreadyInGameException
	@abstractmethod
	def create_landmark(self, game_id, title, desc):
		pass
	
	# Throws InvalidLandmarkException, InvalidGameException
	@abstractmethod
	def edit_landmark(self, landmark_id, game_id, title, desc):
		pass

	# Throws InvalidLandmarkException
	# Returns > 0 if changes made, 0 if not (setting to null)
	@abstractmethod
	def set_clue(self, landmark_id, game_id, clue):
		pass
	
	# Throws InvalidLandmarkException, SettingAnswerWithNoQuestionException
	# Returns > 0 if changes made, 0 if not (setting to null)
	@abstractmethod
	def set_question(self, landmark_id, game_id, prompt, answer):
		pass

