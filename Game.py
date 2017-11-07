from GameGameMaker import GameGameMaker
from GameTeam import GameTeam
from Landmark import Landmark


class Game(GameGameMaker, GameTeam):
    def __init__(self):
        self.on = False
        self.myUserList = []
        self.landmarkList = []

    def start(self) -> bool:
        self.on = True
        return self.on

    def stop(self) -> bool:
        self.on = False
        return self.on

    def get_landmarks(self) -> list:
        return self.landmarkList

    def add_landmark(self, landmark: Landmark) -> bool:
        self.landmarkList.append(Landmark)
        return True

    def get_clue(self, index: int):
        return self.landmarkList[index].get_clue

    def get_question(self, index: int):
        return self.landmarkList[index].get_confirmation

    def check_answer(self, index: int, answer: str):
        return self.landmarkList[index].check_answer(answer)

    def get_landmark_by_name(self, name) -> Landmark:
        for i in self.landmarkList:
            if i.name == name:
                return i
