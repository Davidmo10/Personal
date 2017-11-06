import copy

from db_interfaces import TeamDBInterface, MasterDBInterface, GameDBInterface, LandmarkDBInterface
from escavenger_db_exceptions import InvalidGameException, InvalidTeamException, InvalidUserException, \
	InvalidLandmarkException, InvalidGameStateException, InvalidTeamStateException, EmptyGameSetException, \
	EmptyTeamListException, LandmarkAlreadyInGameException, SettingAnswerWithNoQuestionException


class DBMock:
	teams = [{"user_id": 0, "name": "team1", "pwd": "team1pwd", "game_id": 0}, {"userid": 1, "name": "team2", "pwd": "team2pwd"}, {"userid": 2, "name": "team3", "pwd": "team3pwd"}, {"userid": 3, "name": "team4", "pwd": "team4pwd"}]
	masters = [{"user_id": 2, "name": "master", "pwd": "masterpass", "game_id": 0}]
	games = [{"game_id": 0,
	          "master_id": 2,
	          "title": "Pokemon",
	          "desc": "Catch those fuckers",
	          "on": True,
	          "landmarks": [
		          {"landmark_id": 0,
		           "title": "uwm",
		           "desc": "blah uwm blah",
		           "clue": "it's uwm",
		           "question": "am i uwm?",
		           "answer": "yes"
		           },
		          {"landmark_id": 1,
		           "title": "ems",
		           "desc": "blah ems blah",
		           "clue": "it's ems",
		           "question": "am i ems?",
		           "answer": "yes"
		           },
		          {"landmark_id": 2,
		           "title": "jimmy johns",
		           "desc": "blah jimmy johns blah",
		           "clue": "it's jimmy johns",
		           "question": "am i jimmy johns?",
		           "answer": "yes"
		           }
	          ],
	          "teams": [
		          {"team_id": 0,
		           "events": [
			           {"landmark_id": 0,
			            "correct": True
			            },
			           {"landmark_id": 1,
			            "correct": False
			            },
			           {"landmark_id": 1,
			            "correct": False
			            }
		           ],
		           "playing": True
		           },
		          {"team_id": 1,
		           "events": [
			           {"landmark_id": 0,
			            "correct": True
			            },
			           {"landmark_id": 1,
			            "correct": False
			            },
		           ],
		           "playing": True
		           },
		          {"team_id": 2,
		           "events": [],
		           "playing": True
		           },
		          {"team_id": 3,
		           "events": [
			           {"landmark_id": 0,
			            "correct": True
			            },
			           {"landmark_id": 1,
			            "correct": True
			            },
			           {"landmark_id": 2,
			            "correct": True
			            }
		           ],
		           "playing": True
		           }
	          ]}]

	def __init__(self):
		pass

	@staticmethod
	def fetch_game(game_id) -> dict:
		if len(DBMock.games) <= game_id:
			raise InvalidGameException
		output = DBMock.games[game_id]
		if output is None:
			raise InvalidGameException
		return output

	@staticmethod
	def fetch_team(game_id, team_id)->dict:
		g = DBMock.fetch_game(game_id)
		if len(g["teams"]) <= team_id:
			raise InvalidTeamException
		output = g["teams"][team_id]
		if not output:
			raise InvalidTeamException
		return output

	@staticmethod
	def fetch_lm(lm_id, game_id):
		g = DBMock.fetch_game(game_id)
		if len(g["landmarks"]) <= lm_id:
			raise InvalidLandmarkException
		output = g["landmarks"][lm_id]
		if not output:
			raise InvalidLandmarkException
		return output


class TeamDBMock(TeamDBInterface, DBMock):
	def __init__(self):
		super().__init__()

	def login(self, name, pwd):
		for user in self.teams:
			if user["name"] == name:
				if user["pwd"] == pwd:
					return copy.deepcopy(user)
				else:
					raise InvalidUserException
		raise InvalidUserException

	def forfeit(self, game_id, team_id):
		g = DBMock.fetch_game(game_id)
		t = DBMock.fetch_team(game_id, team_id)
		if not g["on"]:
			raise InvalidGameStateException
		if not t['playing']:
			raise InvalidTeamStateException
		t["playing"] = False


