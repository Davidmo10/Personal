

class Status():
    def __init__(self):
        self.score = 0
        self.teamid = 0
        self.currentlm = None
        self.pendingquestion = None

    def getTeamId(self) -> int:
        return self.teamid

    def getLastlm(self) -> str:
        return self.currentlm

    def getPendingQuestion(self) -> str:
        return self.pendingquestion

    def getScore(self) -> int:
        return self.score
    
    
