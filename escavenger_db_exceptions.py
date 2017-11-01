
class InvalidGameException(Exception):
    def __init__(self, value=""):
        self.parameter = value
    def __str__(self):
        return repr(self.parameter)
        
class InvalidUserException(Exception):
    def __init__(self, value=""):
        self.parameter = value
    def __str__(self):
        return repr(self.parameter)
        
class InvalidGameStateException(Exception):
    def __init__(self, value=""):
        self.parameter = value
    def __str__(self):
        return repr(self.parameter)
        
class InvalidTeamStateException(Exception):
    def __init__(self, value=""):
        self.parameter = value
    def __str__(self):
        return repr(self.parameter)
class InvalidLandmarkException(Exception):
    def __init__(self, value=""):
        self.parameter = value
    def __str__(self):
        return repr(self.parameter)
class InvalidTeamException(Exception):
    def __init__(self, value=""):
        self.parameter = value
    def __str__(self):
        return repr(self.parameter)

class EmptyGameSetException(Exception):
    def __init__(self, value=""):
        self.parameter = value
    def __str__(self):
        return repr(self.parameter)
        
class EmptyTeamListException(Exception):
    def __init__(self, value=""):
        self.parameter = value
    def __str__(self):
        return repr(self.parameter)
        
class LandmarkAlreadyInGameException(Exception):
    def __init__(self, value=""):
        self.parameter = value
    def __str__(self):
        return repr(self.parameter)
        
class SettingAnswerWithNoQuestionException(Exception):
    def __init__(self, value=""):
        self.parameter = value
    def __str__(self):
        return repr(self.parameter)
 