class MasterDBMock(MasterDBInterface, DBMock):
	def __init__(self):
		super().__init__()

	def login(self, name, pwd):
		for user in self.masters:
			if user['name'] == name:
				if user['pwd'] == pwd:
					return copy.deepcopy(user)
				else:
					raise InvalidUserException
		raise InvalidUserException

	def create_game(self, master_id, title="Default Title", desc="Default Description"):
		new_id = len(self.games)
		self.games.append(
			{"game_id": new_id, "title": title, "desc": desc, "master_id": master_id, "on": 0, "landmarks": (), "teams": ()})
		return new_id

	def end_game(self, game_id):
		g = DBMock.fetch_game(game_id)
		if not g["on"]:
			raise InvalidGameStateException
		g["on"] = False


class GameDBMock(GameDBInterface, DBMock):
	def __init__(self):
		super().__init__()

	def is_on(self, game_id):
		g = DBMock.fetch_game(game_id)
		return g["on"]

	def start(self, game_id) -> bool:
		g = DBMock.fetch_game(game_id)
		if g["on"]:
			raise InvalidGameStateException
		g["on"] = True
		return True

	def stop(self, game_id):
		g = DBMock.fetch_game(game_id)
		if not g["on"]:
			raise InvalidGameStateException
		g["on"] = False
		return True

	def fetch_landmarks(self, game_id):
		g = DBMock.fetch_game(game_id)
		if g["landmarks"] is None:
			raise EmptyGameSetException
		return copy.deepcopy(g["landmarks"])

	def fetch_team_list(self, game_id):
		g = DBMock.fetch_game(game_id)
		if g["teams"] is None:
			raise EmptyTeamListException
		return copy.deepcopy(g["teams"])

	def fetch_team_status(self, game_id, team_id):
		return copy.deepcopy(DBMock.fetch_team(game_id, team_id))

	def submit_answer(self, game_id, team_id, lm_id, answer):
		t = DBMock.fetch_team(game_id, team_id)
		lm = DBMock.fetch_lm(lm_id, game_id)
		is_correct = answer.strip().capitalize() == lm["answer"].strip().capitalize()
		answer = {"landmark_id": lm["landmark_id"], "correct": is_correct}
		t["events"].append(answer)
		return is_correct


class LandmarkDBMock(LandmarkDBInterface, DBMock):
	def __init__(self):
		super().__init__()

	def create_landmark(self, game_id, title=None, desc=None):
		lm_list = self.games[game_id]["landmarks"]
		found_it = any((lname["title"] == title and lname["title"] is not None) for lname in lm_list)
		if found_it:
			raise LandmarkAlreadyInGameException(lm_list[3])
		new_lm_id = len(lm_list)
		new_lm_dict = {"landmark_id": new_lm_id, "title": title, "desc": desc, "clue": None, "question": None, "answer": None}
		lm_list.append(new_lm_dict)
		return copy.deepcopy(new_lm_dict)

	def edit_landmark(self, lm_id, game_id, title, desc):
		l = DBMock.fetch_lm(lm_id, game_id)
		flag = 0
		if title is not None:
			l["title"] = title
			flag += 1
		if desc is not None:
			l["desc"] = desc
			flag += 1
		return flag

	def set_clue(self, lm_id, game_id, clue):
		l = DBMock.fetch_lm(lm_id, game_id)
		flag = 0
		if clue is not None:
			l["clue"] = clue
			flag += 1
		return flag

	def set_question(self, lm_id, game_id, prompt, answer=None):
		l = DBMock.fetch_lm(lm_id, game_id)
		flag = 0
		if prompt is not None:
			l["question"] = prompt
			flag += 1
		if answer is not None:
			if flag is 0 and l["question"] is None:
				raise SettingAnswerWithNoQuestionException
			l["answer"] = answer
			flag += 1
		return flag
